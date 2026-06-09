import requests
import json
from pathlib import Path

# decora kkkk
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_weather_data(url:str) -> list:
    response = requests.get(url)
    data = response.json()

    # O Status code 200 quer dizer sucesso em padrão de API
    if response.status_code != 200:
        logging.error("Erro na requisição")
        return []
    
    if not data:
        logging.warn("Nenhum dado retornado")
        return []

    output_path = 'data/weather_data.json'
    # .parent vai sair da pasta em que estamos e vai procurar a pasta correta, ela vai considerar que o que está sendo procurado não está dentro da pasta
    output_dir = Path(output_path).parent
    # Ele vai criar o arquivo independente do caminho, e o exist_ok vai conferir se ele já existe ou não
    output_dir.mkdir(parents=True, exist_ok=True)

    # abre o arquivo em modo de escrita, pega o json dentro de f e escreve em data
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Dados foram gravados em {output_path}")
    return data
