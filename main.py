from pymongo import MongoClient
from uuid import uuid4
from datetime import datetime

# Conexão
client = MongoClient("mongodb://localhost:27017")

db = client["pokemon_battle"]

# --Crud treinador--.

# criando uma collection
db.create_collection("treinador")
{"ok": 1}

# Collection treinador - Create
cadastro = db.treinador.insert_one(
    {
        "unique_id": str(uuid4()),
        "nome": "lucas oliveira",
        "idade": 25,
        "genero": "m",
        "status": "true",
        "created_at": datetime.now(),
    }
)
print("Cadastrado com sucesso.")


# Collection treinador - Read all
read_all = db.treinador.find({})
for dado in read_all:
    print(dado)

# Collection treinador - Read one
read_one = db.treinador.find_one({"unique_id": "4224d0f2-c2fd-4f75-b3c5-99a007e917b9"})
if read_one:
    print(read_one)
else:
    print("Não encontrado")


# Collection treinador - Update
updatee_one = db.treinador.update_one(
    {"unique_id": "4224d0f2-c2fd-4f75-b3c5-99a007e917b9"},
    # {"$set": {"nome": "Moly"}},
    # {"$set": {"idade": 30}},
    {"$set": {"status": "true"}},
)
print("Update realizado.")


# Collection treinador - Delete
delete = db.treinador.delete_one({"unique_id": "3ab67d86-b192-48dc-b848-41444e8593kee"})
if delete:
    print("Dados deletados com sucesso.")
else:
    print("Não encontrado.")


# Collection treinador - Skip
trinador_skip = db.treinador.find().skip(0).limit(10)
for dados in trinador_skip:
    print(dados)
