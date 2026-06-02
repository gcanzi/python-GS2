"""
Módulo de Medições e Alertas - Orbit Sentinel
Processa as coletas de dados dos sensores e implementa o motor de regras
para emissão de alertas climáticos preventivos.
"""

from datetime import datetime
from utilidades import cabecalho, linha, pausar, pedir_inteiro, pedir_float
from sensores import buscar_sensor

def analisar_alerta(tipo_sensor: str, valor: float) -> str:
    """
    Motor de regras climáticas.
    Avalia o valor medido com base no tipo de sensor e retorna o status de risco.
    """
    tipo = tipo_sensor.strip().lower()
    
    if "temperatura" in tipo:
        if valor >= 35.0:
            return "ALERTA CRÍTICO: Calor Extremo / Risco de Queimada"
        elif valor >= 30.0:
            return "Atenção: Temperatura Elevada"
            
    elif "umidade" in tipo:
        if valor <= 20.0:
            return "ALERTA CRÍTICO: Baixa Umidade do Ar"
        elif valor >= 90.0:
            return "ALERTA CRÍTICO: Risco de Enchente"
            
    elif "fumaça" in tipo or "gas" in tipo or "gás" in tipo:
        if valor >= 50.0: # Considerando um índice hipotético de qualidade do ar
            return "ALERTA CRÍTICO: Alta Concentração de Fumaça"
            
    return "Normal"

def registrar_medicao(medicoes: list, sensores: list) -> None:
    """
    Fluxo de registro de uma nova medição climática.
    Exige a vinculação com um sensor previamente cadastrado.
    """
    cabecalho("Registrar Nova Medição")

    if not sensores:
        print("\n  [!] Operação bloqueada: Nenhum sensor cadastrado no sistema.")
        print("  Por favor, cadastre um sensor antes de registrar medições.")
        pausar()
        return

    id_sensor = pedir_inteiro("ID do Sensor correspondente")
    
    # Validação de integridade: O sensor existe?
    sensor = buscar_sensor(sensores, id_sensor)
    if sensor is None:
        print(f"\n  [!] Erro: Sensor com ID {id_sensor} não encontrado na infraestrutura.")
        pausar()
        return

    print(f"\n  [Sensor Localizado] Tipo: {sensor['tipo']} | Local: {sensor['local']}")
    valor_medido = pedir_float(f"Valor registrado para {sensor['tipo']}")
    
    # Analisa o risco no momento da coleta
    status_alerta = analisar_alerta(sensor["tipo"], valor_medido)
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    nova_medicao = {
        "id_sensor": id_sensor,
        "valor": valor_medido,
        "status": status_alerta,
        "timestamp": data_hora_atual
    }

    medicoes.append(nova_medicao)

    linha()
    if "ALERTA CRÍTICO" in status_alerta:
        print(f"  [!!!] {status_alerta.upper()} [!!!]")
    else:
        print("  [✓] Leitura registrada com sucesso.")
        
    print(f"      Valor: {valor_medido} | Status: {status_alerta} | Data: {data_hora_atual}")
    pausar()