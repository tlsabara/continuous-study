from abc import abstractmethod, ABC
from enum import Enum, auto
import uuid

class DeliveryClass(Enum):
    BASIC = auto()
    EXPRESS = auto()

class DeliveryOrder(ABC):
    def __init__(self, sender_address:str=None, reciver_address:str=None, contact:str=None, *args, **kwargs) -> None:
        self.id: str = uuid.uuid4()
        self.sender_address: str = sender_address
        self.reciver_address: str = reciver_address
        self.contact: str = contact
        self._valid: bool = False

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.id}>"

    def validate(self) -> str:
        if self.reciver_address and self.sender_address:
            self._valid = True
            return "Ordem pdoe ser execcutada!!"
        return "Ordem não pode ser executada, cadastro incompleto"

    @abstractmethod
    def start_delivery(self) -> str:
        ...


class BasicDelivery(DeliveryOrder):
    def start_delivery(self) -> str:
        print("Enviando SMS para o contato")
        return f"Pedido inciado com suicesso"


class ExpressDelivery(DeliveryOrder):
    def start_delivery(self) -> str:
        print("Ligando para o ")
        return f"Pedido de entrega inciado"


class DeliveryFactory:
    @staticmethod
    def get_delivery(delivery_type: DeliveryClass):
        if delivery_type == DeliveryClass.BASIC:
            return BasicDelivery()
        if delivery_type == DeliveryClass.EXPRESS:
            return ExpressDelivery()

        else:
            raise TypeError("DeliveryClass not match.")

if __name__ == "__main__":
    pedido = DeliveryFactory.get_delivery(DeliveryClass.EXPRESS)
    print(pedido)
    pedido = DeliveryFactory.get_delivery(DeliveryClass.BASIC)
    print(pedido)
    pedido = DeliveryFactory.get_delivery("Ola")
    print(pedido)