import json
import urllib.request

BASE_URL = "https://mempool.space/api"


def consultar_bitcoin(endpoint):
    url = BASE_URL + endpoint

    try:
        with urllib.request.urlopen(url, timeout=15) as resposta:
            return json.loads(resposta.read().decode())

    except Exception as erro:
        print("Erro:", erro)
        return None


print("=== BITCOIN MEMPOOL MONITOR ===")

mempool = consultar_bitcoin("/mempool")

if mempool:
    print("\nTransacoes pendentes:")
    print(mempool["count"])

taxas = consultar_bitcoin("/v1/fees/recommended")

if taxas:
    print("\nTaxas Bitcoin (sat/vB):")
    print("Urgente:", taxas["fastestFee"])
    print("Normal:", taxas["halfHourFee"])
    print("Economica:", taxas["hourFee"])

blocos = consultar_bitcoin("/blocks")

if blocos:
    print("\nUltimo bloco:")
    print("Altura:", blocos[0]["height"])

print("\nConsulta terminada!")
