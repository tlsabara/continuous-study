from time import sleep

import pika
import json
class RBMQConsumer:
    def __init__(self, callback_fn):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "admin"
        self.__password = "123123"
        self.__queue = "queue_processa_consulta"
        self.__callback_fn = callback_fn
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
        self.channel.queue_declare(queue=self.__queue, durable=True)
        self.channel.basic_consume(queue=self.__queue, on_message_callback=self.__callback_fn, auto_ack=True)

    def consume(self, callback: callable = None):
        if callback:
            self.__callback_fn = callback
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

def callback_check_json(ch, method, properties, body):
    try:
        print("Processando.....")
        sleep(2)
        json_body = json.loads(body.decode())
    except Exception as e:
        print(e)
    print(json_body)
    print(properties)
    print(f"{'*' * 50}")


if __name__ == '__main__':
    rbconsumer = RBMQConsumer(callback_check_json)
    rbconsumer.consume()