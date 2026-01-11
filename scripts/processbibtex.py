import bibtexparser

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
