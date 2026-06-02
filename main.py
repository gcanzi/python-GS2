"""
Ponto de Entrada - Orbit Sentinel
Orquestra os módulos do sistema, controla o loop de execução principal 
e gerencia a injeção da persistência de dados.

Autores (Equipe de Desenvolvimento):
- Eduarda da Silva Brito
- Gustavo Castilho Gonçalves
- Gustavo Moretim Canzi
- Lucca Ghiraldi Urso
"""

from utilidades import limpar_tela, cabecalho, linha, pedir_opcao_menu
from arquivos import carregar_dados, salvar_dados
from sensores import cadastrar_sensor, listar_sensores
from medicoes_alertas import registrar_medicao
from relatorios import listar_historico_medicoes, exibir_estatisticas

def exibir_menu() -> None:
    """Exibe as opções de navegação do sistema."""
    cabecalho("Menu Principal")
    print("\n  1. Cadastrar Novo Sensor")
    print("  2. Inventário de Sensores")
    print("  3. Registrar Medição Climática")
    print("  4. Histórico de Medições")
    print("  5. Dashboard Estatístico")
    print("  6. Salvar e Sair\n")
    linha()

def main() -> None:
    """Função principal que inicializa o sistema e controla o estado."""
    # Carga inicial de dados do arquivo JSON
    banco_dados = carregar_dados()
    
    # Referências para as listas em memória
    sensores = banco_dados.get("sensores", [])
    medicoes = banco_dados.get("medicoes", [])

    opcoes_validas = ["1", "2", "3", "4", "5", "6"]

    while True:
        limpar_tela()
        exibir_menu()
        opcao = pedir_opcao_menu(opcoes_validas)

        if opcao == "1":
            limpar_tela()
            cadastrar_sensor(sensores)
            # Salva o estado imediatamente após a alteração para evitar perda de dados
            banco_dados["sensores"] = sensores
            salvar_dados(banco_dados)

        elif opcao == "2":
            limpar_tela()
            listar_sensores(sensores)

        elif opcao == "3":
            limpar_tela()
            registrar_medicao(medicoes, sensores)
            banco_dados["medicoes"] = medicoes
            salvar_dados(banco_dados)

        elif opcao == "4":
            limpar_tela()
            listar_historico_medicoes(medicoes, sensores)

        elif opcao == "5":
            limpar_tela()
            exibir_estatisticas(medicoes)

        elif opcao == "6":
            limpar_tela()
            print("\n  Salvando dados e encerrando o Orbit Sentinel...")
            banco_dados["sensores"] = sensores
            banco_dados["medicoes"] = medicoes
            salvar_dados(banco_dados)
            print("  Sistema encerrado com segurança. Até logo!\n")
            break

# Garante que o script só rode se executado diretamente
if __name__ == "__main__":
    main()