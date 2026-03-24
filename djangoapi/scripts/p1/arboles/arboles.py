from myLib.db import Db
from myLib import p1Settings

class Arboles:
    
    def insert(self, d: dict):
        db = Db()
        
        # Redondeo de laas  coord a 0.0001
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", 
                 [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        # Validar que el punto este bien (ST_IsValid)
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria de punto invalida', 'data': None}
            
        # Comprobar que el (arbol) este dentro de alguna parcela que exista
        db.query("""
            SELECT id FROM d.parcelas 
            WHERE ST_Within(ST_GeomFromText(%s, %s), geom)
        """, [geom_snapped, p1Settings.EPSG_CODE])
        
        if len(db.result) == 0:
            db.disconnect()
            return {'ok': False, 'message': 'El arbol rechazado: NO esta dentro de ninguna parcela', 'data': None}
            
        # 4. Insertar los que si funciona 
        cons = """
            INSERT INTO d.arboles (especie, diametro_cm, altura_m, volumen_m3, calidad_madera, geom)
            VALUES (%s, %s, %s, %s, %s, ST_GeomFromText(%s, %s))
            RETURNING id
        """
        values = [d['especie'], d['diametro_cm'], d['altura_m'], d['volumen_m3'], d['calidad_madera'], geom_snapped, p1Settings.EPSG_CODE]
        db.query(cons, values)
        
        new_id = db.result[0]['id'] #nuevo id 
        db.disconnect()
        return {'ok': True, 'message': 'Arbol insertado correctamente', 'data': [{'id': new_id}]}
#actualizar
    def update(self, d: dict):
        db = Db()
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria de punto invalida', 'data': None}
            
        # Al actualizar, también debe seguir dentro de una parcela 
        db.query("SELECT id FROM d.parcelas WHERE ST_Within(ST_GeomFromText(%s, %s), geom)", [geom_snapped, p1Settings.EPSG_CODE])
        if len(db.result) == 0:
            db.disconnect()
            return {'ok': False, 'message': 'Arbol rechazado: al moverlo quedo fuera de las parcelas', 'data': None}
            
        cons = """
            UPDATE d.arboles 
            SET especie=%s, diametro_cm=%s, altura_m=%s, volumen_m3=%s, calidad_madera=%s, geom=ST_GeomFromText(%s, %s)
            WHERE id=%s
        """
        values = [d['especie'], d['diametro_cm'], d['altura_m'], d['volumen_m3'], d['calidad_madera'], geom_snapped, p1Settings.EPSG_CODE, d['id']]
        db.query(cons, values)
        
        filas_actualizadas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': filas_actualizadas}]}

    def delete(self, d: dict):
        db = Db()
        cons = "DELETE FROM d.arboles WHERE id = %s"
        db.query(cons, [d['id']])
        filas_borradas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': filas_borradas}]}

    def selectAsDicts(self, d: dict):
        db = Db(getRowsAsDicts=True)
        cons = """
            SELECT id, especie, diametro_cm, altura_m, volumen_m3, calidad_madera, ST_AsText(geom) as geom 
            FROM d.arboles 
            WHERE id = %s
        """
        db.query(cons, [d['id']])
        data = db.result
        db.disconnect()
        if len(data) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
        return {'ok': True, 'message': 'Data retrieved', 'data': data}