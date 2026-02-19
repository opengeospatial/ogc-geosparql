
# GeoSPARQL Geometry Properties (Model)

`ogc.geosparql.vocabulary.properties.geometry` *v0.1*

Properties which can be used to describe a geometry's attributes

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### A simple geometry
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral ;
    geo:isSimple "true"^^xsd:boolean .
```


### An empty and a non-empty geometry
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyGeom rdf:type sf:LineString ;
    geo:asWKT ""^^geo:wktLiteral ;
    geo:isEmpty "true"^^xsd:boolean .
```

#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral ;
    geo:isSimple "false"^^xsd:boolean .
```

## Sources

* [Spec section](https://opengeospatial.github.io/ogc-geosparql/geosparql11/document.html#geometry_properties)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/properties/geometry`

