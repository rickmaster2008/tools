import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceKey.json")

firebase_admin.initialize_app(cred, {
    'storageBucket': 'wbusch-f8fb7.appspot.com'
})

db = firestore.client()

f = open("modelos.json")
m = open("new_marcas.txt")

marcas = m.readlines()

marcas = [x.strip() for x in marcas]

modelos = json.load(f)

i = 0

for marca in marcas:
    db.collection("listas").document(marca).set(modelos[marca])
    i = i + 1
    print(i)
# f = open("aplicaciones.json")
# m = open("modelos.json", "w")

# aplicaciones = json.load(f)

# modelos = {}

# for a in aplicaciones:
#     if a["marca"] not in modelos:
#         modelos[a["marca"]] = {}
#         modelos[a["marca"]][a["modelo"]] = True
#     elif a["modelo"] not in modelos[a["marca"]]:
#         modelos[a["marca"]][a["modelo"]] = True


# modelos = json.dumps(modelos)
# m.write(modelos)

f.close()
m.close()

