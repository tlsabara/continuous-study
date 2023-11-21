import pika

def callback_read(ch, method, properties, body):
    print(body)

conn_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials("admin", "123123"),
)

channel = pika.BlockingConnection(conn_params).channel()

channel.queue_declare(
    queue="queue_processa_consulta",
    durable=True,
)

channel.basic_consume(
    queue="queue_processa_consulta",
    auto_ack=True,
    on_message_callback=callback_read
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

