import sys
from PyQt6 import QtWidgets
from ChatWindow import Ui_MainWindow

class VentanaChat(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super(VentanaChat, self).__init__(parent)
        self.setupUi(self)
        
        #Botones
        self.btnEnviar.clicked.connect(self.enviar)
        
        def enviar():
            pass

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VentanaChat()
        myApp.show()
        app.exec()

if __name__ == "__main__":
    abrir()