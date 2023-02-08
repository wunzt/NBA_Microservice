import pika
import json
import random

"""Decodes received JSON string into a Python list, generates a random int based on the size of the list,
selects the value at that index, and sends it back via RabbitMQ."""
def on_message_received(channel, method, properties, body):
    data = json.loads(body)
    print(data)

    i = random.randint(0, len(data) - 1)
    print(i)

    result = data[i]
    print(result)

    channel.queue_declare(queue='randomized_name_result')      # Responds via RabbitMQ server queue "randomized_name_result"

    channel.basic_publish(exchange='', routing_key='randomized_name_result', body=result)

    print(f"sent message: {result}")

    connection.close()


connection_parameters = pika.ConnectionParameters('localhost')      # Connects via localhost

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='randomized_name')      # Receives via RabbitMQ server queue "randomized_name".

channel.basic_consume(queue='randomized_name', auto_ack=True, on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()
