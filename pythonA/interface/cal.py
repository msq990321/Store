import imp
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sys

main_wind = None

class Stat:
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/calc.ui')
        self.ui.calc.clicked.connect(self.Volcalc)
    
    def Volcalc(self):
        self.NO1 = int(self.ui.NO1.text())
        self.NO2 = int(self.ui.NO2.text())
        self.NO3 = int(self.ui.NO3.text())
        self.sum = self.NO1*10 + self.NO2*50 + self.NO3*100

        QtWidgets.QMessageBox.about(self.ui,
                            '计算结果',
                            f'''最终需要配置的培养基体积为：\n{self.sum}ml''')

app = QtWidgets.QApplication([])
app.setWindowIcon(QIcon('logo.png'))
stats = Stat()
stats.ui.show()
app.exec_()