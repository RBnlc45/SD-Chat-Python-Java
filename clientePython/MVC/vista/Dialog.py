# Form implementation generated from reading ui file '.\Dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog) -> None:
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 172)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.labelTitulo = QtWidgets.QLabel(Dialog)
        self.labelTitulo.setGeometry(QtCore.QRect(120, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelTexto = QtWidgets.QLabel(Dialog)
        self.labelTexto.setGeometry(QtCore.QRect(10, 50, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTexto.setFont(font)
        self.labelTexto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTexto.setObjectName("labelTexto")
        
        self.ImgCargando = QtWidgets.QLabel(Dialog)
        self.ImgCargando.setObjectName(u"ImgCargando")
        self.ImgCargando.setGeometry(QtCore.QRect(170, 60, 51, 51))
        
        self.animacion = QtGui.QMovie(u"./clientePython/MVC/vista/cargando.gif")
        
        self.ImgCargando.setMovie(self.animacion)
        self.ImgCargando.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog: QtWidgets.QDialog) -> None:
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aviso"))
        self.labelTitulo.setText(_translate("Dialog", "Aviso"))
        self.labelTexto.setText(_translate("Dialog", "Texto"))
        self.ImgCargando.setText(_translate("Dialog", ""))
    
    def aviso(self, titulo: str, texto: str) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.labelTitulo.setText(_translate("Dialog", titulo))
        self.labelTexto.setText(_translate("Dialog", texto))
        self.ImgCargando.setVisible(False)
    
    def cargando(self, titulo: str = "Cargando"):
        _translate = QtCore.QCoreApplication.translate
        self.labelTitulo.setText(_translate("Dialog", titulo))
        self.labelTexto.setText(_translate("Dialog", ""))
        self.ImgCargando.setVisible(True)
        self.animacion.start()
        
        