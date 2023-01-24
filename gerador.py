from pymongo import MongoClient
from uuid import uuid4
from datetime import datetime
import names
from random import randint


# Conexão
client = MongoClient("mongodb://localhost:27017")

db = client["pokemon_battle"]


def insert_trainer(name, genero, idade):

    bd = db.treinador.insert_one(
        {
            "unique_id": str(uuid4()),
            "nome": name,
            "genero": genero,
            "idade": idade,
            "created_at": datetime.now(),
            "status": "true",
        }
    )


for c in range(1, 6):
    insert_trainer(names.get_full_name(gender="male"), "m", randint(15, 80))
    insert_trainer(names.get_full_name(gender="female"), "f", randint(15, 80))

print("Inserido.")
