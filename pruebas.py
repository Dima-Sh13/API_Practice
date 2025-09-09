import requests
from config import API_KEY


moneda = input("Introduce una moneda").upper()


r = requests.get(f"https//api.exchangerate.host/live?acces_key={API_KEY}&source={moneda}&currencies=EUR,USD")