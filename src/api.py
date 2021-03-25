import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('API_HOST')
api_key = os.getenv('API_KEY')

def quote_stock(symbol):
    url = f'{base_url}/stock/{symbol}/quote/latestPrice?token={api_key}'
    r = requests.get(url)
    if r.status_code == 200:
        quote = f"Cotação atual: ${r.text}"
        return quote
    else:
        print(f"Status code: {r.status_code}")
        return "Símbolo não encontrado"
