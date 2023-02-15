import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Publish a message to the request queue
channel.basic_publish(exchange='',
                      routing_key='date_request_queue',
                      body='Please send me the date!')

# Close the connection
connection.close()