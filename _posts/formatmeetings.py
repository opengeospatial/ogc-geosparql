import os

folders=["2021","2020","2022","2023","2024"]

for folder in folders:
    print(folder)
    directory = os.fsencode(folder)
    print(directory)	
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".md"): 
            with open(folder+"/"+filename,encoding="utf-8") as f:
                data = f.read()
        print("GeoSPARQL Standards Working Group Meeting Minutes "+str(filename).replace(".md","").replace("-","/"))
        f = open(folder+"/"+filename, "w",encoding="utf-8")
        #f.write("---\ntitle: GeoSPARQL Standards Working Group Meeting Minutes "+str(filename).replace(".md","").replace("-","/")+"\n---\n")
        f.write(data.replace("\n---","\n---\n"))
        f.close()	
	