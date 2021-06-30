# GeoSPARQL 1.1 Extended Examples
This directory contains multiple files of GeoSPARQL 1.1 examples. These are an extension to examples in the [Specification Document's Annex B](https://opengeospatial.github.io/ogc-geosparql/geosparql11/spec.html#_annex_b_informative_geosparql_examples) and are presented separately since some of them are large and not easily incorporated into the Specification's document format.

These examples are:

1. **Multiple Geometry Serializations**
    * A rough boundary for [Moreton Island](https://en.wikipedia.org/wiki/Moreton_Island) is presented in all of the serialization described in GeoSPARQL 1.1 in the following files:
        * [moreton-island.auspix](moreton-island.auspix) - AusPIX DGGS [AUSPIX]
        * [moreton-island.geojson](moreton-island.geojson) - GeoJSON [GEOJSON]
        * [moreton-island.gml](moreton-island.gml) - Geographic Markup Language [OGC07-036]
        * [moreton-island.kml](moreton-island.kml) - Keyhole Markup Language [OGCKML]
        * [moreton-island.wkt](moreton-island.wkt) - Well-Known Text [ISO19125-1]
2. **GeoSPARQL Demonstration Dataset**
    * An example of how to package multiple `Feature` instances in `FeatureCollection` instances within a [DCAT] `dcat:Dataset`.
    * The following single file contains the dataset:
        * [demo-dataset.ttl](demo-dataset.ttl)


## References

* [AUSPIX] Geoscience Australia, _AusPIX: An Australian Government implimentation of the rHEALPix DGGS in Python_ (2020). <https://github.com/GeoscienceAustralia/AusPIX_DGGS>
* [DCAT2] World Wide Web Consortium, _Data Catalog Vocabulary (DCAT) - Version 2_ (2020). W3C Recommendation (04 February 2020). <https://www.w3.org/TR/vocab-dcat/>
* [GEOJSON] Internet Engineering Task Force, _RFC 7946: The GeoJSON Format_. IETF Request for Comment (August 2016). <https://tools.ietf.org/html/rfc7946>
* [OGC07-036] Open Geospatial Consortium, _OGC 07-036: Geography Markup Language (GML) Encoding Standard_, Version 3.2.1 (27 August 2007).
* [OGCKML] Open Geospatial Consortium, _OGC KML 2.3_. OGC Implementation Standard (04 August 2015). <http://www.opengis.net/doc/IS/kml/2.3>
* [ISO19125-1] International Organization for Standardization, _ISO 19125-1: Geographic information — Simple feature access — Part 1: Common architecture_

