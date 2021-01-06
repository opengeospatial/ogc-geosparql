import os
import itertools

functions=["geo:sfEquals","geo:sfDisjoint","geo:sfIntersects","geo:sfTouches","geo:sfWithin","geo:sfContains","geo:sfOverlaps","geo:sfCrosses","geo:ehEquals","geo:ehDisjoint","geo:ehMeet","geo:ehOverlap","geo:ehCovers","geo:ehCoveredBy","geo:ehInside","geo:ehContains","geo:rcc8eq","geo:rcc8dc","geo:rcc8ec","geo:rcc8po","geo:rcc8tppi","geo:rcc8tpp","geo:rcc8ntpp","geo:rcc8ntppi"]
literals=["geo:wktLiteral","geo:gmlLiteral","geo:kmlLiteral","geo:geoJSONLiteral"]
properties=["geo:asWKT","geo:asGML","geo:asKML","geo:asGeoJSON"]

combinations=list(itertools.combinations(properties,2))
combinations+=list(map(lambda x, y:(x,y), properties, properties)) 

print(combinations)

f = open("rules.rifps","w")
f.write("Document("+"\n")
f.write("\tPrefix(geo <http://www.opengis.net/ont/geosparql#>)"+"\n")
f.write("\tPrefix(geof <http://www.opengis.net/def/function/geosparql/>)"+"\n")
f.write("\tGroup ("+"\n")
for func in functions:
	for comb in combinations:
		f.write("\t\t\t# "+func+"\n")
		f.write("\t\t\tForall ?f1 ?f2 ?g1 ?g2 ?g1Serial ?g2Serial ("+"\n")
		f.write("\t\t\t\t?f1["+func+"->?f2] :-"+"\n")
		f.write("\t\t\t\tOr ("+"\n")
		f.write("\t\t\t\t\t# feature - feature rule"+"\n")
		f.write("\t\t\t\t\tAnd ("+"\n")		
		f.write("\t\t\t\t\t\t?f1[geo:hasDefaultGeometry->?g1]"+"\n")
		f.write("\t\t\t\t\t\t?f2[geo:hasDefaultGeometry->?g2]"+"\n")   
		f.write("\t\t\t\t\t\t?g1["+comb[0]+"->?g1Serial]"+"\n")
		f.write("\t\t\t\t\t\t?g2["+comb[1]+"->?g2Serial]"+"\n")   		
		f.write("\t\t\t\t\t\tExternal("+func+" (?g1Serial,?g2Serial))"+"\n")   
		f.write("\t\t\t\t\t)"+"\n")
		f.write("\t\t\t\t\t# feature - geometry rule"+"\n")
		f.write("\t\t\t\t\tAnd ("+"\n")		
		f.write("\t\t\t\t\t\t?f1[geo:hasDefaultGeometry->?g1]"+"\n")   
		f.write("\t\t\t\t\t\t?g1["+comb[0]+"->?g1Serial]"+"\n")
		f.write("\t\t\t\t\t\t?f2["+comb[1]+"->?g2Serial]"+"\n")   		
		f.write("\t\t\t\t\t\tExternal("+func+" (?g1Serial,?g2Serial))"+"\n")   
		f.write("\t\t\t\t\t)"+"\n")  
		f.write("\t\t\t\t\t# geometry - feature rule"+"\n")
		f.write("\t\t\t\t\tAnd ("+"\n")		
		f.write("\t\t\t\t\t\t?f2[geo:hasDefaultGeometry->?g2]"+"\n")   
		f.write("\t\t\t\t\t\t?f1["+comb[0]+"->?g1Serial]"+"\n")
		f.write("\t\t\t\t\t\t?g2["+comb[1]+"->?g2Serial]"+"\n")   		
		f.write("\t\t\t\t\t\tExternal("+func+" (?g1Serial,?g2Serial))"+"\n")   
		f.write("\t\t\t\t\t)"+"\n") 
		f.write("\t\t\t\t\t# geometry - geometry rule"+"\n")
		f.write("\t\t\t\t\tAnd ("+"\n")		
		f.write("\t\t\t\t\t\t?f1["+comb[0]+"->?g1Serial]"+"\n")
		f.write("\t\t\t\t\t\t?f2["+comb[1]+"->?g2Serial]"+"\n")   		
		f.write("\t\t\t\t\t\tExternal("+func+" (?g1Serial,?g2Serial))"+"\n")   
		f.write("\t\t\t\t\t)"+"\n")
		f.write("\t\t\t\t)"+"\n")  
		f.write("\t\t\t)"+"\n")  
f.write("\t\t)"+"\n")
f.write(")"+"\n") 
f.close()