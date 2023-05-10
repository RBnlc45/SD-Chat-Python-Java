class Conexion():
    def __init__(self) -> None:
        self.usuarios = []
    
    def listar_usuarios(self):
        #Escribir código para listar usuarios, agregar usuarios a la lista con su nombre y su ip en tupla (nombre, ip)
        usuarios = [("Albert", "192.168.0.1"), ("Juan", "172.56.7.2")]
        
        return usuarios


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
    
    