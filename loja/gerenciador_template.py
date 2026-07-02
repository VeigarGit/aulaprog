from datetime import datetime
from typing import Dict, Any


def renderizar_nota_fiscal(dados: Dict[str, Any]) -> str:
    """
    Renderiza a Nota Fiscal usando um template.
    Atualiza automaticamente sempre que novos dados são passados.
    """
    template = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        NOTA FISCAL DE COMPRA                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Número da NF: {dados.get('numero_nf', 'N/A'):<40} Data: {dados.get('data_emissao', 'N/A')[:10]:<20} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ FORNECEDOR                                                                   ║
║ Nome: {dados.get('fornecedor_nome', 'N/A'):<60} ║
║ CNPJ: {dados.get('cnpj', 'N/A'):<60} ║
║ Endereço: {dados.get('endereco', 'N/A'):<56} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ ITENS                                                                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ {'Descrição':<40} {'Qtd':>6} {'Unit.':>12} {'Total':>12} ║
╠══════════════════════════════════════════════════════════════════════════════╣
"""

    # Adiciona os itens dinamicamente
    for item in dados.get('itens', []):
        linha = f"║ {item['descricao']:<40} {item['quantidade']:>6} R$ {item['valor_unitario']:>10.2f} R$ {item['valor_total']:>10.2f} ║\n"
        template += linha

    # Rodapé com totais
    template += f"""╠══════════════════════════════════════════════════════════════════════════════╣
║ {'VALOR TOTAL DA NOTA:':<52} R$ {dados.get('valor_total', 0):>15.2f} ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """

    return template


def salvar_nota_em_arquivo(dados: Dict[str, Any], nome_arquivo: str = None) -> str:
    """
    Salva a nota fiscal renderizada em um arquivo .txt.
    O nome do arquivo é gerado automaticamente se não for informado.
    """
    if nome_arquivo is None:
        nome_arquivo = f"nota_fiscal_{dados.get('numero_nf', 'sem_numero')}.txt"

    conteudo = renderizar_nota_fiscal(dados)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print(f"Nota fiscal salva em: {nome_arquivo}")
    return nome_arquivo