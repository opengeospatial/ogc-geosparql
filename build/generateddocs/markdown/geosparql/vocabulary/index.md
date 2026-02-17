
# GeoSPARQL Vocabulary (Model)

`ogc.geosparql.vocabulary` *v0.1*

The GeoSPARQL vocabulary allows to model geospatial features and geometries

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## GeoSPARQL ontology

The GeoSPARQL ontology defines core concepts of handling geospatial data in a Semantic Web context.

![GeoSPARQL ontology overview](assets/ont-overview.png)

The ontology defines a geo:SpatialObject as the superclass of the concepts geo:Feature and geo:Geometry.

Two application examples are given:

Example 1 consists of the application example included in the GeoSPARQL specification:

![GeoSPARQL ontology example spec](assets/03.png)

Each relation described in the GeoSPARQL ontology is included in a toy example.

Example 2 consists of a real world use case in Australia: Moreton Island

![GeoSPARQL ontology example Moreton Island](assets/03.png)

## Examples

### GeoSPARQL Specification Annex C Example
#### ttl
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

<http://www.opengis.net/ont/sf#Polygon>
  a rdfs:Class ;
  rdfs:subClassOf <http://www.opengis.net/ont/sf#Surface> .

<http://www.opengis.net/ont/sf#LineString>
  a rdfs:Class ;
  rdfs:subClassOf <http://www.opengis.net/ont/sf#Curve> .

<http://example.org/ApplicationSchema#PlaceOfInterest>
  a rdfs:Class ;
  rdfs:subClassOf <http://www.opengis.net/ont/geosparql#Feature> .

<http://www.opengis.net/ont/gml#Polygon>
  a rdfs:Class ;
  rdfs:subClassOf <http://www.opengis.net/ont/gml#Surface> .

<http://example.org/ApplicationSchema#hasExactGeometry>
  a rdf:Property ;
  rdfs:subPropertyOf <http://www.opengis.net/ont/geosparql#hasGeometry>, <http://www.opengis.net/ont/geosparql#hasDefaultGeometry> .

<http://example.org/ApplicationSchema#hasPointGeometry>
  a rdf:Property ;
  rdfs:subPropertyOf <http://www.opengis.net/ont/geosparql#hasGeometry> .

<http://example.org/ApplicationSchema#A>
  a <http://example.org/ApplicationSchema#PlaceOfInterest>, <http://www.opengis.net/ont/geosparql#Feature>, <http://www.opengis.net/ont/geosparql#SpatialObject> ;
  ex:hasExactGeometry ex:AExactGeom ;
  ex:hasPointGeometry ex:APointGeom ;
  geo:hasDefaultGeometry ex:AExactGeom ;
  geo:hasGeometry ex:AExactGeom ;
  geo:sfEquals ex:A ;
  geo:ehEquals ex:A ;
  geo:rcc8eq ex:A ;
  geo:sfIntersects ex:D ;
  geo:sfTouches ex:C ;
  geo:ehMeet ex:C ;
  geo:rcc8ec ex:C ;
  geo:sfContains ex:B ;
  geo:ehContains ex:B ;
  geo:sfOverlaps ex:D ;
  geo:ehOverlap ex:D ;
  geo:rcc8po ex:D ;
  geo:ehCovers ex:B ;
  geo:rcc8tppi ex:B .

ex:AExactGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:hasSerialization """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))
        
    """^^geo:wktLiteral ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Polygon xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.6 34.1 -83.2 34.1 -83.2 34.5 -83.6 34.5 -83.6 34.1</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon>
    """^^geo:gmlLiteral .

ex:APointGeom
  a <http://www.opengis.net/ont/sf#Point>, geo:Geometry, <http://www.opengis.net/ont/gml#Point> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.4 34.3)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Point xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.4 34.3</gml:pos></gml:Point>
    """^^geo:gmlLiteral .

ex:B
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  ex:hasExactGeometry ex:BExactGeom ;
  ex:hasPointGeometry ex:BPointGeom ;
  geo:hasDefaultGeometry ex:BExactGeom ;
  geo:hasGeometry ex:BExactGeom ;
  geo:sfEquals ex:B ;
  geo:ehEquals ex:B ;
  geo:rcc8eq ex:B ;
  geo:sfDisjoint ex:C ;
  geo:ehDisjoint ex:C ;
  geo:rcc8dc ex:C ;
  geo:sfWithin ex:A ;
  geo:ehCoveredBy ex:A ;
  geo:rcc8tpp ex:A .

ex:BExactGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.4 34.1, -83.4 34.3, -83.6 34.3, -83.6 34.1))
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Polygon xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.6 34.1 -83.4 34.1 -83.4 34.3 -83.6 34.3 -83.6 34.1</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon>
    """^^geo:gmlLiteral .

ex:BPointGeom
  a <http://www.opengis.net/ont/sf#Point>, geo:Geometry, <http://www.opengis.net/ont/gml#Point> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.5 34.2)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Point xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.5 34.2</gml:pos></gml:Point>
    """^^geo:gmlLiteral .

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

