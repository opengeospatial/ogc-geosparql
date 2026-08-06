![](ogc-logo.png)
  
# OGC GeoSPARQL
                          
This GitHub repository contains [OGC](https://www.ogc.org/)'s [GeoSPARQL Standard](https://www.ogc.org/standards/geosparql) and associated resources.
                
This repository is managed by the _GeoSPARQL Standards Working Group_ (SWG) within the OGC's [GeoSemantics Domain Working Group](https://github.com/opengeospatial/geosemantics-dwg), the Charter for which can be viewed here:  
      
* [GeoSPARQL SWG Charter](https://opengeospatial.github.io/ogc-geosparql/charter.html)

## Documentation

To see human-readable documented forms of elements of GeoSPARQL standard variants, please see:
 
* [GeoSPARQL's auto-built documentation](https://opengeospatial.github.io/ogc-geosparql/)      

The source information for this documentation is:

* static content from the `docco/` folder in this repository
* GeoSPARQL Next artifacts from the `geosparql-next` folder in this branch
* GeoSPARQL ISO artifacts from the `geosparql-iso` branch
* GeoSPARQL 1.1 artifacts from the `geosparql-1.1` branch
* GeoSPARQL 1.0 artifacts from the `geosparql-1.0` branch

## Citation

If you want to cite the current OGC standard (1.1) we encourage you to use the following BibTeX statement:  
    
```bibtex
@techreport{ogc_geosparql_11_2024,
	type = {{OGC} {Implementation} {Standard}}, 
	title = {{OGC} {GeoSPARQL} - {A} {Geographic} {Query} {Language} for {RDF} {Data}},
	url = {http://www.opengis.net/doc/IS/geosparql/1.1},
	number = {OGC 22-047},
	institution = {Open Geospatial Consortium},
	author = {{Nicholas J. Car} and {Timo Homburg} and {Matthew Perry} and {John Herring} and {Frans Knibbe} and {Simon J.D. Cox} and {Joseph Abhayaratna} and {Mathias Bonduel}},
	collaborator = {Paul J. Cripps and {Krzysztof Janowicz}},
	year = {2024},
  version = {1.1},
}
```

## GeoSPARQL variants

### GeoSPARQL Next

This is the in-development version of GeoSPARQL, as of July 2026. It is expected to be completed in mid to late 2026 with publication in late 2026 or early 2027. It will be proposed for ISO co-adoption as soon as it is published as an OGC standard.

Source files for this variant are held in the `geosparql-next` folder. 

Current work on GeoSPARQL Next can be tracked by following the [Pull Requests](https://github.com/opengeospatial/ogc-geosparql/pulls) and [Issues](https://github.com/opengeospatial/ogc-geosparql/issues) within this repository as this is where the SWG works. Look for items tagged as "next".

### GeoSPARQL Building Block

An experimental [OGC Building Block](https://ogcincubator.github.io/bblocks-docs/) representation of GeoSPARQL is stored in the `bblocks/` folder. This representation may be delivered within _GeoSPARQL Next_.

### GeoSPARQL ISO

This is the International Standards Organization (ISO) standard ISO 19186-1 which is the ISO's co-adoption of OGC GeoSPARQL 1.1 with only styling, formatting and non-normative referencing and definitions changes to align it with [ISO/TC211](https://www.iso.org/committee/54904.html)'s 19* series of standards.

As of July 2026, this standard is in draft:

* <https://www.iso.org/standard/32591.html>

Source files for this variant are internal to ISO systems and not publicly available. The RDF data use for this variant is the same as that of GeoSPARQL 1.1.

### GeoSPARQL 1.1

This is the current OGC published standard version of GeoSPARQL, online at <http://www.opengis.net/doc/IS/geosparql/1.1>.

If you are looking to use GeoSPARQL, use this version.

Source files, except for RDF files, for this variant are held in the `geosparql-1.1` branch of this repository.

> [!NOTE]
> All the RDF resources for GeoSPARQL 1.1 are not managed here but in the [Geosemantics DWG repository's GeoSPARQL SWG subfolder](https://github.com/opengeospatial/geosemantics-semantic-resources/tree/main/resources/geosparql-swg). This is because they are automatically picked up from there and loaded into the OGC's [Definitions Service](https://defs.opengis.net/).

### GeoSPARQL 1.0

This is the original version of GeoSPARQL published in 2012. A copy of its specification as then published is available from the OGC GeoSPARQL standard listing:

* <https://www.ogc.org/standards/geosparql/>

Source files for this variant are held in the `geosparql-1.0` branch of this repository.

## Other SWG outputs

This SWG has produced resources other than GeoSPARQL standard variants:

### Charter

* [GeoSPARQL SWG Charter](charter/swg_charter.html)

Source files in `charter/` folder.

### Extended Well Known Binary (EWKB) Community Standard

* [Community Standard Work Item Justification](https://opengeospatial.github.io/ogc-geosparql/ewkb/work_item.html)
* [Community Standard](https://opengeospatial.github.io/ogc-geosparql/ewkb/community_standard.html)

Source files for both in `ewkb/` folder.

## Working documents

An index of the working artefacts for the current GeoSPARQL variants can be found here:

* <https://opengeospatial.github.io/ogc-geosparql/>. These are built automatically as updates occur. 

> [!NOTE]
> These are only working documents only and are not approved standards, so they are in flux. To see a stable standard, selecte one of the variants listed above.

Extended GeoSPARQL work can also be found in the following OGC code repositories:

* <https://github.com/opengeospatial/ogc-geosparql-shapes>

## How to get involved

To be involved in the development of GeoSPARQL, [join the OGC](https://www.ogc.org/membership/) and participate in the GeoSPARQL SWG!

Additionally, you may communicate with the SWG and raise bugs/issues/Use Cases in the issue tracker at <https://github.com/opengeospatial/ogc-geosparql/issues>.

If you're already a member of the ISO, you can be involved in the development of ISO versions of GeoSPARQL too through the ISO's [Technical Committee 211 - Geographic information/Geomatics](https://www.iso.org/committee/54904.html). 

## License

OGC documents, such as the [GeoSPARQL 1.1 Standard]() are licensed for use with the [OGC's Document License Agreement for OGC Resources](https://www.ogc.org/about/policies/document-license-agreement/).

Software and data, such as the [GeoSPARQL 1.1 Ontology](http://www.opengis.net/ont/geosparql), are licensed for use with the [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0) as per the OGC's policy on [Licensing for Geospatial Software](https://www.ogc.org/about/policies/software-licenses/). 

## Contact

To contact the SWG directly, please email the chairs:

* Joseph Abhayaratna - <joseph.abhayaratna@geoscape.com.au>
* Matthew Perry - <matthew.perry@oracle.com>

You may also get in touch by posting an Issue in the [Issue Tracker](https://github.com/opengeospatial/ogc-geosparql/issues).
