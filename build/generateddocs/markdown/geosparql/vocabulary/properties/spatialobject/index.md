
# GeoSPARQL SpatialObject Properties (Model)

`ogc.geosparql.vocabulary.properties.spatialobject` *v0.1*

The properties defined for a geo:SpatialObject

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### GeoSPARQL Specification geo:hasSize and geo:hasMetricSize example
Usage of the properties geo:hasSize and geo:hasMetricSize. In a standard case, subproperties like geo:hasArea or geo:hasLength should be used
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix qudt: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:hasMetricSize "4.079967948035431E8"^^xsd:double ;
  geo:hasSize ex:MyPlace_size .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .

ex:MyPlace_size a geo:SpatialMeasure ;
          qudt:numericValue "101064.28" ;
          qudt:unit qudt:AC .

```


### GeoSPARQL Specification geo:hasLength and geo:hasMetricLength example
Usage of the properties geo:hasLength and geo:hasMetricLength. The length of a polygon is given in meters (geo:hasMetricLength) and foot(geo:hasLength).
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix qudt: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:hasMetricLength "34531.762814738206"^^xsd:double ;
  geo:hasLength ex:MyPlace_length .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)"^^geo:wktLiteral .

ex:MyPlace_length a geo:SpatialMeasure ;
          qudt:numericValue "113293.1850877238" ;
          qudt:unit qudt:FT .

```


### GeoSPARQL Specification geo:hasPerimeterLength and geo:hasMetricPerimeterLength example
Usage of the properties geo:hasPerimeterLength and geo:hasMetricPerimeterLength. The perimeter length of a polygon is given in meters (geo:hasMetricPerimeterLength) and miles (geo:hasPerimeterLength).
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix qudt: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:hasMetricPerimeterLength "81151.59235053362"^^xsd:double ;
  geo:hasArea ex:MyPlace_perimeterLength .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .

ex:MyPlace_perimeterLength rdf:type geo:SpatialMeasure ;
        qudt:numericValue "50.42" ;
        qudt:unit qudt:MI .
```


### GeoSPARQL Specification geo:hasArea and geo:hasMetricArea example
Usage of the properties geo:hasArea and geo:hasMetricArea. The area of a polygon is given in squaremeters (geo:hasMetricArea) and acres (geo:hasArea).
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix qudt: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:hasMetricArea "4.079967948035431E8"^^xsd:double ;
  geo:hasArea ex:MyPlace_area .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .

ex:MyPlace_area a geo:SpatialMeasure ;
          qudt:numericValue "101064.28" ;
          qudt:unit qudt:AC .

```


### GeoSPARQL Specification geo:hasVolume and geo:hasMetricVolume example
Usage of the properties geo:hasVolume and geo:hasMetricVolume. The volume of a polygon is given in cubic meters (geo:hasMetricVolume) and gallons (geo:hasVolume). Note that for a property geo:hasVolume to be set, the geometry does not necessarily have to be defined as a 3D geometry.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix qudt: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:hasMetricVolume "100"^^xsd:double ;
  geo:hasArea ex:MyPlace_volume .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .

ex:MyPlace_volume a geo:SpatialMeasure ;
          qudt:numericValue "26417.2" ;
          qudt:unit qudt:GAL_US .

```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/properties/spatialobject`

