# ==================== 1. Paradigma Procedural ====================
def calcular_media(notas):
    return sum(notas) / len(notas)

notas = [7, 8, 9]
media = calcular_media(notas)
print(f"Média (procedural): {media}")


# ==================== 2. Paradigma Orientado a Objetos (OOP) ====================
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

aluno = Aluno("Maria", [7, 8, 9])
print(f"Média de {aluno.nome}: {aluno.calcular_media()}")
aluno = Aluno("Pedro", [7, 8, 9])
print(f"Média de {aluno.nome}: {aluno.calcular_media()}")
aluno = Aluno("João", [7, 8, 9])
print(f"Média de {aluno.nome}: {aluno.calcular_media()}")

# ==================== 3. Paradigma Funcional ====================
from functools import reduce

notas = [7, 8, 9]
media = reduce(lambda x, y: x + y, notas) / len(notas)
print(f"Média (funcional): {media}")