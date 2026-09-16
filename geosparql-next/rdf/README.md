# GeoSPARQL Next RDF Resources

This folder contains GeoSPARQL Next's RDF resources while they are in development. Once finalised, they will be 
transferred to the [Geosemantics DWG's core repository](https://github.com/opengeospatial/geosemantics-semantic-resources/) 
for where they will sit alongside GeosPARQL 1.0 and 1.1 RDF resources for long-term maintenance and automated loading 
in to the [OGC definition Service](https://defs.opengis.net).

## Structure

The RDF resources here are structured to work with the [PrezManifest](https://pypi.org/project/prezmanifest/) tool used 
to automate the loading of RDF resources in files in version control into RDF databases.

The key file is `manifest.ttl` that links to and provides metadata for all the resources.