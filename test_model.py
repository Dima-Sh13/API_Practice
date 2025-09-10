from appchanges.model import ModelCoints
from appchanges.config import *

def test_allcoints():
    objCoints = ModelCoints()#creando objeto de la clase
    objCoints.getAllCoints(API_KEY)# llamando al metodo getallcoints
    listas = objCoints.valores_lista
    assert listas != None #True
    cantidad = len(listas)
    assert cantidad == 171#True
    
def test_exchange():
    cambio = ModelCoints()
    cambio.updateExchanges(API_KEY,"BTC")
    assert len(cambio.respuesta) > 0
    assert cambio.respuesta != []    