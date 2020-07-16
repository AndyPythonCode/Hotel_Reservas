import sys
from Hotel import *
from PyQt5.QtWidgets import QApplication, QWidget

class appHotel(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItem("Individual")
        self.comboBox.addItem("Doble")
        self.comboBox.addItem("Triple")

        self.pushButton.clicked.connect(self.calcular)

        self.show()
    
    def calcular(self):
        fecha = self.calendarWidget.selectedDate().toPyDate()
        dias = self.spinBox.value()
        habitacion = self.comboBox.itemText(self.comboBox.currentIndex())
        self.label_4.setText(f"«Fecha: {fecha}» «Dias: {dias}» «Habitacion: {habitacion}»")

        costo = 0
        if habitacion == "Individual":
            costo = 10
        elif habitacion =="Doble":
            costo = 20
        elif habitacion == "Triple":
            costo = 30
        
        self.label_5.setText(f"««Total {costo*dias}»»")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = appHotel()
    sys.exit(app.exec_())