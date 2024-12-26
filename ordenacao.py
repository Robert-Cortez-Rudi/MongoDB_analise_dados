from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 1 - Ordenação Ascendente - Do menor para o maior

cursor = db.prizes.find(
    {"category": "physics"},
    ["year"],
    sort = [("year", 1)]
)
# Ordena os documentos de forma ascendente. O 1 indica que a ordenação é ascendente.

print([doc["year"] for doc in cursor][:5])

# 2 - Ordenação Descendente - Do maior para o menor

cursor_2 = db.prizes.find(
    {"category": "physics"},
    ["year"],
    sort = [("year", -1)]
)
# Ordena os documentos de forma descendente. O -1 indica que a ordenação é descendente.

print([doc["year"] for doc in cursor_2][:5])

# 3 - Prêmios concedidos entre 1966 até 1970

for doc in db.prizes.find(
    {"year": {"$gt": "1966", "$lt": "1970"}},
    ["category", "year"],
    sort=[("year", 1), ("category", -1)]):
    print("{year} - {category}".format(**doc))
