# ==================== IF / ELIF / ELSE ====================
nota = 7.5

if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"

print(f"Conceito: {conceito}")


# ==================== FOR ====================
print("\nContagem de 1 a 5:")
for i in range(1, 6):
    print(i)

# Iterando sobre uma lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")


# ==================== WHILE ====================
print("\nContagem regressiva:")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1

print("Fogo!")