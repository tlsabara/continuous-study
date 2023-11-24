import pika
import json
from time import sleep


class RBMQPublisher:
    def __init__(self):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "admin"
        self.__password = "123123"
        self.__exchange = "publisher_consultas"

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

    def publish(self, dict_message, routing_key, encoding="utf-8", delivery_mode=2):
        print("Publishing.....")
        self.channel.basic_publish(
            exchange=self.__exchange,
            routing_key=routing_key,
            body=json.dumps(
                dict_message
            ).encode(encoding),
            properties=pika.BasicProperties(
                delivery_mode=delivery_mode
            )
        )
        print("......Published")


if __name__ == '__main__':
    rbpublisher = RBMQPublisher()
    for i in range(100):
        routing_key = "THIAGO" if i % 7 == 0 else "PEDRO"
        if i % 29 == 0 and i != 0:
            for i2 in range(100):
                print("->>>>>", i2)
                message = {
                    "key": "teste_publish_"+routing_key,
                    f"iteration_inner_{i}": i2
                }
                rbpublisher.publish(message, routing_key)
        print("->>", i)
        if i % 5 == 0 and i != 0:
            sleep(3)

        message = {
            "key": "teste_publish_"+routing_key,
            "iteration": i
        }
        rbpublisher.publish(message, routing_key)