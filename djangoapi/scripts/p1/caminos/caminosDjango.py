from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.forms.models import model_to_dict
from forestal.models import Caminos
from myLib import p1Settings

class CaminosDjango:
    
    def insert(self, d: dict):
        cur = connection.cursor()
        
        # 1. Redondear coordenadas
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        # 2. Validar
        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        # 3. Guardar con Django
        d['geom'] = g
        b = Caminos(**d)
        b.save()
        
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': b.id}]}

    def update(self, d: dict):
        cur = connection.cursor()
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}

        f = Caminos.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        b = l[0]
        b.geom = g
        b.nombre = d['nombre']
        b.tipo_superficie = d['tipo_superficie']
        b.ancho_m = d['ancho_m']
        b.estado_mantenimiento = d['estado_mantenimiento']
        b.pendiente_max_pct = d['pendiente_max_pct']
        b.save()
        
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': 1}]}

    def delete(self, d: dict):
        f = Caminos.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        b = l[0]
        b.delete()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': 1}]}

    def selectAsDicts(self, d: dict):
        f = Caminos.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
            
        b = l[0]
        dic = model_to_dict(b)
        dic['geom'] = b.geom.wkt 
        return {'ok': True, 'message': 'Data retrieved', 'data': [dic]}
    