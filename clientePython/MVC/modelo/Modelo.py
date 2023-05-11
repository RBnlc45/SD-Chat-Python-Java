import pika
import requests
import threading
class Conexion():
    def __init__(self, controlador) -> None:
        self.controlador = controlador

        self.conexion = None
        self.canalRecibir = None
        self.canalEnviar = None
        
        self.usuarios = []

        self.host = None #Ip RabbitMQ
        self.nombre = None #Nombre usuario
        self.destinatario = None #Nombre del destinatario

    def listar_usuarios(self):
        #Escribir código para listar usuarios, agregar usuarios a la lista con su nombre y su ip en tupla (nombre, ip)
        usuarios = [("Albert", "192.168.0.1"), ("Juan", "172.56.7.2")]
        
        return usuarios

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
        try:
            self.conexion = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        except:
            return False

        return True

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


class Chat():
    def __init__(self, nombre: str, ip: str) -> None:
        self.nombre = nombre
        self.ip = ip
        self.mensajes = []
    
    #Destinatario = True si el mensaje llega desde el destinario, = False si sale desde el usuario
    def ingresar_mensaje(self, mensaje: str, destinarario: bool):
        self.mensajes.append((mensaje, destinarario))
        
        if not destinarario:
            #Escribir código para enviar mensaje a destinario self.ip es la ip del destinario
            pass
    
    async def recibir_mensaje(self):
        #Escribir código para recibir mensaje
        
        mensaje = "Mensaje recibido"
        self.ingresar_mensaje(mensaje, True)
    

class Usuario():
    def __init__(self, nombre: str, ip: str) -> None:
        self.nombre = nombre
        self.ip = ip
        self.chats = []
    
    def crear_chat(self, nombre: str, ip: str) -> None:
        self.chats.append(Chat(nombre, ip))
    
    def buscar_chat(self, nombre: str, ip: str) -> Chat:
        for chat in self.chats:
            if chat.nombre == nombre:
                return chat
        
        self.crear_chat(nombre, ip)
        return self.chats[-1]
    
    