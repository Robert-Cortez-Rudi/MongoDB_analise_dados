from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 1 - Valor incluido
# 0 - valor não incluido

docs = db.laureates.find(
    filter = {},
    projection = {
        "prizes.affiliations": 1,
        "_id": 0
    }
)

print(docs)
print(list(docs[:3]))

# 2 - Projeção com campos ausentes

docs_2 = db.laureates.find(
    filter = {"gender": "org"},
    projection = [
        "bornCountry",
        "firstname"
    ]
)

print("\n")
print(list(docs_2[:3]))