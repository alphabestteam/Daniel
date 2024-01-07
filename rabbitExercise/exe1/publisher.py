import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tasks', exchange_type='direct')

channel.queue_declare(queue='hello')

channel.queue_bind(exchange='tasks', queue='hello', routing_key='task')

message = 'Create a task management website'
channel.basic_publish(exchange='tasks', routing_key='task', body=message)

print("Sent message")

connection.close()
