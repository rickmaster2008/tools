import json
import progressbar

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceKey.json")

firebase_admin.initialize_app(cred, {
    'storageBucket': 'wbusch-f8fb7.appspot.com'
})

db = firestore.client()

# doc = db.collection('codigos').document('AE184').get()

# f = open("filtros.json")

# filtros = json.load(f)

# for filtro in progressbar.progressbar(filtros):
#     db.collection("codigos").document(filtro["codigo"]).set({
#         "item": filtro["codigo"],
#         "linea": filtro["linea"],
#         "tipo": filtro["tipo"],
#         "altura": filtro["altura"],
#         "Diametro Exterior": filtro["diametro_exterior"],
#         "Diametro Interior": filtro["diametro_interior"],
#         "PZS x Caja": filtro["und_x_caja"],
#         "Valv. Antidr": filtro["valv_antidr"],
#         "Valv. by Pass": filtro["valc_by_pass"],
#         "aplicaciones": filtro["resumen_aplicaciones"],
#         "empaquetadura": filtro["empaquetadura"],
#     })

#segundo

# f = open("aplicaciones.json")
# aplicaciones = json.load(f)

# for aplicacion in progressbar.progressbar(aplicaciones):
#     for k in aplicacion:
#         aplicacion[k] = str(aplicacion[k])
#     db.collection("aplicaciones").add(aplicacion)

#tercero

# f = open("new_marcas.txt")

# marcas = f.readlines()

# marcas = [x.strip() for x in marcas]

# marcas_dict = {}
# for marca in marcas:
#     marcas_dict[marca] = True

# db.collection("listas").document("marcas").set(marcas_dict)

#cuarto

f = open("equivalencias.json")

equivalencias =  json.load(f)

for e in progressbar.progressbar(equivalencias):
    db.collection("equivalencias").add(e)
f.close()