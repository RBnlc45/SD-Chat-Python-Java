import pika
import requests
import threading

class Modelo:

    def __init__(self, controlador):
        self.controlador = controlador

        self.conexion = None
        self.canalRecibir = None
        self.canalEnviar = None

        self.host = None #Ip RabbitMQ
        self.nombre = None #Nombre usuarios
        self.destinatario = None #Nombre del destinatario

    def setHost(self, host):
        self.host = host

    def setNombre(self, nombre): #Nombre usuario
        self.nombre = nombre

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
        self.canalEnviar.queue_declare(queue=destinatario)

    def conectar(self, host):
        self.setHost(host)
        # Establecer una conexión con el servidor RabbitMQ
        self.conexion = pika.BlockingConnection(pika.ConnectionParameters(host=host))

    def enviarMensaje(self, mensaje):
        self.canalEnviar.basic_publish(exchange='', routing_key=self.destinatario, body=mensaje.encode('utf-8'))

    def obtenerUsuarios(self):
        url = f'http://{self.host}:{15672}/api/queues'
        response = requests.get(url, auth=("guest", "guest"))
        queues = response.json()
        users = list()
        for queue in queues:
            user = queue['name']
            if user != self.nombre: users.append(user)
        return users

    def estaCanalUsado(self, nombre):
        def start_consuming():
            def callback(ch, method, properties, body):
                self.controlador.mostrarMensaje(body.decode('utf-8'))

            # Recibir los mensajes colocados en mi queue
            self.canalRecibir.basic_consume(queue=nombre, on_message_callback=callback, auto_ack=True)
            self.canalRecibir.start_consuming()

        try:
            self.canalRecibir = self.conexion.channel()
            self.canalEnviar = self.conexion.channel()
            colaRecibir=self.canalRecibir.queue_declare(queue=nombre)

            if (colaRecibir.method.consumer_count == 0) :
                threading.Thread(target=start_consuming, daemon=True).start()
                return False
            else:
                return True
        except:
            return True

    def cerrarConexion(self):
        self.conexion.close()


    '''def __init__(self, cola, view=None, host='localhost', name="cliente2"):
        self.view = view
        self.host = host
        self.name = name
        # Yo cliente 1
        # establecer una conexión con el servidor RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel_receive = self.connection.channel()  # Canal para recibir mensajes
        self.channel_send = self.connection.channel()  # Canal para enviar mensajes

        # declarar una cola recibir en el servidor RabbitMQ
        self.channel_receive.queue_declare(queue="cliente2")
        # Cola para enviar los mensajes a cliente 2
        self.channel_send.queue_declare(queue="cliente1")

        def start_consuming(cola):
            # Recibir los mensajes colocados en mi queu cliente1
            self.channel_receive.basic_consume(queue='cliente2', on_message_callback=self.callback, auto_ack=True)
            try:
                self.channel_receive.start_consuming()
            except KeyboardInterrupt:
                self.channel_receive.stop_consuming()

            # Enviar un mensaje especial a la cola para indicar que la suscripción ha sido detenida
            cola.put(None)

        threading.Thread(target=start_consuming, args=(cola,), daemon=True).start()

    def callback(self, ch, method, properties, body):
        self.view.add_message(body.decode('utf-8'))

    def send_message(self, mensaje):
        # publicar mensaje en cola chat
        self.channel_send.basic_publish(exchange='', routing_key='cliente1', body=mensaje.encode('utf-8'))

    """def receive_message(self, channel, method, properties, body):
        print('pappa')
        #self.view.add_message(body.decode('utf-8'))
        #channel.basic_ack(delivery_tag=method.delivery_tag)*/"""

    def get_users(self):
        url = f'http://{self.host}:{15672}/api/queues'
        response = requests.get(url, auth=("guest", "guest"))
        queues = response.json()
        users = list()
        for queue in queues:
            user = queue['name']
            if user != self.name: users.append(user)
        return user

    def close_connection(self):
        self.connection.close() '''


