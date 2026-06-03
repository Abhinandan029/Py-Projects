import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTimer, QTime

class digital_clock(QWidget) : 
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 400, 500, 300)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.setStyleSheet("""
                    font-size : 200px;
                    background-color : black;
                    color : white;
        """)
        
        font_id = QFontDatabase.addApplicationFont("project_stuff/DS-DIGII.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        
        

def main() :
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec_())
    
    
       
if __name__ == '__main__'   :      
    main()
    