import pika
import json
from time import sleep


class RBMQPublisher:
    def __init__(self):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "adm2in"
        self.__password = "123123"
        self.__exchange = "processa_consulta"

        self.__connection = None
        self.channel = None

        self.create_channel()

    def create_channel(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.__host,
                port=self.__port,
                credentials=pika.PlainCredentials(
                    username=self.__username,
                    password=self.__password
                )
            )
        )
        self.channel = self.__connection.channel()

    def publish(self, message, encoding="utf-8", delivery_mode=2):
        print("Publishing.....")
        self.channel.basic_publish(
            exchange=self.__exchange,
            routing_key='',
            body=json.dumps(
                message
            ).encode(encoding),
            properties=pika.BasicProperties(
                delivery_mode=delivery_mode
            )
        )
        print("......Published")


if __name__ == '__main__':
    rbpublisher = RBMQPublisher()
    for i in range(100):
        print("->>", i)
        sleep(1)
        message = {
            "key": "teste_publish",
            "iteration": i
        }
        rbpublisher.publish(message)