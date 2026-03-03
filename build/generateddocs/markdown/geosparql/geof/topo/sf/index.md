
# GeoSPARQL Topological Query Functions: Simple Features (Model)

`ogc.geosparql.geof.topo.sf` *v0.1*

Simple Feature Topological Query Functions

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Usage example of geof:sfEquals: SPARQL Query and sample data
A geometry should be equal to itself. The SPARQL query tests this equality relationship using the function geof:sfEquals
#### sparql
```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

ASK
WHERE {
    ?f geo:sfEquals ?f2 .
    ?f geo:hasGeometry ?fgeom . ?fgeom geo:asWKT ?fgwkt .
    ?f2 geo:hasGeometry ?f2geom . ?f2geom geo:asWKT ?f2gwkt .
    FILTER (geof:sfEquals(?fgwkt,?f2gwkt)=true)
}
```

#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:sfEquals ex:MyPlace .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
```


### Usage example of geof:sfDisjoint: SPARQL Query and sample data
Two disjoint geometries. The SPARQL query tests their disjointness using the function geof:sfDisjoint
#### sparql
```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

ASK
WHERE {
    ?f geo:sfDisjoint ?f2 .
    ?f geo:hasGeometry ?fgeom . ?fgeom geo:asWKT ?fgwkt .
    ?f2 geo:hasGeometry ?f2geom . ?f2geom geo:asWKT ?f2gwkt .
    FILTER (geof:sfDisjoint(?fgwkt,?f2gwkt)=true)
}
```

#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix geov: <http://www.opengis.net/def/geosparql/validator/> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:sfDisjoint ex:MyPlace2 .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .

ex:MyPlace2
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlace2Geom ;
  geo:sfDisjoint ex:MyPlace .

ex:MyPlace2Geom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.4 34.1, -83.4 34.3, -83.6 34.3, -83.6 34.1))"^^geo:wktLiteral  .
```


### Usage example of geof:sfCrosses: SPARQL Query and sample data
Two disjoint geometries. The SPARQL query tests the crosses relation using the function geof:sfCrosses
#### sparql
```sparql
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

ASK
WHERE {
    ?f geo:sfCrosses ?f2 .
    ?f geo:hasGeometry ?fgeom . ?fgeom geo:asWKT ?fgwkt .
    ?f2 geo:hasGeometry ?f2geom . ?f2geom geo:asWKT ?f2gwkt .
    FILTER (geof:sfCrosses(?fgwkt,?f2gwkt)=true)
}
```

#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlaceGeom ; .

ex:MyPlaceGeom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .

ex:MyPlace2 rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlace2Geom ;
     geo:sfCrosses ex:MyPlace .

ex:MyPlace2Geom rdf:type sf:LineString ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)"^^geo:wktLiteral .
```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/geof/topo/sf`

