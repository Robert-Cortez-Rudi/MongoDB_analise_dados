from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# Forma ERRADA
print(db.laureates.count_documents({
    "prizes": {
        "category": "physics",
        "share": "1"
    }
}))

# Forma CORRETA
# 1 - Todos os laureados que possuem prêmio em Física e compartilhado

print(db.laureates.count_documents({
    "prizes": {
        "$elemMatch": {
            "category": "physics",
            "share": "1"
        }
    }
}))
# O $elemMatch permite que a pesquisa seja feita em um array de objetos

# 2 - Todos os laureados que possuem prêmio em Física e compartilhado antes de 1945

print(db.laureates.count_documents({
    "prizes": {
        "$elemMatch": {
            "category": "physics",
            "share": "1",
            "year": {"$lt": "1945"}
        }
    }
}))

# O $lt é um operador de comparação que significa "menor que"
# O $gt é um operador de comparação que significa "maior que"

