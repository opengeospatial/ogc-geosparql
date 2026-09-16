
# Simple Features Vocabulary (Model)

`ogc.geosparql.simplefeatures` *v0.1*

The Simple Features vocabulary defines additional geometry types connected to the GeoSPARQL type hierarchy

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Point Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPointGeom a sf:Point ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.4 34.3)"^^geo:wktLiteral .

```


### MultiPoint Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyMultiPointGeom a sf:MultiPoint ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> MultiPoint((-83.4 34.3),(-85.2, 32.1))"^^geo:wktLiteral .

```


### Line Geometry
A LineString with exactly 2 Points
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyLineGeom a sf:Line ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)"^^geo:wktLiteral .

```


### LinearRing Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyLinearRingGeom a sf:LinerRing ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LinearRing(-83.4 34.0, -83.3 34.3,-83.4 34.0)"^^geo:wktLiteral .

```


### LineString Geometry
A LineString is a Curve with linear interpolation between Points. Each consecutive pair of Points defines a Line segment.
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyLineStringGeom a sf:LineString ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)"^^geo:wktLiteral .

```


### MultiLineString Geometry
A MultiLineString is a MultiCurve whose elements are LineStrings.
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyMultiLineStringGeom a sf:MultiLineString ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> MultiLineString((-83.4 34.0, -83.3 34.3), (-80.4 30.0, -85.3 38.3))"^^geo:wktLiteral .
```


### Polygon Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPolygonGeom a sf:Polygon ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
```


### MultiPolygon Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyMultiPolygonGeom a sf:MultiPolygon ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> MultiPolygon(((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3)),((-80.2 30.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -80.2 30.3)))"^^geo:wktLiteral .
```


### Envelope Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyEnvelope a sf:Envelope ;
  sf:minimum ex:MyEnvelope_min ;
  sf:maximum ex:MyEnvelope_max .

ex:MyEnvelope_min a sf:Point ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-85.2, 32.1)"^^geo:wktLiteral .

ex:MyEnvelope_max a sf:Point ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.4 34.3)"^^geo:wktLiteral .

```


### GeometryCollection Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyGeometryCollection a sf:GeometryCollection ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> GeometryCollection(Point(-83.4 34.3),MultiPoint((-83.4 34.3),(-85.2, 32.1)),LineString(-83.4 34.0, -83.3 34.3))"^^geo:wktLiteral .
```


### Triangle Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyTriangle a sf:Triangle ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> TRIANGLE((0 0 0,0 1 0,1 1 0,0 0 0))"^^geo:wktLiteral .
```


### TIN Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyTinGeom a sf:TIN ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> TIN (((0 0 0, 0 0 1, 0 1 0, 0 0 0)), ((0 0 0, 0 1 0, 1 1 0, 0 0 0)))"^^geo:wktLiteral .




```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/simplefeatures`

