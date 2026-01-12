import bibtexparser
import re
import os

citedlabels=[]
directory = os.fsencode("spec/sections/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".adoc") and filename!="05-references.adoc" and filename!="az-bibliography.adoc": 
        with open("spec/sections/"+str(filename)) as f:
            content=f.read()
            matches=re.findall("<<(.+)>>",content)
            print("MATCHES: "+str(matches))
            citedlabels+=matches
        continue
    else:
        continue

citedlabels.sort()
print(citedlabels)

with open("spec/bibliography.bib", 'r') as file:
    bibcontent = file.read()
bibtexlib=bibtexparser.parse_string(bibcontent)
bibstring=""
bibstringnormative=""
for entry in bibtexlib.entries:
    founddoi=False
    thedoi=None
    normative=False
    for field in entry.fields:
        if field.key=="doi" or field.key=="DOI":
            thedoi=field.value
            founddoi=True
        if field.key=="category" and field.value=="normative":
            normative=True
    if normative:
        if founddoi:
            bibstringnormative+="* [[["+entry.key+",local-file("+entry.key+")]]]\n\n"
        else:
            bibstringnormative+="* [[["+entry.key+", local-file("+entry.key+")]]]\n\n"
    else:
        if founddoi:
            bibstring+="* [[["+entry.key+", local-file("+entry.key+")]]]\n\n"
        else:
            bibstring+="* [[["+entry.key+", local-file("+entry.key+")]]]\n\n"
with open("spec/sections/05-references.adoc","a") as bibdoc:
    bibdoc.write(bibstringnormative)
with open("spec/sections/az-bibliography.adoc","a") as bibdoc:
    bibdoc.write(bibstring)