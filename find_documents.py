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

# 5 - Utilizando o operador In - Inside
# O operador In é utilizado para filtrar documentos que possuem um campo com um valor que está dentro de uma lista de valores

filter_in = db.laureates.count_documents({
    "diedCountry": {"$in": ["France", "USA"]}
})

print(filter_in)

# 6 - Utilizando o operado Ne - Not Equal
# O operador Ne é utilizado para filtrar documentos que possuem um campo com um valor diferente de um determinado valor

filter_ne = db.laureates.count_documents({
    "diedCountry": {"$ne": "USA"}
})

print(filter_ne)
