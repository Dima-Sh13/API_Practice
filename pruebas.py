import requests
from config import API_KEY


moneda = input("Introduce una moneda").upper()


r = requests.get(f"https//api.exchangerate.host/live?acces_key={API_KEY}&source={moneda}&currencies=EUR,USD")


answer = r.json()

if r.status_code == 200:
    print("rates: ",answer.get("quotes"))
    value1 = moneda + "EUR"
    value2 = moneda + "USD"
else:
    print("error: ",answer)    