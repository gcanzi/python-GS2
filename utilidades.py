"""
Módulo de Utilidades - Orbit Sentinel
Responsável pelas validações de entrada, formatação visual e tratamento de exceções na interface.
"""

import os

def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def linha() -> None:
    print("-" * 55)

def cabecalho(titulo: str) -> None:
    print("=" * 55)
    print(f"  Orbit Sentinel  |  {titulo}")
    print("=" * 55)

def pausar() -> None:
    foguete = r"""
                 ^
                / \
               /___\
              |=   =|
              |  O  |
              |     |
             /|  _  |\
            / | | | | \
           /__|_|_|_|__\
              d b b d
    """
    print(foguete)
    input("  Pressione ENTER para continuar...")
    limpar_tela()

def pedir_string(mensagem: str) -> str:
    while True:
        valor = input(f"  {mensagem}: ").strip()
        if valor:
            return valor
        print("  [!] Entrada inválida. Este campo não pode ficar vazio.")

def pedir_inteiro(mensagem: str) -> int:
    while True:
        valor = input(f"  {mensagem}: ").strip()
        try:
            return int(valor)
        except ValueError:
            print("  [!] Erro: Por favor, digite um número inteiro válido.")

def pedir_float(mensagem: str) -> float:
    while True:
        valor = input(f"  {mensagem}: ").strip().replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            print("  [!] Erro: Por favor, digite um número numérico válido.")

def pedir_opcao_menu(opcoes_validas: list) -> str:
    while True:
        escolha = input("\n  Escolha uma opção: ").strip()
        if escolha in opcoes_validas:
            return escolha
        print("  [!] Opção inválida. Tente novamente.")