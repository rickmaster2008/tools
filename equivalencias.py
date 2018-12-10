import json

marcas = ["purolator", "lys", "sakura", "nissan", "fleetguard", "volvo", "bosch", "caterpillar", "cummins", "daewoo", "dong feng", "donaldson", "fram", 
         "hengst", "hp", "hino", "hyundai", "luberfinner", "mann"]

f = open("filtros.json")
e = open("equivalencias.json", 'w')

filtros =  json.load(f)

equivalencias = []

i = 0

for filtro in filtros:
    for marca in marcas:
        if filtro[marca] != "":
            equivalencias.append({
                "codigo": str(filtro[marca]),
                "marca": marca,
                "equivalencia": filtro["Codigo"]
            })

json.dump(equivalencias, e)

f.close()
