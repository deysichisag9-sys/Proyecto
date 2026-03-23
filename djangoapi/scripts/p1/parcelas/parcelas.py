from myLib.db import Db
from myLib import p1Settings

class ParcelasOOP:
    
    def insert(self, d: dict):
        db = Db()
        
        # 1. Redondear coordenadas a 0.0001
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", 
                 [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        # 2. Validar que el polígono esté bien dibujado
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria invalida', 'data': None}
            
        # 3. Comprobar que NO se interseque con otra parcela existente
        db.query("SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s))", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if len(db.result) > 0:
            db.disconnect()
            return {'ok': False, 'message': 'El poligono se interseca con parcelas existentes', 'data': db.result}
            
        # 4. Insertar los datos
        cons = """
            INSERT INTO d.parcelas (nombre, propietario, area_ha, tipo_bosque, estado_legal, geom)
            VALUES (%s, %s, %s, %s, %s, ST_GeomFromText(%s, %s))
            RETURNING id
        """
        values = [d['nombre'], d['propietario'], d['area_ha'], d['tipo_bosque'], d['estado_legal'], geom_snapped, p1Settings.EPSG_CODE]
        db.query(cons, values)
        
        new_id = db.result[0]['id']
        db.disconnect()
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': new_id}]}

    def update(self, d: dict):
        db = Db()
        
        # Redondear y validar igual que en insert
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria invalida', 'data': None}
            
        # Comprobar intersecciones (¡excluyendo la parcela que estamos actualizando!)
        db.query("SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s)) AND id != %s", 
                 [geom_snapped, p1Settings.EPSG_CODE, d['id']])
        if len(db.result) > 0:
            db.disconnect()
            return {'ok': False, 'message': 'El poligono se interseca con parcelas existentes', 'data': db.result}
            
        # Actualizar
        cons = """
            UPDATE d.parcelas 
            SET nombre=%s, propietario=%s, area_ha=%s, tipo_bosque=%s, estado_legal=%s, geom=ST_GeomFromText(%s, %s)
            WHERE id=%s
        """
        values = [d['nombre'], d['propietario'], d['area_ha'], d['tipo_bosque'], d['estado_legal'], geom_snapped, p1Settings.EPSG_CODE, d['id']]
        db.query(cons, values)
        
        # El profesor pide que update devuelva 'rows_updated'
        filas_actualizadas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': filas_actualizadas}]}

    def delete(self, d: dict):
        db = Db()
        cons = "DELETE FROM d.parcelas WHERE id = %s"
        db.query(cons, [d['id']])
        
        # El profesor pide que delete devuelva 'rows_deleted'
        filas_borradas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': filas_borradas}]}

    def selectAsDicts(self, d: dict):
        # Usamos getRowsAsDicts=True para que nos devuelva un diccionario automáticamente
        db = Db(getRowsAsDicts=True)
        cons = """
            SELECT id, nombre, propietario, area_ha, tipo_bosque, estado_legal, ST_AsText(geom) as geom 
            FROM d.parcelas 
            WHERE id = %s
        """
        db.query(cons, [d['id']])
        
        data = db.result
        db.disconnect()
        
        if len(data) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
            
        return {'ok': True, 'message': 'Data retrieved', 'data': data}