ex:CPointGeom
  a <http://www.opengis.net/ont/sf#Point>, geo:Geometry, <http://www.opengis.net/ont/gml#Point> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.1 34.4)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Point xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.1 34.4</gml:pos></gml:Point>
    """^^geo:gmlLiteral .

ex:D
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  ex:hasExactGeometry ex:DExactGeom ;
  ex:hasPointGeometry ex:DPointGeom ;
  geo:hasDefaultGeometry ex:DExactGeom ;
  geo:hasGeometry ex:DExactGeom ;
  geo:sfEquals ex:D ;
  geo:ehEquals ex:D ;
  geo:rcc8eq ex:D ;
  geo:sfIntersects ex:A .

ex:DExactGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.3 34.0, -83.1 34.0, -83.1 34.2, -83.3 34.2, -83.3 34.0))
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Polygon xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.3 34.0 -83.1 34.0 -83.1 34.2 -83.3 34.2 -83.3 34.0</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon>
    """^^geo:gmlLiteral .

ex:DPointGeom
  a <http://www.opengis.net/ont/sf#Point>, geo:Geometry, <http://www.opengis.net/ont/gml#Point> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.2 34.1)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Point xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.2 34.1</gml:pos></gml:Point>
    """^^geo:gmlLiteral .

ex:E
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  ex:hasExactGeometry ex:EExactGeom ;
  geo:hasDefaultGeometry ex:EExactGeom ;
  geo:hasGeometry ex:EExactGeom ;
  geo:sfEquals ex:E ;
  geo:ehEquals ex:E ;
  geo:rcc8eq ex:E ;
  geo:sfCrosses ex:A .

ex:EExactGeom
  a <http://www.opengis.net/ont/sf#LineString>, geo:Geometry, <http://www.opengis.net/ont/gml#LineString> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> LineString(-83.4 34.0, -83.3 34.3)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:LineString srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84" xmlns:gml="http://www.opengis.net/ont/gml"><gml:posList>-83.4 34.0 -83.3 34.3</gml:posList></gml:LineString>
    """^^geo:gmlLiteral .

ex:F
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  ex:hasExactGeometry ex:FExactGeom ;
  geo:hasDefaultGeometry ex:FExactGeom ;
  geo:hasGeometry ex:FExactGeom ;
  geo:sfEquals ex:F ;
  geo:ehEquals ex:F ;
  geo:rcc8eq ex:F ;
  geo:ehInside ex:A .

ex:FExactGeom
  a <http://www.opengis.net/ont/sf#Point>, geo:Geometry, <http://www.opengis.net/ont/gml#Point> ;
  geo:isEmpty false ;
  geo:isSimple true ;
  geo:dimension 2 ;
  geo:spatialDimension 2 ;
  geo:coordinateDimension 2 ;
  geo:asWKT """
        
            <http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.4 34.4)
        
    """^^geo:wktLiteral ;
  geo:asGML """
        <gml:Point xmlns:gml="http://www.opengis.net/ont/gml" srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.4 34.4</gml:pos></gml:Point>
    """^^geo:gmlLiteral .

```

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.6,34.1], 
                    [-83.2, 34.1], [-83.2, 34.5], 
                    [-83.6, 34.5], [-83.6, 34.1]]]
        },
       "properties":{"rdfs:label":"AExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false,
                     "geo:isSimple": true,
                     "geo:spatialDimension": 2 
                    }
    },    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.6,34.1], 
                    [-83.4, 34.1], [-83.4, 34.3], 
                    [-83.6, 34.3], [-83.6, 34.1]]]
        },
       "properties":{"rdfs:label":"BExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    },  { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-83.5, 34.2]
        },
       "properties":{"rdfs:label":"BPointGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:isEmpty": false,
                     "geo:isSimple": true,
                     "geo:spatialDimension": 2 
                    }
    },     
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.2, 34.3], 
                    [-83.0, 34.3], [-83.0, 34.5], 
                    [-83.2, 34.5], [-83.2, 34.3]]]
        },
       "properties":{"rdfs:label":"CExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    },    
    { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-83.1, 34.4]           
        },
       "properties":{"rdfs:label":"CPointGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    }, 
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.3, 34.0], 
                    [-83.1, 34.0], [-83.1, 34.2], 
                    [-83.3, 34.2], [-83.3, 34.0]]]
        },
       "properties":{"rdfs:label":"DExactGeom",
                     "geo:coordinateDimension": 2,
                     "geo:dimension": 2,
                     "geo:isEmpty": false,
                     "geo:isSimple": true,
                     "geo:spatialDimension":2      
                    }
    }, 
        { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-83.2, 34.1]           
        },
       "properties":{"rdfs:label":"DPointGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    }, 
    { "type": "Feature",
      "geometry": { "type": "LineString",
      "coordinates": [[-83.4, 34.0], 
                    [-83.3, 34.3]]
        },
       "properties":{"rdfs:label":"EExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2                
                    }
    }, 
    { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-83.4, 34.4]
        },
       "properties":{"rdfs:label":"FExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2
                    }
    }, 
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.5, 34.2], [-83.3, 34.2], [-83.3, 34.4], [-83.5, 34.4], [-83.5, 34.2]]]
        },
       "properties":{"rdfs:label":"GExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    },
            { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-83.4, 34.3]           
        },
       "properties":{"rdfs:label":"GPointGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    }, 
    { "type": "Feature",
      "geometry":null,
       "properties":{"rdfs:label":"HExactGeom",
               "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": true,                     
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                 }
    },
    { "type": "Feature",
      "geometry":null,
       "properties":{"rdfs:label":"HPointGeom",
               "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": true,                     
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                 }
    },
    { "type": "Feature",
      "geometry":null,
       "properties":{"rdfs:label":"IExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": true,                     
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    }, 
   { "type": "Feature",
      "geometry":null,
       "properties":{"rdfs:label":"IPointGeom",
               "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": true,                     
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                 }
    },
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-77.089005, 38.913574], [-77.029953, 38.913574], [-77.029953, 38.886321], [-77.089005, 38.886321], [-77.089005, 38.913574]]]
        },
       "properties":{"rdfs:label":"JExactGeom",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple":true ,
                     "geo:spatialDimension": 2        
                    }
    }, 
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-77.089005, 38.913574], [-77.029953, 38.913574], [-77.029953, 38.886321], [-77.089005, 38.886321], [-77.089005, 38.913574]]]
        },
       "properties":{"rdfs:label":"KExactGeom",
                     "geo:coordinateDimension": 2,
                     "geo:dimension": 2 ,
                     "geo:isEmpty":false ,
                     "geo:isSimple": true,
                     "geo:spatialDimension": 2
                    }
    },    
    { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [-88.38, 31.95]
        },
     "properties":{
       "rdfs:label":"LExactGeom",
       "geo:coordinateDimension": 2,
       "geo:dimension": 2, 
       "geo:isEmpty": false,
       "geo:isSimple": true ,
       "geo:spatialDimension": 2  
      }
    },     
    { "type": "Feature",
      "geometry": { "type": "Point",
      "coordinates": [31.95, -88.38]
        },
       "properties":{"rdfs:label":"MExactGeom",
       "geo:coordinateDimension": 2,
       "geo:dimension": 2, 
       "geo:isEmpty": false,
       "geo:isSimple": true ,
       "geo:spatialDimension": 2                  
       }
    } 
   ]
}
```

