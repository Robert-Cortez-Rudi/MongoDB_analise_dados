from pymongo import MongoClient
import requests

# 1 - Estabele conexão com o MongoDB e o Database

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 2 - Filtração e contar documentos por genêro 

print(db.laureates.count_documents({"gender": "female"}))
print(db.laureates.count_documents({'gender': 'male'}))

# 3 - Contar documentos pelo pais que faleceu

print(db.laureates.count_documents({"diedCountry": "France"}))

# 4 - Filtro composto com informações

filter_doc = {
    "diedCountry": "France",
    "gender": "female",
    "bornCity": "Warsaw"
}

print(db.laureates.count_documents(filter_doc))
print(db.laureates.find_one(filter_doc))
