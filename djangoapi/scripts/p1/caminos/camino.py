from myLib.db import Db
from myLib import p1Settings

class Caminos:
    
    def insert(self, d: dict):
        db = Db()
        
        # Redondear coord
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", 
                 [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        #para ver si la linea esta bien dibujada 
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", 
                 [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria de linea invalida', 'data': None}
            
        # Insert los datos
        cons = """
            INSERT INTO d.caminos (nombre, tipo_superficie, ancho_m, estado_mantenimiento, pendiente_max_pct, geom)
            VALUES (%s, %s, %s, %s, %s, ST_GeomFromText(%s, %s))
            RETURNING id
        """
        values = [d['nombre'], d['tipo_superficie'], d['ancho_m'], d['estado_mantenimiento'], d['pendiente_max_pct'], geom_snapped, p1Settings.EPSG_CODE]
        db.query(cons, values)
        
        new_id = db.result[0]['id']
        db.disconnect()
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': new_id}]}
#actualizar 
    def update(self, d: dict):
        db = Db()
        db.query("SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001)) AS geom_snapped", [d['geom'], p1Settings.EPSG_CODE])
        geom_snapped = db.result[0]['geom_snapped']
        
        db.query("SELECT ST_IsValid(ST_GeomFromText(%s, %s)) AS is_valid", [geom_snapped, p1Settings.EPSG_CODE])
        if not db.result[0]['is_valid']:
            db.disconnect()
            return {'ok': False, 'message': 'Geometria de linea invalida', 'data': None}
            
        cons = """
            UPDATE d.caminos 
            SET nombre=%s, tipo_superficie=%s, ancho_m=%s, estado_mantenimiento=%s, pendiente_max_pct=%s, geom=ST_GeomFromText(%s, %s)
            WHERE id=%s
        """
        values = [d['nombre'], d['tipo_superficie'], d['ancho_m'], d['estado_mantenimiento'], d['pendiente_max_pct'], geom_snapped, p1Settings.EPSG_CODE, d['id']]
        db.query(cons, values)
        
        filas_actualizadas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': filas_actualizadas}]}
#elimianr 
    def delete(self, d: dict):
        db = Db()
        cons = "DELETE FROM d.caminos WHERE id = %s"
        db.query(cons, [d['id']])
        filas_borradas = db.result
        db.disconnect()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': filas_borradas}]}

    def selectAsDicts(self, d: dict):
        db = Db(getRowsAsDicts=True)
        cons = """
            SELECT id, nombre, tipo_superficie, ancho_m, estado_mantenimiento, pendiente_max_pct, ST_AsText(geom) as geom 
            FROM d.caminos 
            WHERE id = %s
        """
        db.query(cons, [d['id']])
        data = db.result
        db.disconnect()
        if len(data) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
        return {'ok': True, 'message': 'Data retrieved', 'data': data}
    