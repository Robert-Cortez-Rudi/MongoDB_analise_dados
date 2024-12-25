from pymongo import MongoClient

# 1 - Estabele conexão com o MongoDB e o Database

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 2 - Buscando o primeiro documento

walter = db.laureates.find_one({
    "firstname": "Walter",
    "surname": "Kohn"
})

print(walter)

# 3 - Pesquisando em uma subestrutura

california = db.laureates.count_documents({
    "prizes.affiliations.name": "University of California"
})

print(california)

san_francisco = db.laureates.count_documents({
    "prizes.affiliations.city": "San Francisco, CA"
})

print(san_francisco)

# 4 - Conta documentos que não possuem informação
# O $exists verifica se o campo existe ou não no documento

no_country = db.laureates.count_documents({
    "bornCountry": {"$exists": False}
})

print(no_country)
