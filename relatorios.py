"""
Módulo de Relatórios - Orbit Sentinel
Consolida os dados de medições, gerando o histórico detalhado e
estatísticas de monitoramento para apoio à tomada de decisão.
"""

from utilidades import cabecalho, linha, pausar
from sensores import buscar_sensor

def listar_historico_medicoes(medicoes: list, sensores: list) -> None:
    cabecalho("Histórico de Medições Ambientais")

    if not medicoes:
        print("\n  [!] Não há registros de medições no histórico.")
        pausar()
        return

    print(f"\n  {'DATA/HORA':<20} | {'LOCAL':<15} | {'VALOR':<8} | {'STATUS'}")
    linha()

    for medicao in medicoes:
        sensor = buscar_sensor(sensores, medicao["id_sensor"])
        local_nome = sensor["local"] if sensor else "Desconhecido"
        
        data = medicao['timestamp']
        valor = str(medicao['valor'])
        status = medicao['status']
        
        print(f"  {data:<20} | {local_nome:<15} | {valor:<8} | {status}")

    linha()
    pausar()

def exibir_estatisticas(medicoes: list) -> None:
    #Consolida os dados e exibe a contagem de ocorrências por status

    cabecalho("Dashboard Estatístico")

    if not medicoes:
        print("\n  [!] Dados insuficientes para gerar estatísticas.")
        pausar()
        return

    total_medicoes = len(medicoes)
    
    contagem_status = {}
    total_alertas_criticos = 0

    for medicao in medicoes:
        status = medicao["status"]
        contagem_status[status] = contagem_status.get(status, 0) + 1
        
        if "ALERTA CRÍTICO" in status:
            total_alertas_criticos += 1

    print(f"\n  Total de Leituras Realizadas : {total_medicoes}")
    print(f"  Total de Alertas Críticos    : {total_alertas_criticos}")
    
    print("\n  [ Distribuição por Status ]")
    linha()
    
    for status, quantidade in contagem_status.items():
        print(f"  {quantidade:>3}x - {status}")

    linha()
    pausar()