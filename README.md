# NBA_Microservice
Microservice designed to take a JSON string of a Python list and return a random item from the list. Sending/Receiving via RabbitMQ server queues on localhost.

Instructions:
  Requesting data from the microservice:
  
    Requests are made via RabbitMQ. ConnectionParameters are set to 'localhost'. Queue is set to 'randomized_name'.
    To send our Python list via RabbitMQ, we use json.dumps([your, list, here]).
    
      Example:
      
        message = json.dumps([this, is, a, list])
        channel.queue_declare(queue='randomized_name')
        channel.basic_publish(exchange='', routing_key='randomized_name', body=message)
        
  Received data from the microservice:
  
    Receipts are made via RabbitMQ. ConnectionParameters are still set to 'localhost'. Queue is now set to 'randomized_name_result'.
    Data is returned as a string, so there is no need for json parsing.
    
      Example:
      
        channel.queue_declare(queue="randomized_name_result")
        channel.basic_consume(queue='randomized_name_result', auto_ack=True, on_message_callback=on_message_received)
        channel.start_consuming()
  
  UML Sequence Diagram:
  
 ![UMLSequenceDiagram](https://user-images.githubusercontent.com/102569472/217657224-1c300cf8-4212-41d2-9b72-436e70cbb279.PNG)
