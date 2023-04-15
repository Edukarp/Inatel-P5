from pymongo import MongoClient
from bson.objectid import ObjectId
from Corrida import Corrida
from Passageiro import Passageiro

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_driver(self, nota: int, corridas:Corrida, quantCorridas:int):
         try:
            res = self.db.collection.insert_one({"nota": nota})
            for i in range(quantCorridas):
                res += self.db.collection.insert_one({"corridas":{ corridas: [
                    {"nota": corridas.nota[i], "distancia": corridas.distancia[i], "valor": corridas.valor[i], "passageiro": {
                        "nome": corridas.passageiro[i].nome, "documento": corridas.passageiro[i].documento
                    }}
                ]}})
            print(f"Driver created with id: {res.inserted_id}")
            return res.inserted_id
         except Exception as e:
            print(f"An error occurred while creating driver: {e}")
            return None

    def read_driver_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Driver found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading driver: {e}")
            return None

    def update_driver(self,id , corridas:Corrida, nota: int, quantCorridas: int ,):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota}})
            for i in range(quantCorridas):
                res += self.db.collection.update_one({"_id": ObjectId(id)},{"$set": {"corridas":{ corridas[i]: [
                    {"nota": corridas[i].nota, "distancia": corridas[i].distancia, "valor": corridas[i].valor, "passageiro": {
                        "nome": corridas[i].passageiro.nome, "documento": corridas[i].passageiro.documento
                    }}
                ]}}})
            print(f"Driver updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None

    def delete_driver(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Driver deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting driver: {e}")
            return None