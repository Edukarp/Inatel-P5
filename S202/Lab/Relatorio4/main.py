from database import Database
from writeAJson import writeAJson
from ProductAnalyzer import *

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

productAnalyzer = ProduductAnalyzer(db)

productAnalyzer.totalVendidoPorDia()
productAnalyzer.produtoMaisVendido()
productAnalyzer.clienteQueGastouMais()
#productAnalyzer.produtoVendido() #Nao deu certo o ultimo caso