#### gml
```gml
<?xml version="1.0" encoding="utf-8" ?>
<ogr:FeatureCollection
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://ogr.maptools.org/ dataset_2.xsd"
     xmlns:ogr="http://ogr.maptools.org/"
     xmlns:gml="http://www.opengis.net/gml">
  <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-88.38 -88.38</gml:lowerCorner><gml:upperCorner>31.95 38.913574</gml:upperCorner></gml:Envelope></gml:boundedBy>                                                                                                                                                       
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.0">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.6 34.1</gml:lowerCorner><gml:upperCorner>-83.2 34.5</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.6 34.1 -83.2 34.1 -83.2 34.5 -83.6 34.5 -83.6 34.1</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>AExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.1">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.6 34.1</gml:lowerCorner><gml:upperCorner>-83.4 34.3</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.6 34.1 -83.4 34.1 -83.4 34.3 -83.6 34.3 -83.6 34.1</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>BExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.2">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.5 34.2</gml:lowerCorner><gml:upperCorner>-83.5 34.2</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.5 34.2</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>BPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.3">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.2 34.3</gml:lowerCorner><gml:upperCorner>-83.0 34.5</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.2 34.3 -83.0 34.3 -83.0 34.5 -83.2 34.5 -83.2 34.3</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>CExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.4">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.1 34.4</gml:lowerCorner><gml:upperCorner>-83.1 34.4</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.1 34.4</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>CPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.5">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.3 34.0</gml:lowerCorner><gml:upperCorner>-83.1 34.2</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.3 34.0 -83.1 34.0 -83.1 34.2 -83.3 34.2 -83.3 34.0</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>DExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.6">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.2 34.1</gml:lowerCorner><gml:upperCorner>-83.2 34.1</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.2 34.1</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>DPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.7">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.4 34.0</gml:lowerCorner><gml:upperCorner>-83.3 34.3</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:LineString srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:posList>-83.4 34.0 -83.3 34.3</gml:posList></gml:LineString></ogr:geometryProperty>
      <ogr:rdfs_label>EExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.8">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.4 34.4</gml:lowerCorner><gml:upperCorner>-83.4 34.4</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.4 34.4</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>FExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.9">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.5 34.2</gml:lowerCorner><gml:upperCorner>-83.3 34.4</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-83.5 34.2 -83.3 34.2 -83.3 34.4 -83.5 34.4 -83.5 34.2</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>GExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.10">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-83.4 34.3</gml:lowerCorner><gml:upperCorner>-83.4 34.3</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-83.4 34.3</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>GPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.11">
      <ogr:rdfs_label>HExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>true</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.12">
      <ogr:rdfs_label>HPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>true</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.13">
      <ogr:rdfs_label>IExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>true</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.14">
      <ogr:rdfs_label>IPointGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>true</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.15">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-77.089005 38.886321</gml:lowerCorner><gml:upperCorner>-77.029953 38.913574</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-77.089005 38.913574 -77.029953 38.913574 -77.029953 38.886321 -77.089005 38.886321 -77.089005 38.913574</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>JExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.16">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-77.089005 38.886321</gml:lowerCorner><gml:upperCorner>-77.029953 38.913574</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Polygon srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:exterior><gml:LinearRing><gml:posList>-77.089005 38.913574 -77.029953 38.913574 -77.029953 38.886321 -77.089005 38.886321 -77.089005 38.913574</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
      <ogr:rdfs_label>KExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.17">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:lowerCorner>-88.38 31.95 </gml:lowerCorner><gml:upperCorner>-88.38 31.95</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/OGC/1.3/CRS84"><gml:pos>-88.38 31.95</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>LExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
  <ogr:featureMember>
    <ogr:dataset_2 gml:id="dataset_2.18">
      <gml:boundedBy><gml:Envelope srsName="http://www.opengis.net/def/crs/EPSG/0/4326"><gml:lowerCorner>31.95 -88.38</gml:lowerCorner><gml:upperCorner>31.95 -88.38</gml:upperCorner></gml:Envelope></gml:boundedBy>
      <ogr:geometryProperty><gml:Point srsName="http://www.opengis.net/def/crs/EPSG/0/4326"><gml:pos>31.95 -88.38</gml:pos></gml:Point></ogr:geometryProperty>
      <ogr:rdfs_label>MExactGeom</ogr:rdfs_label>
      <ogr:geo_coordinateDimension>2</ogr:geo_coordinateDimension>
      <ogr:geo_dimension>2</ogr:geo_dimension>
      <ogr:geo_isEmpty>false</ogr:geo_isEmpty>
      <ogr:geo_isSimple>true</ogr:geo_isSimple>
      <ogr:geo_spatialDimension>2</ogr:geo_spatialDimension>
    </ogr:dataset_2>
  </ogr:featureMember>
</ogr:FeatureCollection>
```


