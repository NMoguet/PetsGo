# PetsGo

How to request data from RabbitMQ for date micro service (sample code is in between lines):

-----------------------------------------------------------------------

import pika

# Set up a RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the 'date' message queue
channel.queue_declare(queue='date')

# Define a function to consume messages from the 'date' queue
def receive_date(ch, method, properties, body):
    print("Received date:", body.decode()) # Obviously, you 

# Start consuming messages from the 'date' queue
channel.basic_consume(queue='date', on_message_callback=receive_date, auto_ack=True)

# Keep consuming messages until interrupted
channel.start_consuming()

# End code
-----------------------------------------------------------------------

Please see uml_date.png for UML sequence diagram.
