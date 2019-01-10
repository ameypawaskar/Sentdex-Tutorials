import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setGeometry(50,50,1000,1000)
window.setWindowTitle("PyQT Tuts!")

window.show()
