"""
Módulo de Persistência - Orbit Sentinel
Responsável pela leitura e escrita segura da base de dados em formato JSON.
"""

import json
import os

# Constante de configuração do banco de dados
ARQUIVO_DADOS = "banco_dados.json"

def carregar_dados() -> dict:
    """
    Carrega o banco de dados do sistema.
    Retorna a estrutura vazia padrão caso o arquivo não exista ou esteja corrompido.
    """
    estrutura_padrao = {"sensores": [], "medicoes": []}

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(ARQUIVO_DADOS):
        return estrutura_padrao

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
            # Validação estrutural de integridade
            if "sensores" not in dados or "medicoes" not in dados:
                return estrutura_padrao
                
            return dados
            
    except json.JSONDecodeError:
        print("  [!] Aviso: Arquivo de dados corrompido. Iniciando com memória limpa.")
        return estrutura_padrao
    except Exception as e:
        print(f"  [!] Erro inesperado de I/O na leitura: {e}")
        return estrutura_padrao

def salvar_dados(dados: dict) -> None:
    """
    Persiste os dados em disco formatados com indentação para legibilidade.
    """
    try:
        # A flag 'w' substitui o arquivo com os dados mais recentes
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print("  [!] Erro crítico: Sem permissão para salvar no arquivo base.")
    except Exception as e:
        print(f"  [!] Erro crítico ao salvar dados: {e}")