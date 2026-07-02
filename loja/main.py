"""
main.py
Sistema Interativo de Geração de Nota Fiscal de Compra

Funcionalidades:
- Menu interativo para adicionar produtos ao carrinho
- Geração automática da Nota Fiscal no banco de dados
- Renderização visual da nota + salvamento em arquivo .txt
"""

from gerenciador_banco import (
    criar_tabelas,
    inserir_fornecedor,
    gerar_nota_fiscal,
    buscar_nota_fiscal
)
from gerenciador_template import renderizar_nota_fiscal, salvar_nota_em_arquivo


# ============================================================
# CATÁLOGO DE PRODUTOS DISPONÍVEIS
# ============================================================
PRODUTOS = [
    {"id": 1, "descricao": "Notebook Dell Inspiron 15", "valor_unitario": 3499.90},
    {"id": 2, "descricao": "Mouse sem fio Logitech", "valor_unitario": 89.90},
    {"id": 3, "descricao": "Teclado Mecânico RGB", "valor_unitario": 249.00},
    {"id": 4, "descricao": "Monitor 27'' Full HD", "valor_unitario": 1299.00},
    {"id": 5, "descricao": "Headset Gamer HyperX", "valor_unitario": 299.90},
    {"id": 6, "descricao": "Webcam Full HD Logitech", "valor_unitario": 189.00},
]


def mostrar_produtos():
    """Exibe o catálogo de produtos disponíveis."""
    print("\n" + "=" * 70)
    print("PRODUTOS DISPONÍVEIS")
    print("=" * 70)
    print(f"{'ID':<4} {'Descrição':<40} {'Preço Unitário':>15}")
    print("-" * 70)
    for produto in PRODUTOS:
        print(f"{produto['id']:<4} {produto['descricao']:<40} R$ {produto['valor_unitario']:>10.2f}")
    print("-" * 70)


def adicionar_ao_carrinho(carrinho: list):
    """Permite o usuário adicionar produtos ao carrinho."""
    mostrar_produtos()
    
    try:
        produto_id = int(input("\nDigite o ID do produto que deseja comprar: "))
        quantidade = int(input("Digite a quantidade: "))
        
        # Buscar o produto pelo ID
        produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
        
        if produto and quantidade > 0:
            carrinho.append({
                "descricao": produto["descricao"],
                "quantidade": quantidade,
                "valor_unitario": produto["valor_unitario"]
            })
            print(f"\n✓ {quantidade}x {produto['descricao']} adicionado ao carrinho!")
        else:
            print("\n✗ Produto não encontrado ou quantidade inválida.")
    except ValueError:
        print("\n✗ Entrada inválida. Digite apenas números.")


def mostrar_carrinho(carrinho: list):
    """Mostra os itens atualmente no carrinho."""
    if not carrinho:
        print("\nSeu carrinho está vazio.")
        return

    print("\n" + "=" * 70)
    print("SEU CARRINHO")
    print("=" * 70)
    print(f"{'Descrição':<40} {'Qtd':>6} {'Unit.':>12} {'Total':>12}")
    print("-" * 70)
    
    total = 0
    for item in carrinho:
        subtotal = item["quantidade"] * item["valor_unitario"]
        total += subtotal
        print(f"{item['descricao']:<40} {item['quantidade']:>6} R$ {item['valor_unitario']:>10.2f} R$ {subtotal:>10.2f}")
    
    print("-" * 70)
    print(f"{'TOTAL DO CARRINHO:':<52} R$ {total:>15.2f}")
    print("=" * 70)


def main():
    print("=" * 70)
    print("SISTEMA INTERATIVO DE NOTA FISCAL DE COMPRA")
    print("=" * 70)

    # Preparar banco de dados
    criar_tabelas()

    # Garantir que o fornecedor existe
    fornecedor_id = inserir_fornecedor(
        nome="Tech Solutions Ltda",
        cnpj="12.345.678/0001-90",
        endereco="Rua das Inovações, 456 - São Paulo/SP"
    )

    carrinho = []

    while True:
        print("\n" + "=" * 70)
        print("MENU PRINCIPAL")
        print("=" * 70)
        print("1 - Ver produtos disponíveis")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra e gerar Nota Fiscal")
        print("0 - Sair")
        print("=" * 70)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_produtos()

        elif opcao == "2":
            adicionar_ao_carrinho(carrinho)

        elif opcao == "3":
            mostrar_carrinho(carrinho)

        elif opcao == "4":
            if not carrinho:
                print("\nSeu carrinho está vazio. Adicione produtos antes de finalizar.")
                continue

            # Gerar Nota Fiscal
            nota_id = gerar_nota_fiscal(fornecedor_id=fornecedor_id, itens=carrinho)
            dados_nota = buscar_nota_fiscal(nota_id)

            # Renderizar e mostrar
            print("\n" + "=" * 70)
            print("NOTA FISCAL GERADA COM SUCESSO!")
            print("=" * 70)
            nota_formatada = renderizar_nota_fiscal(dados_nota)
            print(nota_formatada)

            # Salvar em arquivo
            salvar_nota_em_arquivo(dados_nota)

            print("\n✓ Compra finalizada com sucesso!")
            break  # Finaliza o programa após gerar a nota

        elif opcao == "0":
            print("\nObrigado por usar o sistema!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()