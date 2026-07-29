---
layout: null
---
[
{%- for pag in site.pages -%}
{%- if pag.slug contains "geosparql" -%}
"{{pag.slug}}",
{%- endif -%}
{%- endfor -%}
]
