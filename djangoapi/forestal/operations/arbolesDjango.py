from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.forms.models import model_to_dict
from forestal.models import Arboles
from scripts.p1.myLib import p1Settings

class ArbolesDjango:
    
    def insert(self, d: dict):
        cur = connection.cursor()
        
        # Redondear coord: 
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        # Validar
        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        # para comprobar que el arbol este dentro de alguna parcela
        query_within = "SELECT id FROM d.parcelas WHERE ST_Within(ST_GeomFromText(%s, %s), geom)"
        cur.execute(query_within, [snapped_wkt_geometry, p1Settings.EPSG_CODE])
        if len(cur.fetchall()) == 0:
            return {'ok': False, 'message': 'El arbol no esta dentro de la parcela', 'data': None}
            
        # para guardar 
        d['geom'] = g
        b = Arboles(**d)
        b.save()
        
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': b.id}]}
#actualizar 
    def update(self, d: dict):
        cur = connection.cursor()
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        # Al mover el arbol debe caer dentro de una parcela
        query_within = "SELECT id FROM d.parcelas WHERE ST_Within(ST_GeomFromText(%s, %s), geom)"
        cur.execute(query_within, [snapped_wkt_geometry, p1Settings.EPSG_CODE])
        if len(cur.fetchall()) == 0:
            return {'ok': False, 'message': 'arbol rechazado, quedo fuera de la parcela', 'data': None}

        f = Arboles.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        b = l[0]
        b.geom = g
        b.especie = d['especie']
        b.diametro_cm = d['diametro_cm']
        b.altura_m = d['altura_m']
        b.volumen_m3 = d['volumen_m3']
        b.calidad_madera = d['calidad_madera']
        b.save()
        
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': 1}]}
#eliminar 
    def delete(self, d: dict):
        f = Arboles.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        b = l[0]
        b.delete()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': 1}]}

    def selectAsDicts(self, d: dict):
        f = Arboles.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
            
        b = l[0]
        dic = model_to_dict(b)
        dic['geom'] = b.geom.wkt 
        return {'ok': True, 'message': 'Data retrieved', 'data': [dic]}
    