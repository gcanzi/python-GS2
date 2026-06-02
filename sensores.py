"""
Módulo de Sensores - Orbit Sentinel
Gerencia o inventário de dispositivos de monitoramento climático.
Implementa regras de negócio para garantir a unicidade dos registros.
"""

from utilidades import (
    cabecalho, 
    linha, 
    pausar, 
    pedir_inteiro, 
    pedir_string
)

def buscar_sensor(sensores: list, id_sensor: int) -> dict | None:
    """
    Realiza uma busca linear na lista de sensores.
    Retorna o dicionário do sensor se encontrado, ou None caso contrário.
    """
    for sensor in sensores:
        if sensor["id"] == id_sensor:
            return sensor
    return None

def cadastrar_sensor(sensores: list) -> None:
    """
    Fluxo de registro de um novo equipamento.
    Garante que não existam IDs duplicados no sistema.
    """
    cabecalho("Cadastrar Novo Sensor")
    
    id_sensor = pedir_inteiro("ID do Sensor (numérico)")
    
    # Validação de regra de negócio: Unicidade de ID
    if buscar_sensor(sensores, id_sensor) is not None:
        print(f"\n  [!] Falha no registro: O ID {id_sensor} já está em uso por outro equipamento.")
        pausar()
        return

    tipo_sensor = pedir_string("Tipo do Sensor (ex: Temperatura, Umidade, Fumaça)")
    localizacao = pedir_string("Localização / Setor (ex: Zona Norte, Floresta A)")

    novo_sensor = {
        "id": id_sensor,
        "tipo": tipo_sensor,
        "local": localizacao
    }

    sensores.append(novo_sensor)

    linha()
    print("  [✓] Sensor homologado e registrado com sucesso no sistema.")
    print(f"      ID: {id_sensor} | Tipo: {tipo_sensor} | Local: {localizacao}")
    pausar()

def listar_sensores(sensores: list) -> None:
    """
    Exibe o inventário completo de sensores ativos na infraestrutura.
    """
    cabecalho("Inventário de Sensores")

    if not sensores:
        print("\n  [!] Nenhum sensor registrado na infraestrutura atual.")
        pausar()
        return

    print(f"\n  {'ID':<8} | {'TIPO':<20} | {'LOCALIZAÇÃO'}")
    linha()
    
    for sensor in sensores:
        print(f"  {sensor['id']:<8} | {sensor['tipo']:<20} | {sensor['local']}")
    
    linha()
    print(f"  Total de dispositivos ativos: {len(sensores)}")
    pausar()