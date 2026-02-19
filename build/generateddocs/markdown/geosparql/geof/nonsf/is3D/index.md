
# GeoSPARQL is3D Function (Model)

`ogc.geosparql.geof.nonsf.is3D` *v0.1*

The is3D function tests if a given GeoSPARQL goemetry contains a third dimension

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Usage example of is3D
#### ttl
```ttl
PREFIX my: <http://example.org/ApplicationSchema#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

my:is3Dquery skos:definition """
SELECT ?is3D
WHERE {
  my:A geo:hasDefaultGeometry ?geom .
  ?geom geo:asWKT ?wktLiteral .
  BIND (geof:is3D(?wktLiteral) as ?is3D)
}
""" .
```

#### sparql
```sparql
PREFIX my: <http://example.org/ApplicationSchema#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
SELECT ?is3D
WHERE {
  my:A geo:hasDefaultGeometry ?geom .
  ?geom geo:asWKT ?wktLiteral .
  BIND (geof:is3D(?wktLiteral) as ?is3D)
}
```

#### sparqlresult
```sparqlresult
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
 <head>
  <variable name="is3D"/>
 </head>
 <results distinct="false" ordered="true">
  <result>
   <binding name="is3D"><literal datatype="http://www.w3.org/2001/XMLSchema#boolean">true</literal></binding>
  </result>
 </results>
</sparql>
```

## Sources

* [Sample source document](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogc-geosparql](https://github.com/opengeospatial/ogc-geosparql)
* Path: `_sources/geof/nonsf/is3D`

