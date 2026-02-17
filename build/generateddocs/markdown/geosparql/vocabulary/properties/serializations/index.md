
# GeoSPARQL Ontology: Serializations (Model)

`ogc.geosparql.vocabulary.properties.serializations` *v0.1*

Serializations of geometry formats supported by GeoSPARQL

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### GeoSPARQL Specification Well-Known Text Serialization example
#### ttl
```ttl
@prefix my: <http://example.org/ApplicationSchema#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

my:AExactGeom rdf:type geo:Geometry, sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .
```


### GeoSPARQL Specification GML Serialization example
#### ttl
```ttl
@prefix my: <http://example.org/ApplicationSchema#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

my:AExactGeom rdf:type geo:Geometry, sf:Polygon ;
     geo:asGML "<gml:Polygon xmlns:gml=\"http://www.opengis.net/ont/gml\" srsName=\"http://www.opengis.net/def/crs/OGC/1.3/CRS84\"><gml:exterior><gml:LinearRing><gml:posList>-83.6 34.1 -83.2 34.1 -83.2 34.5 -83.6 34.5 -83.6 34.1</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon>"^^geo:gmlLiteral .
```


### GeoSPARQL Specification KML Serialization example
#### ttl
```ttl
@prefix my: <http://example.org/ApplicationSchema#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

my:AExactGeom rdf:type geo:Geometry, sf:Polygon ;
     geo:asKML "<Polygon><outerBoundaryIs><LinearRing><coordinates>-83.6,34.1 -83.2,34.1 -83.2,34.5 -83.6,34.5 -83.6,34.1</coordinates></LinearRing></outerBoundaryIs></Polygon>"^^geo:asKML .
```


### GeoSPARQL Specification GeoJSON Serialization example
#### ttl
```ttl
@prefix my: <http://example.org/ApplicationSchema#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

my:AExactGeom rdf:type geo:Geometry, sf:Polygon ;
     geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[-83.6, 34.1], [-83.2, 34.1], [-83.2, 34.5], [-83.6, 34.5], [-83.6, 34.1]]]}"^^geo:geoJSONLiteral .
```


### GeoSPARQL Specification DGGS Serialization example
#### ttl
```ttl
@prefix my: <http://example.org/ApplicationSchema#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

my:AExactGeom rdf:type geo:Geometry, sf:Polygon ;
    geo:asDGGS "<https://h3geo.org/res/7> CELLIST( '87f15d9acffffff', '87f143749ffffff', '87f15d9a1ffffff', '87f143296ffffff', '87f15d910ffffff', '87f143648ffffff', '87f14374bffffff', '87f15d9aeffffff', '87f15d98dffffff', '87f14366bffffff', '87f15d912ffffff', '87f14374dffffff', '87f15d9a5ffffff', '87f15d832ffffff', '87f15d914ffffff', '87f14364cffffff', '87f15d916ffffff', '87f15d9a9ffffff', '87f15d836ffffff', '87f15d988ffffff', '87f143748ffffff', '87f15d9abffffff', '87f143668ffffff', '87f15d9adffffff', '87f15d98cffffff', '87f14366affffff', '87f143649ffffff', '87f14366cffffff', '87f15d810ffffff', '87f143661ffffff', '87f15d913ffffff', '87f14364bffffff', '87f14366effffff', '87f14364dffffff', '87f15d9a8ffffff', '87f143292ffffff', '87f15d814ffffff', '87f143665ffffff', '87f15d9aaffffff', '87f15d989ffffff', '87f15d816ffffff' )"^^geo:dggsLiteral .
```

## Sources

* [Spec section](https://opengeospatial.github.io/ogc-geosparql/geosparql11/document.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/properties/serializations`

