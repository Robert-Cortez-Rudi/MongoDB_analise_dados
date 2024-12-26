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

# 3 - Utilizando o Regex

# Alguns laureados que se tornariam Polônia
print(db.laureates.distinct(
    "bornCountry",
    {"bornCountry": {"$regex": "Poland"}}
))

# O $regex é um operador de comparação que permite a utilização de expressões regulares
# O $regex é case sensitive, ou seja, diferencia maiúsculas de minúsculas. 
# Sua função é buscar padrões de texto

# 4 - Case insensitive (Poland)

print(db.laureates.distinct(
    "bornCountry",
    {"bornCountry": {"$regex": "poland", "$options": "i"}}
))

# O $options é um modificador que permite a utilização de opções para a expressão regular
# O "i" é uma opção que torna a expressão regular case insensitive

# 5 - Utilizando a classe Regex
from bson.regex import Regex

print(db.laureates.distinct(
    "bornCountry",
    {"bornCountry": Regex("poland", "i")}
))

# 6 - Começa com

print(db.laureates.distinct(
    "bornCountry",
    {"bornCountry": Regex("^Poland")}
))
# O "^" é um operador de âncora que indica o início de uma string

# 7 - Termina com \ escape de parenteses

print(db.laureates.distinct(
    "bornCountry",
    {"bornCountry": Regex("now Poland\)$")}
))
# O \)$ é um escape de parenteses que indica o final de uma string
