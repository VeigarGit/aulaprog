# ==================== LIST (Lista) ====================
numeros = [10, 20, 30, 40]
numeros.append(50)           # Adiciona no final
numeros.insert(0, 5)         # Adiciona no início
print(numeros)               # [5, 10, 20, 30, 40, 50]


# ==================== DICT (Dicionário) ====================
aluno = {
    "nome": "João",
    "idade": 22,
    "curso": "Engenharia"
}
print(aluno["nome"])         # João
aluno["idade"] = 23          # Atualiza valor


# ==================== TUPLE (Tupla) - imutável ====================
coordenadas = (10, 20)
# coordenadas[0] = 15  # Erro! Tupla não pode ser alterada


# ==================== SET (Conjunto) ====================
numeros_unicos = {1, 2, 3, 3, 4}
print(numeros_unicos)        # {1, 2, 3, 4}