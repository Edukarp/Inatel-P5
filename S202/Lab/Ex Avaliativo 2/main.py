from query import *
from TeacherCRUD import TeacherCRUD
from cli import *

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.239.191.0:7687", "neo4j", "holds-may-customs")
#db.drop_all()

execicio1(db)
exercio2(db)

teacher_db = TeacherCRUD(db)

#teacher_db.create('Chris Lima', 1956, '189.052.396-66')
#teacher_db.read('Chris Lima')
#teacher_db.update('Chris Lima', '162.052.777-77')


teacher_cli = TeacherCLI(teacher_db)
teacher_cli.run()

