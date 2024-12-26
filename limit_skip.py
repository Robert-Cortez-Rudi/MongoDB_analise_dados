from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 1 - Todos os prêmios compartilhados entre 3 pessoas

for doc in db.prizes.find(
    {"laureates.share": "3"}
):
    print("{year} - {category}".format(**doc))

print("\n")

# 2 - Utilizando o limit

for doc in db.prizes.find(
    {"laureates.share": "3"},
limit=5):
    print("{year} - {category}".format(**doc))

print("\n")
# O limit serve para limitar a quantidade de documentos retornados

# 3 - Utilizando o skip

for doc in db.prizes.find(
    {"laureates.share": "3"},
limit=5, skip=5):
    print("{year} - {category}".format(**doc))

print("\n")
# O skip serve para pular uma quantidade de documentos

# 4 - Refatorando / Ordenando Ascendentemente

for doc in db.prizes.find({"laureates.share": "3"}).sort([("year", 1)]).skip(3).limit(5):
    print("{year} - {category}".format(**doc))

