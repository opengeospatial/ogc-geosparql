kurra file reformat -f nt -o as-alignments.nt as-alignments.ttl
kurra file reformat -f nt -o bfo-alignments.nt bfo-alignments.ttl
kurra file reformat -f nt -o crmgeo-alignments.nt crmgeo-alignments.ttl
kurra file reformat -f nt -o dcmi-alignments.nt dcmi-alignments.ttl
kurra file reformat -f nt -o geonames-alignments.nt geonames-alignments.ttl
kurra file reformat -f nt -o juso-alignments.nt juso-alignments.ttl
kurra file reformat -f nt -o lgd-alignments.nt lgd-alignments.ttl
kurra file reformat -f nt -o locn-alignments.nt locn-alignments.ttl
kurra file reformat -f nt -o neogeo-alignments.nt neogeo-alignments.ttl
kurra file reformat -f nt -o osiuk-alignments.nt osiuk-alignments.ttl
kurra file reformat -f nt -o osmrdf-alignments.nt osmrdf-alignments.ttl
kurra file reformat -f nt -o provo-alignments.nt provo-alignments.ttl
kurra file reformat -f nt -o routabletiles-alignments.nt routabletiles-alignments.ttl
kurra file reformat -f nt -o schemaorg-alignments.nt schemaorg-alignments.ttl
kurra file reformat -f nt -o sophox-alignments.nt sophox-alignments.ttl
kurra file reformat -f nt -o wgs84geo-alignments.nt wgs84geo-alignments.ttl
kurra file reformat -f nt -o wikidata-alignments.nt wikidata-alignments.ttl
cat *.nt > all.nt
kurra file reformat -o all.ttl all.nt
rm *.nt