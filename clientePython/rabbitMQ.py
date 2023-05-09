import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='ejemplo')

mensaje = 'Hola, este es un mensaje de prueba!'
#channel.basic_publish(exchange='', routing_key='ejemplo', body=mensaje.encode('utf-8'))

print(" [x] Mensaje enviado!")
channel.queue_delete(queue='ejemplo')
connection.close()

# Eliminar cola 'ejemplo'
