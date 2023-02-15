import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the response queue
channel.queue_declare(queue='date_response_queue')

# Define a callback function to handle incoming response messages
def response_callback(ch, method, properties, body):
    print(f"Received date: {body.decode()}")

# Start consuming messages on the response queue
channel.basic_consume(queue='date_response_queue', on_message_callback=response_callback, auto_ack=True)

# Wait for messages
print("Waiting for date response...")
channel.start_consuming()
