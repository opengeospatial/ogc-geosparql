
# GeoSPARQL Ontology (Model)

`ogc.geosparql.geosparql.classes.feature` *v0.1*

A building block defining a GeoSPARQL Feature

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## GeoSPARQL Feature

A discrete spatial phenomenon in a universe of discourse
## Examples

### Example
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

ex:C
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  ex:hasExactGeometry ex:CExactGeom ;
  ex:hasPointGeometry ex:CPointGeom ;
  geo:hasDefaultGeometry ex:CExactGeom ;
  geo:hasGeometry ex:CExactGeom ;
  geo:sfEquals ex:C ;
  geo:ehEquals ex:C ;
  geo:rcc8eq ex:C ;
  geo:sfDisjoint ex:B ;
  geo:ehDisjoint ex:B ;
  geo:rcc8dc ex:B .

ex:CExactGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Polygon xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.2 34.3 -83.0 34.3 -83.0 34.5 -83.2 34.5 -83.2 34.3</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon>
    """^^geo:gmlLiteral .
```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/geosparql/classes/feature`

