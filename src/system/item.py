class Item:
    
    id = 0
    
    def __init__(self, nombre:str, valor:int) -> None:
        self.__id = Item.id
        self.__nombre = nombre
        self.__valor = valor

        Item.id += 1
    
    def __repr__(self) -> str:
        return(
            f'{self.__class__.__name__}('
            f'{self.__id}, '
            f'{self.__nombre})'
        )
