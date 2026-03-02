
# GeoSPARQL Non SF Functions (Model)

`ogc.geosparql.geof.nonsf` *v0.1*

The geof:is3D function tests if a given GeoSPARQL geometry contains a third dimension

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Usage example of geof:sfEquals: SPARQL Query and sample data
A geometry should be equal to itself. The SPARQL query tests this equality relationsship using the function geof:sfEquals
#### sparql
```sparql
ask
where {
    ?f <http://www.opengis.net/ont/geosparql#sfEquals> ?f2 .
    ?f geov:expectedResult ?expresult .
    ?f <http://www.opengis.net/ont/geosparql#hasGeometry> ?fgeom . ?fgeom <http://www.opengis.net/ont/geosparql#asWKT> ?fgwkt .
    ?f2 <http://www.opengis.net/ont/geosparql#hasGeometry> ?f2geom . ?f2geom <http://www.opengis.net/ont/geosparql#asWKT> ?f2gwkt .
    FILTER (<http://www.opengis.net/def/function/geosparql/sfEquals>(?fgwkt,?f2gwkt)=true)
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

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/geof/nonsf`

