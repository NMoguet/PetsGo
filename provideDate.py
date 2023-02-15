import pika
import datetime

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='date_request_queue')
channel.queue_declare(queue='date_response_queue')


# Define a callback function to handle incoming messages
def callback(ch, method, properties, body):
    # Retrieve the current date
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # Send the date back to the response queue
    channel.basic_publish(
        exchange='',
        routing_key='date_response_queue',
        body=today
    )

    # Acknowledge the message
    channel.basic_ack(delivery_tag=method.delivery_tag)


# Start consuming messages
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='date_request_queue', on_message_callback=callback)
channel.start_consuming()