### GeoSPARQL Specification Moreton Island Example
#### ttl
```ttl
@prefix : <https://example.com/dataset/geo-demo/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix locn: <http://www.w3.org/ns/locn#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sdo: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

@prefix dataset: <https://example.com/dataset/geo-demo> .
@prefix points: <https://example.com/dataset/geo-demo/points> .
@prefix polys: <https://example.com/dataset/geo-demo/polys> .

<https://example.com/dataset/geo-demo>
  a dcat:Dataset , owl:Ontology ;
  dcterms:title "GeoSPARQL 1.1 Example Dataset"@en ;
  dcterms:description """A demonstration dataset for of GeoSPARQL objects.
    
This example demonstrates GeoSPARQL 1.0 and new GeoSPARQL 1.1. geometry serializations (GeoJSON) of `Feature` instances, collected in instances of the new `FeatureCollection` class and a _suggestion_ for the use of [DCAT](https://www.w3.org/TR/vocab-dcat/) to package datasets. New GeoSPARQL 1.1. properties,  such as `hasBoundingBox`, are also used.

Note that GeoSPARQL 1.1 makes no recommendations regarding dataset-level data packaging, however DCAT is a well-used and generic dataset description ontology."""@en ;
  dcterms:publisher [
    a sdo:Organization ;
    sdo:name "Open Geospatial Consortium" ;
    sdo:url "https://www.ogc.org"^^xsd:anyURI ;
  ] ;
  dcterms:creator "OGC GeoSPARQL Standards Working Group" ;
  dcterms:created "2021-06-16"^^xsd:date ;
  dcterms:identifier "geo-demo"^^xsd:token ;
  dcterms:modified "2021-05-21"^^xsd:date ;
  dcterms:license "http://creativecommons.org/licenses/by/4.0/"^^xsd:anyURI ;
  dcterms:spatial [
    a dcterms:Location ;
    geo:hasBoundingBox [
      a geo:Geometry ;
      geo:asWKT "POLYGON ((96.0000 -45.0000, 96.0000 -9.0000, 168.0000 -9.0000, 168.0000 -45.0000, 96.0000 -45.0000))"^^geo:wktLiteral ;
      geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[ [96.0,-45.0],[96.0,-9.0], [168.0,-9.0], [168.0,-45.0], [96.0,-45.0]]]}"^^geo:geoJSONLiteral ;      
    ] ;
    locn:geometry "POLYGON ((96.0000 -45.0000, 96.0000 -9.0000, 168.0000 -9.0000, 168.0000 -45.0000, 96.0000 -45.0000))"^^geo:wktLiteral ;
    rdfs:comment "This spatial information for this dataset contains geo:hasBoundingBox, the GeoSPARQL style of bounding box, as well as locn:geometry, the DCAT style of bounding box" ;
  ] ;
  dcat:contactPoint [
    a vcard:Individual ;
    vcard:hasName "Nicholas Car" ;
    vcard:hasEmail "nick@kurrawong.ai"^^xsd:anyURI ;
    sdo:affiliation <https://kurrawong.ai> ;
  ] ;
  dcat:keyword "GeoSPARQL", "demonstration" , "Australia" ;
  rdfs:member
    points: ,
    polys: ;
.

points:
  a geo:FeatureCollection ;
  dcterms:identifier "points"^^xsd:token ;
  dcterms:title "Points Feature Collection" ;
  dcterms:description "A FeatureCollection of POINT instances"@en ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((150.467423 -33.491384, 150.467423 -34.3223631, 150.9920201 -34.3223631, 150.9920201 -33.491384, 150.467423 -33.491384))"^^geo:wktLiteral ;
  ] ;
  rdfs:member
    :camerons-corner ,
    :shorncliffe-point-1 ,
    :shorncliffe-point-2 ,
    :shorncliffe-point-3 ,
    :wyvenhoe ;
.

polys:
  a geo:FeatureCollection ;
  dcterms:identifier "polys"^^xsd:token ;
  dcterms:title "Polygons Feature Collection" ;
  dcterms:description "A FeatureCollection of POLYGON instances"@en ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((150.467423 -33.491384, 150.467423 -34.3223631, 150.9920201 -34.3223631, 150.9920201 -33.491384, 150.467423 -33.491384))"^^geo:wktLiteral ;
  ] ;
  rdfs:member
    :curlew-park ,
    :shorncliffe ,
    :sandgate-golf-club ,
    :queensland ,
    :australia ;
.

:camerons-corner
  a geo:Feature ;
  dcterms:identifier "camerons-corner"^^xsd:token ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POINT (141.0068201 -28.9911208)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [141.0068201, -28.9911208]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Cameron's Corner Point" ;
  geo:sfWithin :queensland , :australia ;
.

:shorncliffe-point-1
  a geo:Feature ;
  dcterms:identifier "shorncliffe-point-1"^^xsd:token ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POINT (153.0806193 -27.3336526)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.0806193, -27.3336526]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((152.8306193 -27.0836526, 153.3306193 -27.0836526, 153.3306193 -27.5836526, 152.8306193 -27.5836526, 152.8306193 -27.0836526))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[152.8306193, -27.0836526], [153.3306193, -27.0836526], [153.3306193, -27.5836526], [152.8306193, -27.5836526], [152.8306193, -27.0836526]]]}"^^geo:geoJSONLiteral ;
    rdfs:comment "This Bounding Box is calculated by extending a square boundary a certain distance (o.25 degrees) North, South, East & West from the Feature's POINT geometry." ;
  ] ;  
  dcterms:title "Shorncliffe Point 1" ;
  geo:sfWithin :queensland ;
.
:shorncliffe-point-2
  a geo:Feature ;
  dcterms:identifier "shorncliffe-point-2"^^xsd:token ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POINT (153.0880008 -27.3283533)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.0880008, -27.3283533]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (153.0880008 -27.3283533)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.0880008, -27.3283533]}"^^geo:geoJSONLiteral ;
    rdfs:comment "This geometry is redundant as a Feature with a POINT geometry will have the same value for a Centroid." ;
  ] ;
  dcterms:title "Shorncliffe Point 2" ;
  geo:sfWithin :queensland ;
.
:shorncliffe-point-3
  a geo:Feature ;
  dcterms:identifier "shorncliffe-point-3"^^xsd:token ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((152.8362412 -27.0753032, 153.3362412 -27.0753032, 153.3362412 -27.5753032, 152.8362412 -27.5753032, 152.8362412 -27.0753032))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[152.8362412, -27.0753032], [153.3362412, -27.0753032], [153.3362412, -27.5753032], [152.8362412, -27.5753032], [152.8362412, -27.0753032]]]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Shorncliffe Point 3" ;
  geo:sfWithin :queensland ;
.
:wyvenhoe
  a geo:Feature ;
  dcterms:identifier "wyvenhoe"^^xsd:token ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POINT (152.6282523 -27.3298868)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [152.6282523, -27.3298868]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Wyvenhoe Point" ;
  geo:sfWithin :queensland ;
.

:curlew-park
  a geo:Feature ;
  dcterms:identifier "curlew-park"^^xsd:token ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (153.0800692121883 -27.32985122185145)"^^geo:wktLiteral ;
     geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.0800692121883, -27.32985122185145]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0769448 -27.3270212, 153.0830388 -27.3270212, 153.0830388 -27.3329687, 153.0769448 -27.3329687, 153.0769448 -27.3270212))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0769448, -27.3270212], [153.0830388, -27.3270212], [153.0830388, -27.3329687], [153.0769448, -27.3329687], [153.0769448, -27.3270212]]]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0792623 -27.3270212, 153.0769448 -27.3309291, 153.0811505 -27.3329687, 153.0819016 -27.3304334, 153.0830388 -27.3295947, 153.0818801 -27.3277075, 153.0792623 -27.3270212))"^^geo:wktLiteral ;     
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0792623, -27.3270212], [153.0769448, -27.3309291], [153.0811505, -27.3329687], [153.0819016, -27.3304334], [153.0830388, -27.3295947], [153.0818801, -27.3277075], [153.0792623, -27.3270212]]]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Curlew Park" ;
  geo:sfWithin :queensland ;
.
:shorncliffe
  a geo:Feature ;
  dcterms:identifier "shorncliffe"^^xsd:token ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (153.072738950776 -27.32559331247693)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.072738950776, -27.32559331247693]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0691557 -27.3229035, 153.0760651 -27.3229035, 153.0760651 -27.3292706, 153.0691557 -27.3292706, 153.0691557 -27.3229035))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0691557, -27.3229035], [153.0760651, -27.3229035], [153.0760651, -27.3292706], [153.0691557, -27.3292706], [153.0691557, -27.3229035]]]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0695849 -27.3231323, 153.0691557 -27.3252293, 153.0697565 -27.3259918, 153.0710011 -27.3261443, 153.0714302 -27.3276312, 153.0733614 -27.3292706, 153.0742626 -27.3275168, 153.0760651 -27.3275931, 153.0760222 -27.325458, 153.074091 -27.3233611, 153.0713873 -27.3229035, 153.0707007 -27.3232848, 153.0695849 -27.3231323))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0695849, -27.3231323], [153.0691557, -27.3252293], [153.0697565, -27.3259918], [153.0710011, -27.3261443], [153.0714302, -27.3276312], [153.0733614, -27.3292706], [153.0742626, -27.3275168], [153.0760651, -27.3275931], [153.0760222, -27.325458], [153.074091, -27.3233611], [153.0713873, -27.3229035], [153.0707007, -27.3232848], [153.0695849, -27.3231323]]]}"^^geo:geoJSONLiteral ;
    ] ;
  dcterms:title "Shorncliffe" ;
  geo:sfWithin :queensland ;
.
:sandgate-golf-club
  a geo:Feature ;
  dcterms:identifier "sandgate-golf-club"^^xsd:token ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (153.0809080031782 -27.32763692549964)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [153.0809080031782, -27.32763692549964]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0733614 -27.3218518, 153.0882841 -27.3218518, 153.0882841 -27.3348907, 153.0733614 -27.3348907, 153.0733614 -27.3218518))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0733614, -27.3218518], [153.0882841, -27.3218518], [153.0882841, -27.3348907], [153.0733614, -27.3348907], [153.0733614, -27.3218518]]]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((153.0733614 -27.3292706, 153.0755382 -27.3303539, 153.0785423 -27.3324889, 153.0788856 -27.334052, 153.0798298 -27.3348907, 153.0814177 -27.3342426, 153.0823618 -27.3308496, 153.0858808 -27.3296296, 153.0882841 -27.3287527, 153.0862242 -27.3245969, 153.0830055 -27.3220043, 153.0809885 -27.3221568, 153.0780273 -27.3218518, 153.0772119 -27.3261982, 153.0760222 -27.325458, 153.0760651 -27.3275931, 153.0742626 -27.3275168, 153.0733614 -27.3292706))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[153.0733614, -27.3292706], [153.0755382, -27.3303539], [153.0785423, -27.3324889], [153.0788856, -27.334052], [153.0798298, -27.3348907], [153.0814177, -27.3342426], [153.0823618, -27.3308496], [153.0858808, -27.3296296], [153.0882841, -27.3287527], [153.0862242, -27.3245969], [153.0830055, -27.3220043], [153.0809885, -27.3221568], [153.0780273, -27.3218518], [153.0772119, -27.3261982], [153.0760222, -27.325458], [153.0760651, -27.3275931], [153.0742626, -27.3275168], [153.0733614, -27.3292706]]]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Sandgate Golf Club" ;
  geo:sfWithin :queensland ;
.

:queensland
  a geo:Feature ;
  dcterms:identifier "queensland"^^xsd:token ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (144.5976135065624 -22.59841000065646)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [144.5976135065624, -22.59841000065646]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((137.8562434 -10.7826691, 153.7205012 -10.7826691, 153.7205012 -29.1455185, 137.8562434 -29.1455185, 137.8562434 -10.7826691))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[137.8562434, -10.7826691], [153.7205012, -10.7826691], [153.7205012, -29.1455185], [137.8562434, -29.1455185], [137.8562434, -10.7826691]]]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((142.3826106 -10.7826691, 141.591595 -12.4184198, 140.9763606 -17.2174931, 140.2292903 -17.7205136, 138.07597 -16.4604006, 137.8562434 -25.9512058, 140.9324153 -25.911685, 141.0068201 -28.9911208, 148.9744075 -28.9149736, 150.2048762 -28.4523459, 151.2595637 -29.1455185, 152.5339778 -28.2976838, 153.7205012 -28.4909761, 153.2371028 -25.7930431, 148.8425715 -20.3786955, 146.3376887 -18.8471123, 144.6677668 -14.3847506, 143.9646418 -14.6400094, 142.3826106 -10.7826691))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[142.3826106, -10.7826691], [141.591595, -12.4184198], [140.9763606, -17.2174931], [140.2292903, -17.7205136], [138.07597, -16.4604006], [137.8562434, -25.9512058], [140.9324153, -25.911685], [141.0068201, -28.9911208], [148.9744075, -28.9149736], [150.2048762, -28.4523459], [151.2595637, -29.1455185], [152.5339778, -28.2976838], [153.7205012, -28.4909761], [153.2371028, -25.7930431], [148.8425715, -20.3786955], [146.3376887, -18.8471123], [144.6677668, -14.3847506], [143.9646418, -14.6400094], [142.3826106, -10.7826691]]]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Queensland" ;
  dcterms:description "Queensland is a state of Australia and, in this dataset, contains both Features within the FeatureCollection it is in ('polys') and also Features within another FeatureCollection instance ('points') which is still within this demonstration dataset." ;
  geo:sfContains 
    :camerons-corner ,
    :shorncliffe-point-1 ,
    :shorncliffe-point-2 ,
    :shorncliffe-point-3 ,
    :wyvenhoe ,
    :curlew-park ,
    :shorncliffe ,
    :sandgate-golf-club ;
  geo:sfWithin :australia ;
.

:australia
  a geo:Feature ;
  dcterms:identifier "australia"^^xsd:token ;
  geo:hasCentroid [
    a geo:Geometry ;
    geo:asWKT "POINT (134.4352268190664 -25.52803598002069)"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Point\", \"coordinates\": [134.4352268190664, -25.52803598002069]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasBoundingBox [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((113.3787043 -10.7826691, 153.7205012 -10.7826691, 153.7205012 -38.8851125, 113.3787043 -38.8851125, 113.3787043 -10.7826691))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[113.3787043, -10.7826691], [153.7205012, -10.7826691], [153.7205012, -38.8851125], [113.3787043, -38.8851125], [113.3787043, -10.7826691]]]}"^^geo:geoJSONLiteral ;
  ] ;
  geo:hasGeometry [
    a geo:Geometry ;
    geo:asWKT "POLYGON ((121.3328059 -19.4283415, 116.5867122 -20.7490013, 114.3015559 -22.0582289, 113.4226497 -24.0395178, 114.2576106 -25.9907133, 113.3787043 -26.4244169, 114.9167903 -29.0687274, 114.9607356 -30.1765468, 115.6638606 -31.3846645, 115.6638606 -33.4617628, 115.0046809 -33.7180133, 115.1804622 -34.373435, 117.4656184 -35.0957111, 119.8386653 -34.082762, 123.4861262 -33.8641, 125.1999934 -32.6144637, 129.3747981 -31.6094885, 133.4617122 -31.9829906, 135.7908137 -34.9157343, 137.944134 -32.9101001, 139.5261653 -37.0140251, 140.4929622 -38.0594038, 143.6130793 -38.8166649, 144.8874934 -38.0247943, 146.2497981 -38.8851125, 147.5242122 -37.9901685, 149.9412043 -37.5733844, 151.1277278 -34.0099372, 152.5339778 -32.466278, 153.7205012 -28.4909761, 153.2371028 -25.7930431, 148.8425715 -20.3786955, 146.3376887 -18.8471123, 144.6677668 -14.3847506, 143.9646418 -14.6400094, 142.3826106 -10.7826691, 141.591595 -12.4184198, 140.9763606 -17.2174931, 140.2292903 -17.7205136, 135.5271418 -14.7675278, 136.8015559 -12.2037461, 132.6706965 -11.386423, 130.6492122 -11.386423, 129.6824153 -15.0223398, 126.7820247 -13.8306945, 123.5300715 -17.1755123, 123.0466731 -16.3339267, 121.3328059 -19.4283415))"^^geo:wktLiteral ;
    geo:asGeoJSON "{\"type\": \"Polygon\", \"coordinates\": [[[121.3328059, -19.4283415], [116.5867122, -20.7490013], [114.3015559, -22.0582289], [113.4226497, -24.0395178], [114.2576106, -25.9907133], [113.3787043, -26.4244169], [114.9167903, -29.0687274], [114.9607356, -30.1765468], [115.6638606, -31.3846645], [115.6638606, -33.4617628], [115.0046809, -33.7180133], [115.1804622, -34.373435], [117.4656184, -35.0957111], [119.8386653, -34.082762], [123.4861262, -33.8641], [125.1999934, -32.6144637], [129.3747981, -31.6094885], [133.4617122, -31.9829906], [135.7908137, -34.9157343], [137.944134, -32.9101001], [139.5261653, -37.0140251], [140.4929622, -38.0594038], [143.6130793, -38.8166649], [144.8874934, -38.0247943], [146.2497981, -38.8851125], [147.5242122, -37.9901685], [149.9412043, -37.5733844], [151.1277278, -34.0099372], [152.5339778, -32.466278], [153.7205012, -28.4909761], [153.2371028, -25.7930431], [148.8425715, -20.3786955], [146.3376887, -18.8471123], [144.6677668, -14.3847506], [143.9646418, -14.6400094], [142.3826106, -10.7826691], [141.591595, -12.4184198], [140.9763606, -17.2174931], [140.2292903, -17.7205136], [135.5271418, -14.7675278], [136.8015559, -12.2037461], [132.6706965, -11.386423], [130.6492122, -11.386423], [129.6824153, -15.0223398], [126.7820247, -13.8306945], [123.5300715, -17.1755123], [123.0466731, -16.3339267], [121.3328059, -19.4283415]]]}"^^geo:geoJSONLiteral ;
  ] ;
  dcterms:title "Australia" ;
  dcterms:comment "'Australia' here is a rough outline (boundary) for the country. It contains Queensland and thus, transitively, contains all the Features that Queensland contains." ;
  geo:sfContains 
    :queensland ;
.

```

