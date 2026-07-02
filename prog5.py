# ==================== BIBLIOTECA (Library) ====================
# Você controla o fluxo. A biblioteca te ajuda.
import random

numeros = [1, 2, 3, 4, 5]
escolhido = random.choice(numeros)
print(f"Número sorteado: {escolhido}")


# ==================== FRAMEWORK ====================
# O framework controla o fluxo (Inversão de Controle).
# Exemplo com Flask (você só define as rotas):

"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo!"

if __name__ == "__main__":
    app.run()
"""
# Aqui o Flask decide quando chamar sua função home()