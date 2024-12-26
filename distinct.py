from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 1 - Lista o mapeamento de genêros

# Agragação que vai processar os dados em uma coleção 
# Irá produzir o resultado que foi gerado

print(db.laureates.distinct("gender"))
# O distinct é um método que retorna uma lista de valores distintos para a chave especificada em uma coleção

print(db.laureates.count_documents({"gender": "female"}))
print(db.laureates.count_documents({'gender': 'male'}))
print(db.laureates.count_documents({'gender': 'org'}))

# 2 - Lista o mapeamento de categoria dos prêmios

print(db.laureates.distinct("prizes.category"))

# Alguns prêmios foram compartilhados

# 3 - Quais categorias do prêmios, além de física, tem laureados com ações trimestrais ?

print(db.laureates.distinct(
    "prizes.category",
    {"prizes.share" : "4"}
))

print(db.prizes.distinct(
    "category",
    {"laureates.share" : "4"}
))

# 4 - Quais categorias de laureados ganharam mais de um prêmio ?

print(db.laureates.distinct(
    "prizes.category",
    {"prizes.1": {"$exists": True}}
))