#### geojson
```geojson
{
	"type": "FeatureCollection",
	"name": "moreton-island",
	"crs": {
		"type": "name",
		"properties": {
			"name": "urn:ogc:def:crs:OGC:1.3:CRS84"
		}
	},
	"features": [{
		"type": "Feature",
		"properties": {
			"Name": "Moreton Island"
		},
		"geometry": {
			"type": "Polygon",
			"coordinates": [
				[
					[153.4688146, -27.0291517],
					[153.455768299999988, -27.0242584],
					[153.4337956, -27.0346564],
					[153.4090764, -27.0346564],
					[153.3781774, -27.046888],
					[153.3610112, -27.0621757],
					[153.3685643, -27.0792955],
					[153.3713109, -27.1019141],
					[153.3630712, -27.1367499],
					[153.3733708, -27.1764617],
					[153.3658177, -27.1990606],
					[153.3754308, -27.2198231],
					[153.37749070000001, -27.2350872],
					[153.4042699, -27.2906308],
					[153.405643199999986, -27.2979531],
					[153.4207494, -27.3284578],
					[153.421436, -27.3406573],
					[153.418002800000011, -27.354685],
					[153.426929199999989, -27.3607835],
					[153.4434087, -27.3315078],
					[153.429675800000012, -27.3174771],
					[153.4166295, -27.2613365],
					[153.418002800000011, -27.2106637],
					[153.4310491, -27.1373609],
					[153.4688146, -27.0291517]
				]
			]
		}
	}]
}
```

