from typing import List

from person.cliente import Cliente
from system.item import Item
from system.pedido import Pedido, PedidoOnline, PedidoTelefono

class Pizzeria:
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__clientes: List['Cliente'] = []
        self.__items: List['Item'] = []
        self.__pedidos: List['Pedido'] = []
    
    def __repr__(self) -> str:
        return(
            f'{self.__class__.__name__}('
            f'{self.__nombre}, '
            f'{self.__clientes}, '
            f'{self.__items}, '
            f'{self.__pedidos})'
        )
    
    def get_items(self) -> List['Item']:
        return self.__items

    def add_item(self, item:'Item'):
        self.__items.append(item)
    

pizzeria = Pizzeria('La Bota')

# Creando los items
pizzeria.add_item(Item('Lasagna', 20000))
pizzeria.add_item(Item('Pizza hawaiana', 15000))
pizzeria.add_item(Item('Calzone', 12500))
pizzeria.add_item(Item('Pasta napolitana', 17200))
pizzeria.add_item(Item('Raviolis', 2200))

print(pizzeria)