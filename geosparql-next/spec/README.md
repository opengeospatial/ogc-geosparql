# GeoSPARQL Next Specification Document

View this document online at <https://opengeospatial.github.io/ogc-geosparql/geosparql-next/spec.html>.

> [!IMPORTANT]
> This is a work in progress! If you want a stable version of GeoSPARQL, see [GeoSPARQL 1.1](http://www.opengis.net/doc/IS/geosparql/1.1)

## Technical info

The [Metanorma](https://www.metanorma.org) standards document system this GeoSPARQL document. Source files are [ASCIIDOC](https://asciidoc.org/) files here 
ending in `.adoc` and some supporthing HTML and bibliography files.

To build the document from these you will need Metanorma installed, and then you can run this on the command line:

```
metanorma compile --agree-to-terms -t ogc -x html document.adoc
```

Or you can use Docker the Metanorma container image:

```
docker run --rm -v "$PWD:/metanorma" -w /metanorma metanorma/metanorma metanorma compile --agree-to-terms -t ogc -x html document.adoc
```

Either command will produce an HTML output of `document.html` which will be somewhat like the online copy. You can also 
make PDF documents using Metanorma - just see it's documentation.
