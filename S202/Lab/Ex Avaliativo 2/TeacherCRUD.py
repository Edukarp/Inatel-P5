class TeacherCRUD:

    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):  #cria um Teacher
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf }
        self.db.execute_query(query, parameters)
        print(f"Teacher {name} created")

    def read(self, name): #retorna apenas um Teacher
        query = "MATCH (n:Teacher{name: '$name'}) RETURN n"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete(self, name): #deleta Teacher com base no name
        query = "MATCH (n:Teacher {name: $name}) DETACH DELETE n"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"Teacher {name} deleted")

    def update(self, name, newCpf):  #atualiza cpf com base no name
        query = "MATCH (n:Teacher {name: $name}) SET n.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher {name} updated")
