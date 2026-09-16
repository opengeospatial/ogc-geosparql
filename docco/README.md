# Auto-built documentation

This folder contains the source files for the auto-build website hosted at <https://opengeospatial.github.io/ogc-geosparql/>. The website depends not only on the files here but also lots of artifacts in the various GeoSPARQL variants' branches which this static site links to.

## Building

This documentation is a static [Jekyll](https://jekyllrb.com/) website, built automatically in the GitHub action `docco` in `.gitbu/workflows/geosparql.yml`.

You can build the documentation site manually using the following commands from within this directory:

`gem install jekyll bundler` to install Jekyll - this depends on you having Ruby installed on your computer

`bundle install` to install all the Jekyll dependencies

Run the dev server to serve the site locally:

`bundle exec jekyll serve`