#### kml
```kml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <Placemark>
      <name>Moreton Island</name>
      <Polygon>
        <outerBoundaryIs>
          <LinearRing>
            <tessellate>1</tessellate>
            <coordinates>
              153.4688146,-27.0291517,0
              153.4557683,-27.0242584,0
              153.4337956,-27.0346564,0
              153.4090764,-27.0346564,0
              153.3781774,-27.046888,0
              153.3610112,-27.0621757,0
              153.3685643,-27.0792955,0
              153.3713109,-27.1019141,0
              153.3630712,-27.1367499,0
              153.3733708,-27.1764617,0
              153.3658177,-27.1990606,0
              153.3754308,-27.2198231,0
              153.3774907,-27.2350872,0
              153.4042699,-27.2906308,0
              153.4056432,-27.2979531,0
              153.4207494,-27.3284578,0
              153.421436,-27.3406573,0
              153.4180028,-27.354685,0
              153.4269292,-27.3607835,0
              153.4434087,-27.3315078,0
              153.4296758,-27.3174771,0
              153.4166295,-27.2613365,0
              153.4180028,-27.2106637,0
              153.4310491,-27.1373609,0
              153.4688146,-27.0291517,0
            </coordinates>
          </LinearRing>
        </outerBoundaryIs>
      </Polygon>
    </Placemark>
  </Document>
</kml>
```

