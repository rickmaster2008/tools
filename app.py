import urllib.request
import os.path
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
import json

# cred = credentials.Certificate("serviceKey.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# doc_ref = db.collection('listas').document('filtros')

# productos = []
faltan = open("faltan.txt", "w")
with open("codigos.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

    for codigo in content:
        if (os.path.isfile("img/" + codigo + ".jpg")):
            pass
        else:
            try:
                url = "http://filtroswillybusch.com.pe/imgfiltros/" + codigo + ".jpg"
                urllib.request.urlretrieve(url, 'img/' + codigo + '.jpg')
            except:
                faltan.write(codigo + "\n")
                pass
    f.close()
faltan.close()

# with open('filtros.json') as f:
#     data = json.load(f)
#     for item in data:
#         url = "http://filtroswillybusch.com.pe/imgfiltros/" + 
        # for i in range(len(item['Title'])):
        #     if item['Title'][i].isdigit():
        #         item['Title'] = item['Title'][0:i] + '-' + item['Title'][i:]
        #         break
        # file.write(item['Title'] + '\n')
        # print('escrito')
        # productos.append(item['Title'])
# file.close()
# doc_ref.set({
#     'codigos': productos
# })


        