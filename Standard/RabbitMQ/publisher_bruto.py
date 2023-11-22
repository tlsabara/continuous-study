import time

import pika
import json


conn_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="admin",
        password="123123"
    ),
)

channel = pika.BlockingConnection(conn_params).channel()

# channel.exchange_declare(
#     exchange="queue_processa_consulta",
#     durable=True
# )


for i in range(100):
    print("Publishing.....", i)
    time.sleep(1)
    channel.basic_publish(
        exchange='processa_consulta',
        routing_key='',
        body=json.dumps(
            dict(
                key="teste",
                iteration=i
            )
        ).encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

