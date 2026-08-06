
# GeoSPARQL FeatureCollection (Model)

`ogc.geosparql.vocabulary.classes.featurecollection` *v0.1*

A building block defining a GeoSPARQL FeatureCollection

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyFeatureCollection a geo:FeatureCollection ;
    rdfs:member ex:MyFeature .

ex:MyFeature a geo:Feature ;
  geo:hasGeometry ex:MyFeatureExactGeom .

ex:MyFeatureExactGeom a sf:Polygon, geo:Geometry ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/classes/featurecollection`

