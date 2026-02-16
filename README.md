# OGC GeoSPARQL

## 1.1 - published in 2024 at http://www.opengis.net/doc/IS/geosparql/1.1 

This branch of the [GeoSPARQL version control repository](https://github.com/opengeospatial/ogc-geosparql/) contains source files for the 1.1 specification document and a few supporting resources.

This repository is managed by the _GeoSPARQL Standards Working Group_, the Charter for which can be viewed here:

* [GeoSPARQL SWG Charter](https://rawcdn.githack.com/opengeospatial/ogc-geosparql/f51bfe0643bb4010ba8a2ee2ae79e8335a55558c/charter/swg_charter.html)

## Resources

This branch of this repository does not contain the GeoSPARQL 1.1 RDF resource files which are now fixed - not to be changed in normative ways. They are maintained by the Geosemantics DWG in the [Geosemantics DWG-maintained GeoSPARQL SWG Resources repository](https://github.com/opengeospatial/geosemantics-semantic-resources/tree/main/resources/geosparql-swg) 

The resources it does contain are:

* `contexts/` - JSON-LD context files for 1.1 ontologies
* `examples/` - extended RDF examples of GeoSPARQL 1.1, including SHACL validator test data
* `rif/` - the RIF-CS resource
* `spec/` - the ASCIIDOC soource files for the specification document
* `translations/` - French and German translations of the RDF files' annotations
* `index.html` & `spec.pdf` - built HTML & PDF versions of the spec
    * using the commands in `spec/HTML_Gen.bat` & `spec/PDF_Gen.bat` respectively
* `citeme.bib` - a BibTex file containin .1's citation, as below
* `LICENSE` - the OGC Document License Agreement which applies to all this content.

## Current GeoSPARQL development

For current development of GeoSPARQL, please see the main branch in this repository:

* <https://github.com/opengeospatial/ogc-geosparql>

## Citation

To cit GeoSPARQL 1.1, please use this BibText:

```bibtex
@techreport{nicholas_j_car_ogc_2023,
	type = {{OGC} {Implementation} {Standard}},
	title = {{OGC} {GeoSPARQL} - {A} {Geographic} {Query} {Language} for {RDF} {Data}},
	url = {http://www.opengis.net/doc/IS/geosparql/1.1},
	number = {OGC 22-047r1},
	institution = {Open Geospatial Consortium},
	author = {{Nicholas J. Car} and {Timo Homburg} and {Matthew Perry} and {John Herring} and {Frans Knibbe} and {Simon J.D. Cox} and {Joseph Abhayaratna} and {Mathias Bonduel}},
	collaborator = {Paul J. Cripps and {Krzysztof Janowicz}},
	year = {2024},
  version = {1.1},
}
```

See the above in the `citeme.bib` file too.

## Update of GeoSPARQL 1.0 to 1.1

### Rationale

GeoSPARQL 1.0 was published in 2012. Since then the standard has seen considerable uptake. With that came requests for extension and improvement. This has led to the revival of the OGC GeoSPARQL Standards Working Group (SWG). The overall mission of the GeoSPARQL SWG is to ensure that the features of GeoSPARQL remain up-to-date with expectations from the Semantic Web community. For more details, see the [SWG's charter](https://portal.ogc.org/files/93345) (also linked to above) and the recently published OGC whitepaper [Benefits of Representing Spatial Data Using Semantic and Graph Technologies](http://docs.ogc.org/wp/19-078r1/19-078r1.html).

## Contact

To contact the SWG directly, you may email the closed SWG mailing list (<geosparql.swg@lists.opengeospatial.org>) or email SWG chairs directly:

* Joseph Abhayaratna - <joseph.abhayaratna@geoscape.com.au>
* Linda van den Brink - <l.vandenbrink@geonovum.nl>
* Dimitris Kotzinos - <kotzino@gmail.com>
