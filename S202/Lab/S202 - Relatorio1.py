class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O Professor {self.nome} esta ministrando aula sobre ', assunto)

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        text = f'O aluno {self.nome} esta presente.'
        return text

class Aula:

    def __init__(self, professor, assunto, alunos = []):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicinar_aluno(self, alunos):
        self.alunos.append(alunos)

    def listar_presenca(self):
        alunos = self.alunos.copy()
        text = f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {professor.nome}' \
               f'\ns:'
        for i in range(len(self.alunos)):
            text += f'\n{alunos[i].presenca()}'

        return text

professor = Professor("Eduardo")
aluno1 = Aluno("Joao")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "BD2")
aula.adicinar_aluno(aluno1)
aula.adicinar_aluno(aluno2)
professor.ministrar_aula("BD2")

print(aula.listar_presenca())