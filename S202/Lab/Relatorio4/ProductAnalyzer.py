from writeAJson import writeAJson
class ProduductAnalyzer:

    def __init__(self, database):
        self.database = database

    def totalVendidoPorDia(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}}
            ])
        writeAJson(result, "Total Vendido por Dia")

    def produtoMaisVendido(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    def clienteQueGastouMais(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$limit": 1}
            ])
        writeAJson(result, "Cliente que Gastou Mais")

    def produtoVendido(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "produto":"$produtos.descricao"},"quantidade": {"$gt":["$produtos.quantidade", 1]}}}
        ])
        writeAJson(result, "Pelo mais de 1 unidade vendida do Produto")