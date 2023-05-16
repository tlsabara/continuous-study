from abc import ABC, abstractmethod

class Comida(ABC):
    @abstractmethod
    def preparo(self): pass

    @abstractmethod
    def servir(self): pass


class Pizza(Comida):
    def preparo(self):
        print('Abrir a massa..')
        print('Colocar o molho')
        print('Colocar o Recheio')
        print('Colocar o tempero')
        print('Decorar a pizza.')

    def pos_preparo(self):
        print('Cortar em 8 pedaços')
        print('Complemento de decoração')
        if self.__entrega:
            print('Embalar')
        else:
            print('Colocar na bandeja')
        self._pronto = True


