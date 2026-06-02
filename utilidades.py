"""
Módulo de Utilidades - Orbit Sentinel
Responsável pelas validações de entrada, formatação visual e tratamento de exceções na interface.
"""

import os

def limpar_tela() -> None:
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def linha() -> None:
    """Imprime uma linha separadora padronizada."""
    print("-" * 55)

def cabecalho(titulo: str) -> None:
    """Imprime um cabeçalho padronizado para o sistema."""
    print("=" * 55)
    print(f"  Orbit Sentinel  |  {titulo}")
    print("=" * 55)

def pausar() -> None:
    """Pausa a execução da aplicação até o usuário pressionar ENTER."""
    input("\n  Pressione ENTER para continuar...")
    limpar_tela()

def pedir_string(mensagem: str) -> str:
    """Solicita uma entrada de texto e garante que não seja vazia."""
    while True:
        valor = input(f"  {mensagem}: ").strip()
        if valor:
            return valor
        print("  [!] Entrada inválida. Este campo não pode ficar vazio.")

def pedir_inteiro(mensagem: str) -> int:
    """
    Solicita um número inteiro ao usuário.
    Utiliza try/except para capturar erros de conversão (ValueError).
    """
    while True:
        valor = input(f"  {mensagem}: ").strip()
        try:
            return int(valor)
        except ValueError:
            print("  [!] Erro: Por favor, digite um número inteiro válido.")

def pedir_float(mensagem: str) -> float:
    """
    Solicita um número decimal ao usuário.
    Substitui vírgula por ponto para evitar erros no padrão brasileiro.
    """
    while True:
        valor = input(f"  {mensagem}: ").strip().replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            print("  [!] Erro: Por favor, digite um número numérico válido (ex: 35.5).")

def pedir_opcao_menu(opcoes_validas: list) -> str:
    """Valida a seleção de uma opção de menu contra uma lista permitida."""
    while True:
        escolha = input("\n  Escolha uma opção: ").strip()
        if escolha in opcoes_validas:
            return escolha
        print("  [!] Opção inválida. Tente novamente.")