#### gml
```gml
<?xml version="1.0" encoding="utf-8" ?>
<ogr:FeatureCollection
     gml:id="aFeatureCollection"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://ogr.maptools.org/ moreton-island.xsd"
     xmlns:ogr="http://ogr.maptools.org/"
     xmlns:gml="http://www.opengis.net/gml/3.2">
                                                                                                                                      
  <ogr:featureMember>
    <ogr:moreton_island gml:id="moreton_island.0">
      <ogr:geometryProperty>
        <gml:Polygon srsName="urn:ogc:def:crs:EPSG::4326" gml:id="moreton_island.geom.0">
          <gml:exterior>
            <gml:LinearRing>
              <gml:posList>
                -27.0291517 153.4688146 -27.0242584 153.4557683 -27.0346564 153.4337956 -27.0346564 153.4090764 -27.046888 153.3781774 -27.0621757 153.3610112 -27.0792955 153.3685643 -27.1019141 153.3713109 -27.1367499 153.3630712 -27.1764617 153.3733708 -27.1990606 153.3658177 -27.2198231 153.3754308 -27.2350872 153.3774907 -27.2906308 153.4042699 -27.2979531 153.4056432 -27.3284578 153.4207494 -27.3406573 153.421436 -27.354685 153.4180028 -27.3607835 153.4269292 -27.3315078 153.4434087 -27.3174771 153.4296758 -27.2613365 153.4166295 -27.2106637 153.4180028 -27.1373609 153.4310491 -27.0291517 153.4688146
              </gml:posList>
            </gml:LinearRing>
          </gml:exterior>
        </gml:Polygon>
      </ogr:geometryProperty>
      <ogr:geometryProperty>
        <gml:Polygon srsName="urn:ogc:def:crs:EPSG:6.9:3857" gml:id="moreton_island.geom.1">
          <gml:exterior>
            <gml:LinearRing>
              <gml:posList>
                12902794.504700001 -3757970.5163999982 12902886.478399999 -3757877.9356999993 12902680.1307 -3757668.7490000017 12902665.726799998 -3757654.1464999989 12902657.5436 -3757662.6539999992 12902619.630199999 -3757700.3423999995 12902607.136100002 -3757687.6403999999 12902569.230799999 -3757725.3311999999 12902563.392099999 -3757739.1667999998 12902690.743700001 -3757865.7820999995 12902794.504700001 -3757970.5163999982
              </gml:posList>
            </gml:LinearRing>
          </gml:exterior>
        </gml:Polygon>
      </ogr:geometryProperty>      
      <ogr:Name>Moreton Island</ogr:Name>
    </ogr:moreton_island>
  </ogr:featureMember>
</ogr:FeatureCollection>
```

