from typing import List

from system.pedido import Pedido

class Cliente:
    def __init__(self, nombre:str) -> None:
        self.__nombre: nombre
        self.__pedidos: List['Pedido'] = []
    
    def __repr__(self) -> str:
        return(
            f'{self.__class__.__name__}('
            f'{self.__nombre}, '
            f'{self.__pedidos})'
        )