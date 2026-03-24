 from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from buildings2.models import Parcelas
from myLib import p1Settings

class ParcelasDjango:
    
    def insert(self, d: dict):
        cur = connection.cursor()
        
        # 1. Redondear coordenadas a 0.0001 (Igual que el profesor en insert3)
        query = "SELECT ST_AsText(ST_SnapToGrid(ST_GeomFromText(%s, %s), 0.0001))"
        cur.execute(query, [d['geom'], p1Settings.EPSG_CODE])
        snapped_wkt_geometry = cur.fetchall()[0][0]

        # 2. Validar con GEOSGeometry de Django
        g = GEOSGeometry(snapped_wkt_geometry, srid=p1Settings.EPSG_CODE)
        if not g.valid:
            return {'ok': False, 'message': 'Invalid geometry', 'data': None}
            
        # 3. Comprobar intersecciones 
        query_intersect = "SELECT id FROM d.parcelas WHERE ST_Intersects(geom, ST_GeomFromText(%s, %s))"
        cur.execute(query_intersect, [snapped_wkt_geometry, p1Settings.EPSG_CODE])
        if len(cur.fetchall()) > 0:
            return {'ok': False, 'message': 'El poligono se interseca con parcelas existentes', 'data': None}
            
        # 4. ¡LA MAGIA DE DJANGO! Guardar en la base de datos
        # Reemplazamos el texto de la geometría por el objeto GEOS válido
        d['geom'] = g
        b = Parcelas(**d) # Empaqueta todo el diccionario
        b.save()          # Lo guarda automáticamente en PostgreSQL
        
        # Devolvemos el diccionario exacto que pide el PDF
        return {'ok': True, 'message': 'Data inserted', 'data': [{'id': b.id}]}
    