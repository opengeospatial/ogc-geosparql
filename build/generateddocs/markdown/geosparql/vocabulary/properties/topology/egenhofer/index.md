
# GeoSPARQL Topology: Egenhofer Properties (Model)

`ogc.geosparql.vocabulary.properties.topology.egenhofer` *v0.1*

Properties which can be used to describe the topology of geometries using RCC8 relations

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Equals relation example
A feature is related to itself using the geo:ehEquals relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:ehEquals ex:MyPlace .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
```

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features":[
    { "type": "Feature",
      "geometry": { "type": "Polygon",
      "coordinates": [[[-83.2, 34.3], 
                    [-83.0, 34.3], [-83.0, 34.5], 
                    [-83.2, 34.5], [-83.2, 34.3]]]
        },
       "properties":{"rdfs:label":"MyPlace",
                     "geo:coordinateDimension": 2 ,
                     "geo:dimension": 2 ,
                     "geo:isEmpty": false ,
                     "geo:isSimple": true ,
                     "geo:spatialDimension": 2 
                    }
    }
  ]
}
```


### Disjoint relation example
A feature is related to another feature using the geo:ehDisjoint relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

ex:MyPlace
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlaceGeom ;
  geo:ehDisjoint ex:MyPlace2 .

ex:MyPlaceGeom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .


ex:MyPlace2
  a ex:PlaceOfInterest, geo:Feature, geo:SpatialObject ;
  geo:hasGeometry ex:MyPlace2Geom ;
  geo:ehDisjoint ex:MyPlace .

ex:MyPlace2Geom
  a <http://www.opengis.net/ont/sf#Polygon>, geo:Geometry, <http://www.opengis.net/ont/gml#Polygon> ;
  geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.4 34.1, -83.4 34.3, -83.6 34.3, -83.6 34.1))"^^geo:wktLiteral  .
```

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features":[
    { "type": "Feature",
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
    }
  ]
}
```


### Covers/CoveredBy relation example
A feature is related to another feature using the geo:ehCovers relation. The inverse relation geo:ehCoveredBy is placed on the other feature.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace rdf:type geo:Feature  ;
     geo:ehCovers ex:MyPlace2 ;
     geo:hasGeometry ex:MyPlaceGeom .


ex:MyPlaceGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .

ex:MyPlace2 rdf:type geo:Feature ;
     geo:ehCoveredBy ex:MyPlace ;
     geo:hasGeometry ex:MyPlace2Geom .

ex:MyPlace2Geom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.4 34.1, -83.4 34.3, -83.6 34.3, -83.6 34.1))"^^geo:wktLiteral .
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
        }
    ]
}
```


### Contains relation example
A feature is related to another feature using the geo:ehContains relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace rdf:type geo:Feature  ;
     geo:ehContains ex:MyPlace2 ;
     geo:hasGeometry ex:MyPlaceGeom .

ex:MyPlaceGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .

ex:MyPlace2 rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlace2Geom .

ex:MyPlace2Geom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.4 34.1, -83.4 34.3, -83.6 34.3, -83.6 34.1))"^^geo:wktLiteral .
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
        }
    ]
}
```


### Inside relation example
A feature is related to another feature using the geo:ehInside relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace2 rdf:type geo:Feature  ;
     geo:ehInside ex:MyPlace ;
     geo:hasGeometry ex:MyPlaceGeom2 .

ex:MyPlace2Geom rdf:type sf:Point ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Point(-83.4 34.4)"^^geo:wktLiteral .

ex:MyPlace rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlace2Geom .

ex:MyPlaceGeom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
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
        }
    ]
}
```


### Meet relation example
A feature is related to another feature using the geo:ehMeet relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace rdf:type geo:Feature  ;
     geo:ehMeet ex:MyPlace2 ;
     geo:hasGeometry ex:MyPlaceGeom .

ex:MyPlaceGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .

ex:MyPlace2 rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlace2Geom .

ex:MyPlace2Geom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.2 34.3, -83.0 34.3, -83.0 34.5, -83.2 34.5, -83.2 34.3))"^^geo:wktLiteral .
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
        } 
    ]
}
```


### Overlap relation example
A feature is related to another feature using the geo:ehOverlap relation.
#### ttl
```ttl
@prefix ex: <http://example.org/ApplicationSchema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sf: <http://www.opengis.net/ont/sf#> .

ex:MyPlace rdf:type geo:Feature  ;
     geo:ehOverlap ex:MyPlace2 ;
     geo:hasGeometry ex:MyPlaceGeom .

ex:MyPlaceGeom rdf:type sf:Polygon ;
    geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.6 34.1, -83.2 34.1, -83.2 34.5, -83.6 34.5, -83.6 34.1))"^^geo:wktLiteral .

ex:MyPlace2 rdf:type geo:Feature ;
     geo:hasGeometry ex:MyPlace2Geom .

ex:MyPlace2Geom rdf:type sf:Polygon ;
              geo:asWKT "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> Polygon((-83.3 34.0, -83.1 34.0, -83.1 34.2, -83.3 34.2, -83.3 34.0))"^^geo:wktLiteral .
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
        }
    ]
}
```

## Sources

* [Spec section](https://opengeospatial.github.io/ogc-geosparql/geosparql11/document.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/vocabulary/properties/topology/egenhofer`

