
# GeoSPARQL Geometry Dimension Properties (Model)

`ogc.geosparql.geosparql.properties.geometry.dimension` *v0.1*

Properties which can be used to describe a geometry's dimensionality

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## GeoSPARQL Geometry Dimensionality

This building block includes properties which describe dimensionality of geo:Geometry

## Examples

### A two-dimensional polygon
A two-dimensional polygon described with the properties geo:dimension, geo:coordinateDimension and geo:spatialDimension .
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:dimension_example
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  skos:definition """A two-dimensional polygon""" ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"""^^geo:wktLiteral .
```

## Sources

* [Spec section](https://opengeospatial.github.io/ogc-geosparql/geosparql11/document.html#_property_geodimension)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/geosparql/properties/geometry/dimension`

