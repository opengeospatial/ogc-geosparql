from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import sys

g = Graph().parse(sys.argv[1], format='turtle')

g.serialize(format='json-ld', indent=2, destination=sys.argv[2])
g.serialize(format='n3', indent=2, destination=sys.argv[3])
