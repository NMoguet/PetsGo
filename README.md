#PetsGo

The date microservice program can be found in this repo in the file: provideDate.py

A. How to request data

Example code for how to REQUEST data can be found in this repo in the file: requestDate.py

How to request data from RabbitMQ for date microservice (this assumes the system already has RabbitMQ configured):

-----------------------------------------------------------------------
    #Import the pika library
    
import pika

    #Set up a RabbitMQ connection

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

    #Publish a message to the request queue
    
channel.basic_publish(exchange='',
                      routing_key='date_request_queue',
                      body='Please send me the date!')
                      
    #Close the connection

connection.close()

-----------------------------------------------------------------------

Example code for how to RECEIVE data can be found in this repo in the file: receiveDate.py

B. How to receive data from RabbitMQ for date microservice:

    #Import pika library
    
import pika

    #Connect to RabbitMQ

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

    #Declare the response queue
channel.queue_declare(queue='date_response_queue')

    #Define a callback function to handle incoming response messages
def response_callback(ch, method, properties, body):
    print(f"Received date: {body.decode()}")

    #Start consuming messages on the response queue
channel.basic_consume(queue='date_response_queue', on_message_callback=response_callback, auto_ack=True)

    #Wait for messages
    
print("Waiting for date response...")
channel.start_consuming()

-----------------------------------------------------------------------


Please see uml_date.png for UML sequence diagram.
