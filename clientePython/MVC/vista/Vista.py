# Form implementation generated from reading ui file '.\ChatWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        
        #Ventana
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 844)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        
        #Canva
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBoxUsuario = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUsuario.setGeometry(QtCore.QRect(10, 40, 691, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBoxUsuario.setFont(font)
        self.groupBoxUsuario.setObjectName("groupBoxUsuario")
        
        self.labelNombreUsuario = QtWidgets.QLabel(self.groupBoxUsuario)
        self.labelNombreUsuario.setGeometry(QtCore.QRect(140, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.labelNombreUsuario.setFont(font)
        self.labelNombreUsuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelNombreUsuario.setObjectName("labelNombreUsuario")
        
        self.labelServer = QtWidgets.QLabel(self.groupBoxUsuario)
        self.labelServer.setGeometry(QtCore.QRect(410, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.labelServer.setFont(font)
        self.labelServer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelServer.setObjectName("labelServer")
        
        self.lineEditNombreUsuario = QtWidgets.QLineEdit(self.groupBoxUsuario)
        self.lineEditNombreUsuario.setGeometry(QtCore.QRect(240, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.lineEditNombreUsuario.setFont(font)
        self.lineEditNombreUsuario.setObjectName("lineEditNombreUsuario")
        
        self.lineEditServer = QtWidgets.QLineEdit(self.groupBoxUsuario)
        self.lineEditServer.setGeometry(QtCore.QRect(510, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.lineEditServer.setFont(font)
        self.lineEditServer.setObjectName("lineEditServer")
        
        self.pushButtonConectar = QtWidgets.QPushButton(self.groupBoxUsuario)
        self.pushButtonConectar.setGeometry(QtCore.QRect(520, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.pushButtonConectar.setFont(font)
        self.pushButtonConectar.setObjectName("pushButtonConectar")
        self.pushButtonConectar.setVisible(True)
        
        self.pushButtonDesconectar = QtWidgets.QPushButton(self.groupBoxUsuario)
        self.pushButtonDesconectar.setGeometry(QtCore.QRect(520, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.pushButtonDesconectar.setFont(font)
        self.pushButtonDesconectar.setObjectName("pushButtonDesconectar")
        self.pushButtonDesconectar.setVisible(False)
        
        self.groupBoxDestinatario = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDestinatario.setGeometry(QtCore.QRect(10, 150, 691, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBoxDestinatario.setFont(font)
        self.groupBoxDestinatario.setStyleSheet("")
        self.groupBoxDestinatario.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBoxDestinatario.setObjectName("groupBoxDestinatario")
        
        self.labelNombreDestinatario = QtWidgets.QLabel(self.groupBoxDestinatario)
        self.labelNombreDestinatario.setGeometry(QtCore.QRect(270, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.labelNombreDestinatario.setFont(font)
        self.labelNombreDestinatario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelNombreDestinatario.setObjectName("labelNombreDestinatario")
        
        self.comboBoxDestinatario = QtWidgets.QComboBox(self.groupBoxDestinatario)
        self.comboBoxDestinatario.setGeometry(QtCore.QRect(380, 30, 271, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.comboBoxDestinatario.setFont(font)
        self.comboBoxDestinatario.setObjectName("comboBoxDestinatario")
        
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(240, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        
        self.groupBoxChat = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxChat.setGeometry(QtCore.QRect(10, 230, 691, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBoxChat.setFont(font)
        self.groupBoxChat.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBoxChat.setObjectName("groupBoxChat")  
        
        #Scroll Area
        self.scrollAreaChat = QtWidgets.QScrollArea(self.groupBoxChat)
        self.scrollAreaChat.setGeometry(QtCore.QRect(11, 31, 669, 204))
        self.scrollAreaChat.setMinimumSize(QtCore.QSize(669, 20))
        self.scrollAreaChat.setMaximumSize(QtCore.QSize(669, 409))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.scrollAreaChat.setFont(font)
        self.scrollAreaChat.setAutoFillBackground(False)
        self.scrollAreaChat.setStyleSheet("background-color: rgb(255, 255, 255);border: none;")
        self.scrollAreaChat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaChat.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollAreaChat.setWidgetResizable(True)
        self.scrollAreaChat.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollAreaChat.setObjectName("scrollAreaChat")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 204))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        #Layout vertical para el scroll area
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.scrollAreaChat.setWidget(self.scrollAreaWidgetContents)
        
        #Fondo del chat
        self.fondo = QtWidgets.QLabel(self.groupBoxChat)
        self.fondo.setGeometry(QtCore.QRect(10, 30, 671, 411))
        self.fondo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 0, 0);")
        self.fondo.setText("")
        self.fondo.setObjectName("Fondo")
        
        #Traemos el scroll area al frente
        self.scrollAreaChat.raise_()
        
        self.groupBoxMensaje = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxMensaje.setGeometry(QtCore.QRect(10, 680, 691, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBoxMensaje.setFont(font)
        self.groupBoxMensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBoxMensaje.setObjectName("groupBoxMensaje")
        
        self.textMensaje = QtWidgets.QTextEdit(self.groupBoxMensaje)
        self.textMensaje.setGeometry(QtCore.QRect(10, 30, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.textMensaje.setFont(font)
        self.textMensaje.setStyleSheet("padding: 4px;")
        self.textMensaje.setObjectName("textMensaje")
        
        self.pushButtonEnviar = QtWidgets.QPushButton(self.groupBoxMensaje)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(555, 30, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.pushButtonEnviar.setFont(font)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Cliente Python"))
        self.groupBoxUsuario.setTitle(_translate("MainWindow", "Datos Usuario"))
        self.labelNombreUsuario.setText(_translate("MainWindow", "Nombre:"))
        self.labelServer.setText(_translate("MainWindow", "Server IP:"))
        self.pushButtonConectar.setText(_translate("MainWindow", "Conectar"))
        self.pushButtonDesconectar.setText(_translate("MainWindow", "Desconectar"))
        self.groupBoxDestinatario.setTitle(_translate("MainWindow", "Datos Destinatario"))
        self.labelNombreDestinatario.setText(_translate("MainWindow", "Nombre:"))
        self.labelTitulo.setText(_translate("MainWindow", "Cliente Python"))
        self.groupBoxChat.setTitle(_translate("MainWindow", "Chat"))
        self.groupBoxMensaje.setTitle(_translate("MainWindow", "Mensaje"))
        self.pushButtonEnviar.setText(_translate("MainWindow", "Enviar"))

    def cargar_mensajes_ui(self, nombre_des: str, mensajes: list[tuple[str, bool]]):
        self.scrollAreaWidgetContents.setParent(None)
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        #Layout vertical para el scroll area
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.scrollAreaChat.setWidget(self.scrollAreaWidgetContents)
        
        _translate = QtCore.QCoreApplication.translate
        
        #Tamaño inicial vertical, borde superior e inferior
        tam_scroll_area = 8
        _max_caracteres = 42

        for tupla in mensajes:
            
            mensaje, es_recibido= tupla
            
            #Reestructura el mensaje para que se vea bien y calcula lineas extra
            inicio = 0
            fin = _max_caracteres
            
            nuevo_mensaje = ""
            
            while(fin < len(mensaje)):
                if("\n" in mensaje[inicio:fin]):
                    fin = mensaje.find("\n", inicio, fin)
                    nuevo_mensaje += mensaje[inicio:fin+2]
                    
                else:
                    nuevo_mensaje += mensaje[inicio:fin] + "\n"
                
                inicio = fin + 2
                fin = inicio + _max_caracteres
                
            if nuevo_mensaje:
                mensaje = nuevo_mensaje+mensaje[inicio:]
            
            cantidad_saltos = mensaje.count('\n')
        
            #Verifica el tamaño del mensaje para agregar mas lineas
            tam_group_box = 60 + (21 * cantidad_saltos)
            tam_label = 21 + (21 * cantidad_saltos)
        
            if es_recibido:
                
                self.groupBoxMsjDes = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.groupBoxMsjDes.setMinimumSize(QtCore.QSize(0, tam_group_box))
                self.groupBoxMsjDes.setMaximumSize(QtCore.QSize(400, tam_group_box))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                self.groupBoxMsjDes.setFont(font)
                self.groupBoxMsjDes.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
                self.groupBoxMsjDes.setStyleSheet("QGroupBox {border: 1px solid rgb(148, 148, 148);\n"
        "border-radius: 5px; \n"
        "margin-top: 0.5em;}\n"
        "QGroupBox::title {subcontrol-origin: margin;\n"
        "subcontrol-position: top left;\n"
        "padding: 0 3px;}")
                self.groupBoxMsjDes.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.groupBoxMsjDes.setObjectName("groupBoxMsjDes")
                
                self.labelDest = QtWidgets.QLabel(self.groupBoxMsjDes)
                self.labelDest.setGeometry(QtCore.QRect(10, 30, 381, tam_label))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setItalic(True)
                self.labelDest.setFont(font)
                self.labelDest.setStyleSheet("border: unset;")
                self.labelDest.setObjectName("labelDest")
                self.verticalLayout.addWidget(self.groupBoxMsjDes)
                
                self.groupBoxMsjDes.setTitle(_translate("MainWindow", nombre_des))
                self.labelDest.setText(_translate("MainWindow", mensaje))
                
            else:
                self.groupBoxMsjUsu = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.groupBoxMsjUsu.setMinimumSize(QtCore.QSize(0, tam_group_box))
                self.groupBoxMsjUsu.setMaximumSize(QtCore.QSize(400, tam_group_box))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                self.groupBoxMsjUsu.setFont(font)
                self.groupBoxMsjUsu.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
                self.groupBoxMsjUsu.setStyleSheet("QGroupBox {border: 1px solid rgb(148, 148, 148);\n"
        "border-radius: 5px; \n"
        "margin-top: 0.5em;}\n"
        "QGroupBox::title {subcontrol-origin: margin;\n"
        "subcontrol-position: top left;\n"
        "padding: 0 3px;}")
                self.groupBoxMsjUsu.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.groupBoxMsjUsu.setObjectName("groupBoxMsjUsu")
                
                self.labelUsu = QtWidgets.QLabel(self.groupBoxMsjUsu)
                self.labelUsu.setGeometry(QtCore.QRect(10, 30, 381, tam_label))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setItalic(True)
                self.labelUsu.setFont(font)
                self.labelUsu.setStyleSheet("border: none")
                self.labelUsu.setObjectName("labelUsu")
                self.verticalLayout.addWidget(self.groupBoxMsjUsu)
                
                self.groupBoxMsjUsu.setTitle(_translate("MainWindow", "Yo"))
                self.labelUsu.setText(_translate("MainWindow", mensaje))
        
        #Calcula tamaño y modifica el tamaño del scroll area
        
        self.scrollAreaChat.setGeometry(QtCore.QRect(11, 31, 669, 204))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 204))