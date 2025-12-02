from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            
        MainWindow.resize(427, 620)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.layout_1_v = QVBoxLayout()
        self.layout_1_v.setObjectName("layout_1_v")
        self.layout_1_v.setContentsMargins(10, 10, 10, 10)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        
        self.layout_1_v.addWidget(self.label)
        
        self.verticalLayout.addLayout(self.layout_1_v)
        
        self.layout_2_v = QVBoxLayout()
        self.layout_2_v.setObjectName("layout_2_v")
        self.layout_2_v.setContentsMargins(10, 10, 10, 10)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("""
            font-size: 12pt;\n"
            font-family: Inter, sans-serif;\n"
            padding-bottom: 5px;
        """)

        self.layout_2_v.addWidget(self.label_2)
        
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("padding: 10px; font-size: 12pt;")