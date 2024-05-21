from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUi
import sys
import requests

def translate(text, source_language, target_language):
    if text == "":
        return ""
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language}&tl={target_language}&dt=t&q={text}"
    response = requests.get(url)
    result = response.json()[0][0][0]
    return result

class translate_w(QMainWindow):
    def __init__(self):
        super(translate_w, self).__init__()
        uic.loadUi('translate.ui', self)
        self.trans_b.clicked.connect(self.handle_translation)
        
    def handle_translation(self):
        _from = self.From.toPlainText()
        _to = translate(_from, 'en', 'vi')
        self.To.setText(_to)

# App execution
app = QApplication(sys.argv) 
widget = QtWidgets.QStackedWidget() 
translate_f = translate_w()
widget.addWidget(translate_f)
widget.setCurrentIndex(0)
widget.setWindowTitle("Google Translate")
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
app.exec()
