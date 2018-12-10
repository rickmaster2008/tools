import json
import progressbar

f = open("equivalencias.json")
m = open("equis.json", "w")

filtros = json.load(f)

for i in progressbar.progressbar(filtros):
    i["codigo"] = str(i["codigo"])
    i["equivalencia"] = "".join(i["equivalencia"].split("-"))

json.dump(filtros, m)

f.close()
m.close()