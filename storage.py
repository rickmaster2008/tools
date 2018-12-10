import os
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceKey.json")

firebase_admin.initialize_app(cred, {
    'storageBucket': 'wbusch-f8fb7.appspot.com'
})

bucket = storage.bucket()

filtros = []

def upload_blob(source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(
        source_file_name,
        content_type="image/jpg"
    )

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

    url = blob.public_url
a = 0
with open("filtros.json", "r+") as f:
    filtros = json.load(f)
    for i, filtro in enumerate(filtros):
        try:
            blob = bucket.blob("opt/" + filtro["Title"] + ".jpg")

            blob.upload_from_filename(
                "optimized/" + filtro["Title"] + ".jpg",
                content_type="image/jpg"
            )
            url = blob.public_url
            filtros[i]["imagen"] = url
            a = a+1
            print(a)
        except:
            pass
    # filtros = json.dump(filtros)
    # f.write(filtros)
    # f.close()

# for fn in os:
    # upload_blob("img/" + fn, "img/" + fn)