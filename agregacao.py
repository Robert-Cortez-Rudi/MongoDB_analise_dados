from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

cursor = db.laureates.find(
    filter= {"bornCountry": "USA"},
    projection= {"prizes.year": 1},
    limit=3
)

for doc in cursor:
    print(doc["prizes"])

# 1 - Refatorando consulta com agregações

print("\n\n")

cursor = db.laureates.aggregate([
    {"$match": {"bornCountry": "USA"}}, # O $match serve para filtrar os documentos
    {"$project": {"prizes.year": 1}}, # O $project serve para projetar os campos
    {"$limit": 3} # O $limit serve para limitar o número de documentos
])

for doc in cursor:
    print(doc["prizes"])

# 2 - Adicionando novas etapas na agregação
print("\n")
from collections import OrderedDict # O OrderedDict é uma subclasse de dict que mantém a ordem de inserção dos elementos

print(list(db.laureates.aggregate([
    {"$match": {"bornCountry": "USA"}},
    {"$project": {"prizes.year": 1, "_id": 0}},
    {"$sort": OrderedDict([("prizes.year", 1)])}, # O $sort serve para ordenar os documentos
    {"$limit": 3}
])))

# 3 - Quantos laureados nascidos nos EUA ?

print(list(db.laureates.aggregate([
    {"$match": {"bornCountry": "USA"}},
    {"$count": "qtd_born_usa"} # O $count serve para contar o número de documentos
])))
