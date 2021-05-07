from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import sys

g = Graph().parse(data=sys.argv[1], format='turtle')

context = {"@vocab": "http://purl.org/dc/terms/", "@language": "en"}
jsonld=g.serialize(format='json-ld', context=context, indent=4)
 
f = open(sys.argv[2], "w")
f.write(jsonld)
f.close()
