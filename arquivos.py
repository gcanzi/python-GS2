"""
Módulo de Persistência - Orbit Sentinel
Responsável pela leitura e escrita segura da base de dados em formato JSON.
"""

import json
import os

# Configuração do banco de dados
ARQUIVO_DADOS = "banco_dados.json"

def carregar_dados() -> dict:
    # Carrega os dados do arquivo JSON ou retorna a estrutura vazia padrão
    estrutura_padrao = {"sensores": [], "medicoes": []}

    if not os.path.exists(ARQUIVO_DADOS):
        return estrutura_padrao

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
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
    # Salva a estrutura de dados atualizada no arquivo JSON
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print("  [!] Erro crítico: Sem permissão para salvar no arquivo base.")
    except Exception as e:
        print(f"  [!] Erro crítico ao salvar dados: {e}")