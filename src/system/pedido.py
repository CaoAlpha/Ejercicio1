from abc import ABC, abstractmethod
from typing import List, Any

from system.item import Item
from person.cliente import Cliente


class Pedido (ABC):
    def __init__(self, cliente:['Cliente']) -> None:
        self._clientes = cliente
        self._items: List['Item'] = []


    @abstractmethod
    def __repr__(self) -> str:
        return(
            f'{self.__class__.__name__}('
            f'{self._clientes}, '
            f'{self._items}, '
        )
    


class PedidoOnline(Pedido):
    def __init__(self, email:str, **kwargs:Any) -> None:
        self.__email = email
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()


class PedidoTelefono(Pedido):
    def __init__(self, telefono:str, **kwargs:Any) -> None:
        self.__telefono = telefono
        super().__init__(*kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
        