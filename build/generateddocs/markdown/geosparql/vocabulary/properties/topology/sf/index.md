
# GeoSPARQL Topology: Simple Feature Properties (Model)

`ogc.geosparql.vocabulary.properties.topology.sf` *v0.1*

Properties which can be used to describe the topology of geometries using Simple Features relations

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### sfEquals relation example
A feature is related to itself using the geo:sfEquals relation.
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

* [Spec section](https://opengeospatial.github.io/ogc-geosparql/geosparql11/document.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/properties/topology/sf`

