from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from buildings2.models import Parcelas
from myLib import p1Settings

class ParcelasDjango:
    
    def insert(self, d: dict):
        cur = connection.cursor()
        
        # Coord para redondear 
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        # observar la geomtria:  GEOSGeometry de Django
        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        #  comprobaccion de las  interseccion 
        query_intersect = "SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s))"
        cur.execute(query_intersect, [snapped_wkt_geometry, p1Settings.EPSG_CODE])
        if len(cur.fetchall()) > 0:
            return {'ok': False, 'message': 'existe interseccion con el poligono', 'data': None}
            
        
        # agrega una componente espacial (es decir toma la inf de guarda de g)
        d['geom'] = g
        b = Parcelas(**d) # guarda  todo el diccionario
        b.save()          #  guarda automaticament en PostgreSQL
        
        # Resultados 
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': b.id}]}
    
     #actualizar datos 
    def update(self, d: dict):
        cur = connection.cursor()
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        # Comprobamos intersecciones, pero ignoramos la propia parcela que estamos editando
        query_intersect = "SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s)) AND id != %s"
        cur.execute(query_intersect, [snapped_wkt_geometry, p1Settings.EPSG_CODE, d['id']])
        if len(cur.fetchall()) > 0:
            return {'ok': False, 'message': 'El poligono choca con otra parcela', 'data': None}

        # Buscamos la parcela con Django
        f = Parcelas.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        # Actualizamos y guardamos
        b = l[0]
        b.geom = g
        b.nombre = d['nombre']
        b.propietario = d['propietario']
        b.area_ha = d['area_ha']
        b.tipo_bosque = d['tipo_bosque']
        b.estado_legal = d['estado_legal']
        b.save()
        
        return {'ok': True, 'message': 'Data updated', 'data': [{'rows_updated': 1}]}

    def delete(self, d: dict):
        # Buscamos y borramos con una sola orden de Django
        f = Parcelas.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': f"No data found with id {d['id']}", 'data': None}
        
        b = l[0]
        b.delete()
        return {'ok': True, 'message': 'Data deleted', 'data': [{'rows_deleted': 1}]}

    def selectAsDicts(self, d: dict):
        f = Parcelas.objects.filter(id=d['id'])
        l = list(f)
        if len(l) == 0:
            return {'ok': False, 'message': 'No data found', 'data': None}
            
        b = l[0]
        # model_to_dict convierte automáticamente el objeto a un diccionario
        dic = model_to_dict(b)
        # Convertimos la geometría a texto legible (WKT) igual que hace tu profesor
        dic['geom'] = b.geom.wkt 
        return {'ok': True, 'message': 'Data retrieved', 'data': [dic]}