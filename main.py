import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QLineEdit,QTextEdit

app=QApplication(sys.argv)
app.setStyleSheet('''
QPushButton{
background-color:skyblue;
color:white
}


''')

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello App')
        self.resize(400,200)

        layout=QVBoxLayout()
        self.setLayout(layout)

        self.textinput=QLineEdit()
        self.button=QPushButton('Click Me',clicked=self.sayHello)
        self.textoutput=QTextEdit()

        layout.addWidget(self.textinput)
        layout.addWidget(self.button)
        layout.addWidget(self.textoutput)

    def sayHello(self):
        input=self.textinput.text()
        self.textoutput.setText(f'Hello {input}')
        
window=MyApp()
window.show()

sys.exit(app.exec())