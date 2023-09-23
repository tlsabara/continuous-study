from abc import abstractmethod, ABV
from enum import Enum, auto
import uuid

class DeliveryClass(Enum):
    BASIC = auto()
    EXPRESS = auto()

class DeliveryOrder(ABC):
    def __init__(self, sender_address:str=None, reciver_address:str=None, contact:str=None *args, **kwargs) -> None:
        self.id: str = uuid.uuid4()
        self.sender_address: str = sender_address
        self.reciver_address: str = reciver_address
        self.contact: str = contact
        self._valid: bool = False

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
        return f"My name is {self.frist_name}, and i'm a student of basic school"


class ExpressDelivery(DeliveryOrder):
    def start_delivery(self) -> str:
        print("Ligando para o ")
        return f"My name is {self.frist_name}, and i'm a student of high school"


class DeliveryFactory:
    @staticmethod
    def get_student(student_type: Student, frist_name, last_name):
        if student_type == Student.BASIC_STUDENT:
            return BasicStudent()