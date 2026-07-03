# Exemplo prático: Sistema de liberação de acesso
idade = 45
tem_carteira = False
tem_multa_pendente = False

# Operador AND (todas as condições precisam ser True)
pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir? {pode_dirigir}")        # True

# Operador OR (pelo menos uma condição precisa ser True)
tem_acesso = tem_carteira or idade >= 21
print(f"Tem acesso? {tem_acesso}")            # True

# Operador NOT (inverte o valor)
esta_bloqueado = not tem_multa_pendente
print(f"Está bloqueado? {esta_bloqueado}")    # True and = && or =|| 