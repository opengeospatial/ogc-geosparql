from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import sys

g = Graph().parse(data=sys.argv[0], format='turtle')

context = {"@vocab": "http://purl.org/dc/terms/", "@language": "en"}
jsonld=g.serialize(format='json-ld', context=context, indent=4)
 
f = open(sys.argv[1], "w")
f.write(jsonld)
f.close()