#### wkt
```wkt
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <Placemark>
      <name>Moreton Island</name>
      <Polygon>
        <outerBoundaryIs>
          <LinearRing>
            <tessellate>1</tessellate>
            <coordinates>
              153.4688146,-27.0291517,0
              153.4557683,-27.0242584,0
              153.4337956,-27.0346564,0
              153.4090764,-27.0346564,0
              153.3781774,-27.046888,0
              153.3610112,-27.0621757,0
              153.3685643,-27.0792955,0
              153.3713109,-27.1019141,0
              153.3630712,-27.1367499,0
              153.3733708,-27.1764617,0
              153.3658177,-27.1990606,0
              153.3754308,-27.2198231,0
              153.3774907,-27.2350872,0
              153.4042699,-27.2906308,0
              153.4056432,-27.2979531,0
              153.4207494,-27.3284578,0
              153.421436,-27.3406573,0
              153.4180028,-27.354685,0
              153.4269292,-27.3607835,0
              153.4434087,-27.3315078,0
              153.4296758,-27.3174771,0
              153.4166295,-27.2613365,0
              153.4180028,-27.2106637,0
              153.4310491,-27.1373609,0
              153.4688146,-27.0291517,0
            </coordinates>
          </LinearRing>
        </outerBoundaryIs>
      </Polygon>
    </Placemark>
  </Document>
</kml>
```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary`

