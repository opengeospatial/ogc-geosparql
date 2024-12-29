---
layout: null
---
[
{%- for pag in site.pages -%}
{%- if "geosparql" in pag.slug -%}
{{pag.slug}}
{%- endif -%}
{%- endfor -%}
]
