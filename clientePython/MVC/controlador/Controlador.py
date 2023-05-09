from MVC.modelo.Modelo import Modelo
from MVC.vista.Vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista(self)
        self.modelo = None

        self.estaServerDisponible('localhost')
        self.estaUsuarioDisponible('chusino')
        self.usuariosDisponibles('chusino')
        self.cambiarDestinatario('JoseMaria')


    def enviarMensaje(self, mensaje):
        self.modelo.enviarMensaje(mensaje)

    def mostrarMensaje(self, mensaje):
        #self.vista.add_message(mensaje)
        print(mensaje)

    def estaServerDisponible(self, host):
        try:
            self.modelo = Modelo(self)
            self.modelo.conectar(host)
            print('Se conecto')
            return True
        except:
            print('No se conecto')
            return False

    def cambiarDestinatario(self, destinatario):
        try:
            self.modelo.setDestinatario(destinatario)
            return True
        except IOError as e:
            print(e.__cause__.getMessage())
            return False

    def estaUsuarioDisponible(self, usuario):
        self.modelo.setNombre(usuario)
        if self.modelo.estaCanalUsado(usuario):
            print('Ocupado')
            return False
        else:
            print('Libre')
            return True

    def usuariosDisponibles(self, usuario):
        return self.modelo.obtenerUsuarios()

    def close_connection(self):
        self.modelo.cerrarConexion()

    def run(self):
        self.vista.run()

