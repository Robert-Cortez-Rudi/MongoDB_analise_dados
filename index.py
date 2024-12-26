from pymongo import MongoClient
import timeit
# O timeit é uma biblioteca que permite medir o tempo de execução de um código em Python

client = MongoClient()

db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

# 1 - Busca prêmios de 1910

def get_prize():
    list(db.prizes.find({"year": "1910"}))


# 2 - Função para medir o tempo de execução

def measure_executuion_time(function):
    execution_time = timeit.timeit(function, globals=globals(), number=1) * 1000
    # O timeit.timeit() retorna o tempo de execução em segundos. O globals=globals() indica que a função deve ser executada no escopo global, por isso multiplicamos por 1000 para obter o tempo em milissegundos
    print(f"O tempo de execução: {execution_time:.2f} milissengundos")

# 3 - Sem e com o indice

measure_executuion_time("get_prize()") # Sem índice

db.prizes.create_index([("year", 1)]) # Criando o índice

measure_executuion_time("get_prize()") # Com índice

# 4 - Criando indice composto

db.prizes.create_index([("category", 1), ("year", 1)])

def get_all_prizes_economics():
    list(db.prizes.find(
        {"category": "economics"},
        {"year": 1, "_id": 0}
    ))

measure_executuion_time("get_all_prizes_economics()") # Sem índice
