import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

from MVC.vista.Vista import Ui_MainWindow
from MVC.vista.Dialog import Ui_Dialog
from MVC.modelo.Modelo import Usuario, Conexion

class Dialogo(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super(Dialogo, self).__init__(parent)
        self.setupUi(self)

class ActualizarChatEvent(QtCore.QEvent):
    """Evento personalizado para actualizar el chat"""
    EventType = QtCore.QEvent.Type(QtCore.QEvent.registerEventType())
    
    def __init__(self):
        super().__init__(ActualizarChatEvent.EventType)

    def __str__(self):
        return "ActualizarChatEvent"

class VentanaChat(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super(VentanaChat, self).__init__(parent)
        self.setupUi(self)
        self.usuario: Usuario | None = None
        self.conexion: Conexion | None = None
        
        #Ventana de dialogo
        self.dialogo = Dialogo()
        
        #Inavilitados
        self.desconectar()
        
        #Botones
        self.pushButtonDesconectar.clicked.connect(self.desconectar)
        self.pushButtonConectar.clicked.connect(self.conectar)
        self.pushButtonEnviar.clicked.connect(self.enviar)
        
        #ComboBox
        self.comboBoxDestinatario.currentIndexChanged.connect(self.cambio_destinatario)
        
    def enviar(self):
        mensaje = self.textMensaje.toPlainText()
        
        chat = self.usuario.buscar_chat(self.comboBoxDestinatario.currentText())
        chat.ingresar_mensaje(mensaje, False)
        self.textMensaje.clear()
        
        self.actualizar_chat()
        
        self.conexion.enviarMensaje(mensaje)
    
    def actualizar_chat(self):
        if self.usuario != None:
            chat = self.usuario.buscar_chat(self.comboBoxDestinatario.currentText())
            self.cargar_mensajes_ui(chat.nombre, chat.mensajes)
            return
        
        self.cargar_mensajes_ui("", [])
    
    def dialogo_cargar(self, titulo: str):
        self.dialogo.cargando(titulo)
        self.dialogo.show()  
    
    def customEvent(self, event):
        if isinstance(event, ActualizarChatEvent):
            self.actualizar_chat()
    
    def mostrarMensaje(self, mensaje: str):
        chat = self.usuario.buscar_chat(self.comboBoxDestinatario.currentText())
        chat.ingresar_mensaje(mensaje, True)
        
        QtCore.QCoreApplication.postEvent(self, ActualizarChatEvent())
    
    def conectar(self):
        
        if(self.lineEditNombreUsuario.text() == ""):
            self.dialogo.aviso("Error", "Ingrese un nombre de usuario")
            self.dialogo.show()
            return
        
        if(self.lineEditServer.text() == ""):
            self.dialogo.aviso("Error", "Ingrese un servidor")
            self.dialogo.show()
            return
        
        self.conexion = Conexion(self)
        self.dialogo_cargar("Conetando...")
        QtWidgets.QApplication.processEvents()  # Actualiza la interfaz de usuario
        
        if(not self.conexion.conectar(self.lineEditServer.text())):
            self.dialogo.aviso("Error", "No se pudo conectar al servidor")
            self.dialogo.show()
            self.conexion = None
            return
        else:
            self.dialogo.aviso("Conectado", "Conexión exitosa con el servidor")
            self.dialogo.show()
        
        self.pushButtonDesconectar.setVisible(True)
        self.pushButtonConectar.setVisible(False)
        
        self.lineEditNombreUsuario.setEnabled(False)
        self.lineEditServer.setEnabled(False)
            
        self.groupBoxDestinatario.setEnabled(True)
        self.groupBoxChat.setEnabled(True)
        self.groupBoxMensaje.setEnabled(True)
        
        self.usuario = Usuario(self.lineEditNombreUsuario.text())
        
        #Coloca el nombre de usuario
        self.conexion.setNombre(self.lineEditNombreUsuario.text())
        
        #Crea la cola
        if self.conexion.estaCanalUsado():
            self.dialogo.aviso("Error", "El canal ya esta en uso")
            self.dialogo.show()
            self.usuario = None
            self.conexion = None
            return  
        
        #Actualiza los usuarios
        self.actualizar_usuarios()

        #Coloca destinatario por defecto
        if self.comboBoxDestinatario.count() > 0:
            self.comboBoxDestinatario.setCurrentIndex(0)
            self.conexion.setDestinatario(self.comboBoxDestinatario.currentText())
            
            self.dialogo.aviso("Conectado", "Conectado en chat con " + self.comboBoxDestinatario.currentText())
        
        self.actualizar_chat()
        
    
    def cambio_destinatario(self):
        if self.conexion != None:
            self.conexion.setDestinatario(self.comboBoxDestinatario.currentText())
            self.dialogo.aviso("Conectado", "Conectado en chat con " + self.comboBoxDestinatario.currentText())
            self.dialogo.show()
        self.actualizar_chat()
    
    def actualizar_usuarios(self):
        usuarios = self.conexion.obtenerUsuarios()
        self.comboBoxDestinatario.addItems(usuarios)
        
    def desconectar(self):   
        self.pushButtonDesconectar.setVisible(False)
        self.pushButtonConectar.setVisible(True)
        
        self.lineEditNombreUsuario.setEnabled(True)
        self.lineEditServer.setEnabled(True)
            
        self.groupBoxDestinatario.setEnabled(False)
        self.groupBoxChat.setEnabled(False)
        self.groupBoxMensaje.setEnabled(False)
        
        self.conexion = Conexion(self)
        self.dialogo_cargar("Desconetando...")
        QtWidgets.QApplication.processEvents()  # Actualiza la interfaz de usuario
        
        if self.conexion != None:
            self.conexion.cerrarConexion()
            self.dialogo.aviso("Desconetado", "Conexión cerrada")
            self.dialogo.show()
        
        self.usuario = None
        self.conexion = None
        
        self.actualizar_chat()
        self.comboBoxDestinatario.clear()
        

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VentanaChat()
        myApp.show()
        app.exec()