# from random import randint
# import names
# from pymongo import MongoClient
# import os
# from uuid import uuid4
# from datetime import datetime
# import names
# client = MongoClient("mongodb://localhost:27017")
# db = client["ProjetoGru"]

# nome = names.get_full_name()

# def insert_trainer(name, genero, idade):
#     bd = db.Trainer.insert_one(
#         {
#             "Id": str(uuid4()),
#             "Nome": name,
#             "Genero": genero,
#             "Idade": idade,
#             "created_at": datetime.now(),
#             "status": "ativo",
#         }
#     )

# for N in range(1, 6):
#     insert_trainer(names.get_full_name(gender="male"), "M", randint(1, 80))


#     name = input("Nome: ")
#     genero = input("Genero: ")
#     idade = input("Idade: ")
#     bd = db.Trainer.insert_one(
#         {
#             "Id": str(uuid4()),
#             "Nome": name,
#             "Genero": genero,
#             "Idade": idade,
#             "created_at": datetime.now(),
#             "status": "ativo",
#         }
#     )


# update
#  unique_id = input("Digite o id do documeto a ser alterado: ")
# escolha = input("Alterar o [N]ome, [G]enero ou [I]dade? : ")

# if escolha == "N" or "n":
#     nome = input("Escolha um novo nome: ")
#     update_obj = {"$set": {"Nome": nome}}
#     query = {"Id": unique_id}

# elif escolha == "G" or "g":
#     genero = input("Escolha um novo genero: ")

#     update_obj = {"$set": {"Genero": genero}}
#     query = {"Id": unique_id}

# elif escolha == "I" or "i":
#     idade = input("Escolha uma nova idade: ")

#     update_obj = {"$set": {"Idade": idade}}
#     query = {"Id": unique_id}


# elif option_start == "u" or option_start == "U":
#     unique_id = input("Digite o id do documeto a ser alterado: ")
#     escolha = input("Alterar o [N]ome, [G]enero ou [I]dade? : ")
#     objeto = input("Digite o novo: ")
#     choice_dict = {
#             "N": "Nome",
#             "G": "Genero",
#             "I": "Idade"
#         }
#         mapping = choice_dict.get(escolha, "Nome")
#         update_obj = {"$set": {mapping: objeto}}
#         query = {"Id": unique_id}
