from MVC.modelo.Modelo import Modelo
from MVC.vista.Vista import Vista
import queue

class Controlador:
    def __init__(self):
        self.vista = Vista(self)
        self.modelo = None

        self.estaServerDisponible('localhost')
        self.estaUsuarioDisponible('mateo')
        self.usuariosDisponibles('mateo')
        self.cambiarDestinatario('juan')


    def enviarMensaje(self, mensaje):
        self.modelo.enviarMensaje(mensaje)

    def mostrarMensaje(self, message):
        self.vista.add_message(message)

    def estaServerDisponible(self, host):
        try:
            self.modelo = Modelo(self)
            self.modelo.conectar(host)
            return True
        except:
            return False

    def cambiarDestinatario(self, destinatario):
        try:
            self.modelo.setDestinatario(destinatario)
            return True
        except IOError as e:
            print(e.__cause__.getMessage())
            return False

    def estaUsuarioDisponible(self, usuario):
        if self.modelo.estaCanalUsado(usuario): return False
        else: return True

    def usuariosDisponibles(self, usuario):
        self.modelo.setNombre(usuario)
        return self.modelo.obtenerUsuarios()

    def close_connection(self):
        self.modelo.cerrarConexion()

    def run(self):
        self.vista.run()

