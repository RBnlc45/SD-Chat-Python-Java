import sys
from PyQt6 import QtWidgets
from MVC.vista.Vista import Ui_MainWindow

from MVC.modelo.Modelo import Usuario, Conexion

class VentanaChat(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super(VentanaChat, self).__init__(parent)
        self.setupUi(self)
        self.usuario = None
        self.conexion = None
        
        #Inavilitados
        self.desconectar()
        
        #Botones
        self.pushButtonDesconectar.clicked.connect(self.desconectar)
        self.pushButtonConectar.clicked.connect(self.conectar)
        self.pushButtonEnviar.clicked.connect(self.enviar)
        
    def enviar(self):
        chat = self.usuario.buscar_chat(self.comboBoxDestinatario.currentText(), self.lineEditServer.text())
        chat.ingresar_mensaje(self.textMensaje.toPlainText(), False)
        self.textMensaje.clear()
        
        self.actualizar_chat()
    
    def actualizar_chat(self):
        chat = self.usuario.buscar_chat(self.comboBoxDestinatario.currentText(), self.lineEditServer.text())
        self.cargar_mensajes_ui(chat.nombre, chat.mensajes)
        
    def conectar(self):
        self.pushButtonDesconectar.setVisible(True)
        self.pushButtonConectar.setVisible(False)
        
        self.lineEditNombreUsuario.setEnabled(False)
        self.lineEditServer.setEnabled(False)
            
        self.groupBoxDestinatario.setEnabled(True)
        self.groupBoxChat.setEnabled(True)
        self.groupBoxMensaje.setEnabled(True)
        
        self.usuario = Usuario(self.lineEditNombreUsuario.text(), self.lineEditServer.text())
        self.conexion = Conexion()
        
        self.actualizar_usuarios()
    
    def actualizar_usuarios(self):
        usuarios = [tupla[0] for tupla in self.conexion.listar_usuarios()]
        self.comboBoxDestinatario.addItems(usuarios)
        
    def desconectar(self):
        self.pushButtonDesconectar.setVisible(False)
        self.pushButtonConectar.setVisible(True)
        
        self.lineEditNombreUsuario.setEnabled(True)
        self.lineEditServer.setEnabled(True)
            
        self.groupBoxDestinatario.setEnabled(False)
        self.groupBoxChat.setEnabled(False)
        self.groupBoxMensaje.setEnabled(False)
            
        self.usuario = None
        self.conexion = None
        
        self.comboBoxDestinatario.clear()

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VentanaChat()
        myApp.show()
        app.exec()

if __name__ == "__main__":
    abrir()