import os
import sys
import re
import json
from rdflib import Graph, URIRef, Literal

logfile=open("logfile.txt","w")

def check_functions_sd_consistency(input1,input2):
    if isinstance(input2,set):
        print("\n==========\nCOMPARISON: "+str(input1)+" vs. Spec Vocab Functions\n==========\n")
        logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. Spec Vocab Functions\n==========\n")
    else:
        print("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
        logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    g1=Graph()
    g1.parse(input1)
    funcs1={}
    funcs2={}
    for obj in g1.subjects(URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("https://w3id.org/function/ontology#Function")):
        funcs1[str(obj)]=str(obj)[str(obj).rfind("/")+1]
    if not isinstance(input2,set):
        g2=Graph()
        g2.parse(input2)
        for obj in g2.objects(None,URIRef("http://www.w3.org/ns/sparql-service-description#extensionFunction")):
            funcs2[str(obj)]=str(obj)[str(obj).rfind("/")+1]
        comparison(funcs1.keys(),funcs2.keys(),input1,input2)
    else:
        funcs2=input2
        input2="Spec Vocab Functions"
        comparison(funcs1.keys(),funcs2,input1,input2)
    
def comparison(items1,items2,input1,input2):
    diff1=items1-items2
    diff2=items2-items1
    print(str(len(diff1))+" Functions missing in "+str(input2)+" file: ")
    logfile.write("\n"+str(len(diff1))+" Functions missing in "+str(input2)+" file: \n")
    for func in sorted(diff1):
        print("- "+str(func))
        logfile.write("- "+str(func)+"\n")
    print("\n-------\n")
    print(str(len(diff2))+" Functions missing in "+str(input1)+" file: ")
    logfile.write("\n"+str(len(diff2))+" Functions missing in "+str(input1)+" file: \n")
    for func in sorted(diff2):
        print("- "+str(func))
        logfile.write("- "+str(func)+"\n")
    print("\n-------\n")
    
def check_functions_reqs_consistency(input1,input2):
    print("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    g1=Graph()
    g1.parse(input1)
    g2=Graph()
    g2.parse(input2)
    funcs1={}
    funcs2={}
    for obj in g1.objects(None,URIRef("http://www.w3.org/2000/01/rdf-schema#isDefinedBy")):
        funcs1[str(obj)]=str(obj)[str(obj).rfind("/")+1]
    for obj in g2.subjects(URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.opengis.net/def/spec-element/Requirement")):
        funcs2[str(obj)]=str(obj)[str(obj).rfind("/")+1]
    comparison(funcs1.keys(),funcs2.keys(),input1,input2)
    
def check_vocab_jsonld_consistency(input1,input2):
    print("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    f=open(input1)
    jsonld=json.load(f)
    g2=Graph()
    g2.parse(input2)
    contextvals=[]
    for val in jsonld["@context"].values():
        if val!="geo:":
            contextvals.append(val.replace("geo:","http://www.opengis.net/ont/geosparql#"))
    funcs2={}
    for obj in g2.subjects():
        if isinstance(obj,URIRef) and "http://www.opengis.net/ont/geosparql#" in str(obj):
            if not str(obj).endswith("/"):
                funcs2[str(obj)]=str(obj)[str(obj).rfind("/")+1]
    comparison(contextvals,funcs2.keys(),input1,input2)

def check_translation_consistency(translationfolder,vocabfolder):
    nametoGraph={}
    for file in os.listdir(vocabfolder):
        g=Graph()
        g.parse(vocabfolder+"/"+file)
        funcs1=set()
        for obj in g.subjects():
            funcs1.add(str(obj))
        nametoGraph[file]=funcs1
    langs=[langfolder[0] for langfolder in os.walk(translationfolder)]
    for lang in langs:
        if lang!="translations/":
            for file in os.listdir(lang):
                if ".ttl" in file:
                    filenamemod=file[0:file.rfind("_")]+".ttl"
                    g=Graph()
                    g.parse(lang+"/"+file)
                    print("\n==========\nCOMPARISON: "+str(file)+" vs. "+str(filenamemod)+"\n==========\n")
                    logfile.write("\n==========\nCOMPARISON: "+str(file)+" vs. "+str(filenamemod)+"\n==========\n")
                    for sub in g.subjects():
                        if str(sub) not in nametoGraph[filenamemod]:
                            if isinstance(sub,URIRef):
                                print("Translation "+str(str(lang)[lang.rfind("/")+1:].upper())+" missing for "+str(sub)+" ["+str(filenamemod)+"]")
                                logfile.write("Translation "+str(str(lang)[lang.rfind("/")+1:].upper())+" missing for "+str(sub)+" ["+str(filenamemod)+"]\n")
            
    
def check_rules_spec_consistency(input1,input2):
    if isinstance(input2,set):
        print("\n==========\nCOMPARISON: "+str(input1)+" vs. Spec Vocab Functions\n==========\n")
        logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. Spec Vocab Functions\n==========\n")
    else:
        print("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
        logfile.write("\n==========\nCOMPARISON: "+str(input1)+" vs. "+str(input2)+"\n==========\n")
    g1=Graph()
    g1.parse(input1)
    funcs1={}
    funcs2={}
    for obj in g1.subjects(URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef("http://www.w3.org/2002/07/owl#Class")):
        funcs1[str(obj)]=str(obj)[str(obj).rfind("/")+1]
    if not isinstance(input2,set):
        g2=Graph()
        g2.parse(input2)
        for obj in g2.objects(None,URIRef("http://www.w3.org/ns/sparql-service-description#extensionFunction")):
            funcs2[str(obj)]=str(obj)[str(obj).rfind("/")+1]
        comparison(funcs1.keys(),funcs2.keys(),input1,input2)
    else:
        funcs2=input2
        input2="Spec Vocab Functions"
        comparison(funcs1.keys(),funcs2,input1,input2)

geopattern="(geo[fr]?:[A-z]+\s)"

def parseSpecForFunctions(directory):
    geopatternset=set()
    geofpatternset=set()
    georpatternset=set()
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".adoc"): 
            print("Process file: "+filename)
            with open(directory+"/"+filename,encoding="utf-8") as f:
                for line in f:
                    matches=re.findall(geopattern, line)
                    if len(matches)>0:
                        for mat in matches:
                            mat=mat.replace("`","").replace("]","").strip()
                            if "geof:" in mat:
                                geofpatternset.add(mat.replace("geof:","http://www.opengis.net/def/function/geosparql/"))
                            elif "geor:" in mat:
                                georpatternset.add(mat.replace("geor:","http://www.opengis.net/def/rule/geosparql/"))                               
                            else:
                                geopatternset.add(mat.replace("geo:","http://www.opengis.net/ont/geosparql#"))
            continue
        else:
            continue

    print("\n==========\nGeo Functions from spec: "+str(len(geofpatternset))+"\n==========\n")
    logfile.write("\n==========\nGeo Functions from spec: "+str(len(geofpatternset))+"\n==========\n")
    for pat in sorted(geofpatternset):
        print("- "+str(pat))
        logfile.write("- "+str(pat)+"\n")
    print("\n==========\nGeo Rules from spec: "+str(len(georpatternset))+"\n==========\n")
    logfile.write("\n==========\nGeo Rules from spec: "+str(len(georpatternset))+"\n==========\n")
    for pat in sorted(georpatternset):
        print("- "+str(pat))
        logfile.write("- "+str(pat)+"\n")
    print("\n==========\nGeo Vocab from spec: "+str(len(geopatternset))+"\n==========\n")
    logfile.write("\n==========\nGeo Vocab from spec: "+str(len(geopatternset))+"\n==========\n")
    for pat in sorted(geopatternset):
        print("- "+str(pat))
        logfile.write("- "+str(pat)+"\n")
    return {"functions":geofpatternset,"vocab":geofpatternset,"rules":georpatternset}
    
    
#input1=sys.argv[1]
#input2=sys.argv[2]
specvocab=parseSpecForFunctions("../spec/")
input1="../vocabularies/functions.ttl"
input2="../servicedescription/servicedescription_all_functions.ttl"
check_functions_sd_consistency(input1,input2)
check_functions_sd_consistency(input1,specvocab["functions"])
input1="../vocabularies/rules.ttl"
check_rules_spec_consistency(input1,specvocab["rules"])
input1="../vocabularies/geo.ttl"
check_vocab_jsonld_consistency("../contexts/geo-context.json",input1)
input2="../vocabularies/requirements.ttl"
check_functions_reqs_consistency(input1,input2)
check_translation_consistency("../translations/","../vocabularies/")
logfile.close()
