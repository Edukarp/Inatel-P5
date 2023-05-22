from database import Database
def execicio1(db):
    #Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.
    print(db.execute_query("MATCH (n:Teacher{name: 'Renzo'}) RETURN n.ano_nasc,n.cpf"))

    #Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.
    print(db.execute_query("MATCH (n:Teacher) WHERE n.name STARTS WITH 'M' RETURN n.name,n.cpf"))

    #Busque pelos nomes de todas as cidades “City” e retorne-os.
    print(db.execute_query("MATCH (n:City) RETURN n.name"))

    #Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550,
    # retorne o nome da escola, o endereço e o número
    print(db.execute_query("MATCH (n:School) WHERE n.number >=150 and n.number < 550 "
                           "RETURN n.name, n.address,n.number"))

def exercio2(db):
    #Encontre o ano de nascimento do professor mais jovem e do professor mais velho
    print(db.execute_query("MATCH (n:Teacher) WITH n ORDER BY n.ano_nasc DESC LIMIT 1 RETURN n.ano_nasc"))  #jovem
    print(db.execute_query("MATCH (n:Teacher) WITH n ORDER BY n.ano_nasc ASC LIMIT 1 RETURN n.ano_nasc")) #velho

    #Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.
    print(db.execute_query("MATCH (n:City) RETURN AVG(n.population)"))

    #Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A”
    print(db.execute_query("MATCH (n:City {cep: '37540-000'}) RETURN REPLACE(n.name, 'a', 'A')"))

    #Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
    print(db.execute_query("MATCH (n:Teacher) RETURN substring(n.name, 2, 1)"))