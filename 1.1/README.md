# OGC GeoSPARQL 1.1

This folder contains the working copy of OGC's GeoSPARQL standard, expected to be published as GeoSPARQL 1.1. The standard is presented as a number of different resources that are linked to the conceptual stnadard via the profile declaration.

* **Profile Declaration**
    * a desription of the various parts of GeoSPARQL 1.1, according to the [W3C's Profiles Vocabulary](https://w3c.github.io/dx-prof/prof/)
    * [profile.ttl](profile.ttl) - RDF file of the profile declaration, in turtle format
    * [https://raw.githack.com/opengeospatial/ogc-geosparql/master/1.1/profile.html](profile.html) - HTML file of the profile declaration, rendered for viewing

* **Specification**
    * [spec/](spec/) - folder containing ASCII Doc source files. images and build scripts
    * [_11-052r4.html](_11-052r4.html) - specification document in HTML
    * [_11-052r4.pdf](_11-052r4.pdf) - specification document as a PDF
    * *files starting 00- to 18-* - the ASCII Doc master source files to build the specification documents
    * HTML_Gen.bat & PDF_Gen.bat - script files to generate HTML & PDF spc docs from ASCIIDoc source files

* **Ontology**
    * the machine-readable data model of GeoSPARQL 1.1
    * [RDF file](geo.ttl) - in turtle format

* **Validation**
    * a [SHACLConstraints Language](https://www.w3.org/TR/shacl/) validation file, to be used to test conformance claims of data to GeoSPARQL 1.1
    * [RDF file](validation.ttl) - in turtle format
