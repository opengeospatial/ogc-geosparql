from rdflib import Graph
from rdflib.namespace import DCTERMS, PROF

g = Graph().parse("profile.ttl")

q = """
    PREFIX prof: <http://www.w3.org/ns/dx/prof/>
    
    SELECT ?r ?p ?o
    WHERE {
        ?profile prof:hasResource ?r .
        
        ?r ?p ?o .
    }
    ORDER BY ?r ?p
    """

pr = None
title = None
desc = None
formt = None
conforms_to = None
has_role = None
has_artifact = None

ROLES = {
    "http://www.w3.org/ns/dx/prof/role/constraints": "Constraints",
    "http://www.w3.org/ns/dx/prof/role/example": "Example",
    "http://www.w3.org/ns/dx/prof/role/guidance": "Guidance",
    "http://www.w3.org/ns/dx/prof/role/mapping": "Mapping",
    "http://www.w3.org/ns/dx/prof/role/schema": "Schema",
    "http://www.w3.org/ns/dx/prof/role/specification": "Specification",
    "http://www.w3.org/ns/dx/prof/role/validation": "Validation",
    "http://www.w3.org/ns/dx/prof/role/vocabulary": "Vocabulary",
}

for row in g.query(q):
    if row["r"] != pr:
        if title:
            print(f"| {title} | {desc} | {str(formt or '')} | {str(conforms_to or '')} | {ROLES.get(str(has_role) or '')} | {str(has_artifact or '')}")

        title = None
        desc = None
        formt = None
        conforms_to = None
        has_role = None
        has_artifact = None

    if row["p"] == DCTERMS.title:
        title = row["o"]
    if row["p"] == DCTERMS.description:
        desc = row["o"]
    if row["p"] == DCTERMS.format:
        formt = row["o"]
    if row["p"] == DCTERMS.conformsTo:
        conforms_to = row["o"]
    if row["p"] == PROF.hasArtifact:
        has_artifact = row["o"]
    if row["p"] == PROF.hasRole:
        has_role = row["o"]

    pr = row["r"]
