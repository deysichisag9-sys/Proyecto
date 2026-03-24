from myLib.db import Db
from myLib import p1Settings

class ParcelasOOP:
    
    def insert(self, d: dict):
        db = Db()
        
        # Redondear las coord 
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", 
                 [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        # para ver si el polgno este bien dibujado (OJITO)
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometry invalid', 'data': None}
            
        # que no haya intersecciones  con alguna  parcela existente
        db.query("SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s))", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if len(db.result) > 0:
            db.disconnect()
            return {'ok': False, 'message': 'Existe interseccion poligono', 'data': db.result}
            
        # 4. Insert  de los datos
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
        
        # Redondeo y validaccion  (algo similar que el insert) 
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria invalida', 'data': None}
            
        # es para poder comprobar intersecciones nuevamente 
        db.query("SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s)) AND id != %s", 
                 [geom_snapped, p1Settings.EPSG_CODE, d['id']])
        if len(db.result) > 0:
            db.disconnect()
            return {'ok': False, 'message': 'interssecciones con poligonos que existen', 'data': db.result}
            
        # Ojito para Actualizar
        cons = """
            UPDATE d.parcelas 
            SET nombre=%s, propietario=%s, area_ha=%s, tipo_bosque=%s, estado_legal=%s, geom=ST_GeomFromText(%s, %s)
            WHERE id=%s
        """
        values = [d['nombre'], d['propietario'], d['area_ha'], d['tipo_bosque'], d['estado_legal'], geom_snapped, p1Settings.EPSG_CODE, d['id']]
        db.query(cons, values)
        
        # Utilizacion de rows_updated (inf guardada)
        filas_actualizadas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': filas_actualizadas}]} #rows_updated(es para guardar el numero de registros / modificaciones)

    def delete(self, d: dict):
        db = Db()
        cons = "DELETE FROM d.parcelas WHERE id = %s"
        db.query(cons, [d['id']])
        
        # Informacion eliminada rows_deleted
        filas_borradas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': filas_borradas}]}

    def selectAsDicts(self, d: dict):
        # Usamos getRowsAsDicts=True para que  devuelva un diccionario (OJITO)
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
    