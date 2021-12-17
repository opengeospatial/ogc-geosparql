from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import sys

g = Graph().parse(sys.argv[1], format='turtle')

g.serialize(format='json-ld', indent=2, destination=sys.argv[2])
