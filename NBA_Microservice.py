import pika
import json
import random


def on_message_received(channel, method, properties, body):
    """Decodes received JSON string into a Python list, generates a random int based on the size of the list,
    selects the value at that index, and sends it back via RabbitMQ."""
    data = json.loads(body)

    i = random.randint(0, len(data) - 1)

    result = data[i]

    # Responds via RabbitMQ server queue "randomized_name_result"
    channel.queue_declare(queue='randomized_name_result')

    channel.basic_publish(exchange='', routing_key='randomized_name_result', body=result)

    connection.close()


# Connects via localhost
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# Receives via RabbitMQ server queue "randomized_name"
channel.queue_declare(queue='randomized_name')

channel.basic_consume(queue='randomized_name', auto_ack=True, on_message_callback=on_message_received)

channel.start_consuming()
