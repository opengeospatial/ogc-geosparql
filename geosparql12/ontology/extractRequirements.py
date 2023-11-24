from rdflib import Graph

versionprefix=""
reqexportdir="../requirements/"
conformanceclassexportdir="../abstract_tests/"


g=Graph()
g.parse("requirements/reqs.ttl")

def requirementToAdoc(tup,filename):
    f=open(reqexportdir+filename+".adoc","w")
    f.close()

for subj in g.subjects():
    if versionprefix in str(subj):
        for tup in g.predicate_objects(subj):
            if str(tup[0])=="http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
                
            
