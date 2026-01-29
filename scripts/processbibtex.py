import bibtexparser
import re
import os

onlycited=False

citedlabels=set()
directory = os.fsencode("spec/sections/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".adoc") and filename!="05-references.adoc" and filename!="az-bibliography.adoc": 
        with open("spec/sections/"+str(filename)) as f:
            content=f.read()
            matches=re.findall("<<([A-Za-z0-9\\-]+)>>",content)
            print("MATCHES: "+str(matches))
            for mat in matches:
                citedlabels.add(mat)
        continue
    else:
        continue

print(citedlabels)

notcited=set()

with open("spec/bibliography.bib", 'r') as file:
    bibcontent = file.read()
bibtexlib=bibtexparser.parse_string(bibcontent)
if len(bibtexlib.failed_blocks) > 0:
    print(str(len(bibtexlib.failed_blocks))+" bibtex items could not be parsed!")
    print(bibtexlib.failed_blocks)
bibstring=""
bibstringnormative=""
for entry in bibtexlib.entries:
    founddoi=False
    thedoi=None
    normative=False
    print("KEY: "+str(entry.key))
    cited=False
    if str(entry.key) in citedlabels:
        cited=True
    else:
        cited=False
        notcited.add(entry.key)
    if not onlycited or (onlycited and cited):
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
if len(notcited)>0:
    print("The following bibitems were not cited: "+str(notcited))
with open("spec/sections/05-references.adoc","a") as bibdoc:
    bibdoc.write(bibstringnormative)
with open("spec/sections/az-bibliography.adoc","a") as bibdoc:
    bibdoc.write(bibstring)
