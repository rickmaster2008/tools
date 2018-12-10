import json

f = open("acambiar.json")

filtros = json.load(f)

for filtro in filtros:
    filtro["codigo"] = filtro["codigo"].split("-")
    filtro["codigo"] = "".join(filtro["codigo"])

new_f = open("equivalencias.json", "w")

json.dump(filtros, new_f)

new_f.close()

f.close()
