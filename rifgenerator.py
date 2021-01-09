import os
import itertools

# all
relations_functions = [
    # Simple Features Topological Relations
    "sfEquals",
    "sfDisjoint",
    "sfIntersects",
    "sfTouches",
    "sfWithin",
    "sfContains",
    "sfOverlaps",
    "sfCrosses",

    # Egenhofer Topological Relations
    "ehEquals",
    "ehDisjoint",
    "ehMeet",
    "ehOverlap",
    "ehCovers",
    "ehCoveredBy",
    "ehInside",
    "ehContains",

    # RCC8 Topological Relations
    "rcc8eq",
    "rcc8dc",
    "rcc8ec",
    "rcc8po",
    "rcc8tppi",
    "rcc8tpp",
    "rcc8ntpp",
    "rcc8ntppi",
]

geom_literals = [
    "gmlLiteral",
    "wktLiteral",
	"geoJSONLiteral",
	"kmlLiteral"
]

template = """   	    # ogc:relation
        Forall ?f1 ?f2 ?g1 ?g2 ?g1Serial ?g2Serial (
            ?f1[ogc:relation->?f2] :-
            Or (
                # feature / feature rule
                And (
                    ?f1[geo:hasDefaultGeometry->?g1]
                    ?f2[geo:hasDefaultGeometry->?g2]
                    ?g1[ogc:asGeomLiteral->?g1Serial]
                    ?g2[ogc:asGeomLiteral->?g2Serial]
                    External(ogc:function (?g1Serial,?g2Serial))
                )
                # feature / geometry rule
                And (
                    ?f1[geo:hasDefaultGeometry->?g1]
                    ?g1[ogc:asGeomLiteral->?g1Serial]
                    ?f2[ogc:asGeomLiteral->?g2Serial]
                    External(ogc:function (?g1Serial,?g2Serial))
                )
                # geometry / feature rule
                And (
                    ?f2[geo:hasDefaultGeometry->?g2]
                    ?f1[ogc:asGeomLiteral->?g1Serial]
                    ?g2[ogc:asGeomLiteral->?g2Serial]
                    External(ogc:function (?g1Serial,?g2Serial))
                )
                # geometry / geometry rule
                And (
                    ?f1[ogc:asGeomLiteral->?g1Serial]
                    ?f2[ogc:asGeomLiteral->?g2Serial]
                    External(ogc:function (?g1Serial,?g2Serial))
                )
            )
        )"""

header = """Document (
    Prefix (geo <http://www.opengis.net/ont/geosparql#>)
    Prefix (geof <http://www.opengis.net/def/function/geosparql/>)

    Group (
"""

footer = """
    )
)
"""
combinations=list(itertools.combinations(geom_literals,2))
combinations+=list(map(lambda x, y:(x,y), geom_literals, geom_literals)) 

print(combinations)

forall_groups = []

for rf in relations_functions:
    for lit in combinations:
        forall_groups.append(
            template
                .replace("ogc:relation", "geo:" + rf)
                .replace("ogc:function", "geof:" + rf)
				.replace("?g1[ogc:asGeomLiteral","?g1[geo:"+lit[0])
				.replace("?f1[ogc:asGeomLiteral","?f1[geo:"+lit[0])
				.replace("?g2[ogc:asGeomLiteral","?g2[geo:"+lit[1])
				.replace("?f2[ogc:asGeomLiteral","?f2[geo:"+lit[1])
        )

with open("rules.rifps", "w") as f2:
    f2.write(header)
    f2.write("\n\n".join(forall_groups))
    f2.write(footer)
