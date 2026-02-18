
# Simple Features Vocabulary (Model)

`ogc.geosparql.simplefeatures` *v0.1*

The Simple Features vocabulary defines additional geometry types connected to the GeoSPARQL type hierarchy

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

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


### LineString Geometry
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyLineStringGeom a sf:LineString> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)"^^geo:wktLiteral .

```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/simplefeatures`

