# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_PageuHWtPU.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 646)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout1_grid = QGridLayout()
        self.layout1_grid.setObjectName(u"layout1_grid")
        self.layout1_grid.setContentsMargins(10, 10, 10, 10)
        self.label_h1sub = QLabel(self.page_1)
        self.label_h1sub.setObjectName(u"label_h1sub")
        self.label_h1sub.setStyleSheet(u"color: #666; font-size: 16px;")

        self.layout1_grid.addWidget(self.label_h1sub, 1, 0, 1, 1)

        self.label_h1 = QLabel(self.page_1)
        self.label_h1.setObjectName(u"label_h1")
        self.label_h1.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif;")

        self.layout1_grid.addWidget(self.label_h1, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.layout1_grid, 0, 1, 1, 1)

        self.layout5_horizontal = QHBoxLayout()
        self.layout5_horizontal.setObjectName(u"layout5_horizontal")
        self.layout5_horizontal.setContentsMargins(10, 10, 10, 10)
        self.tombol_batal = QPushButton(self.page_1)
        self.tombol_batal.setObjectName(u"tombol_batal")
        self.tombol_batal.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.tombol_batal.setStyleSheet(u"QPushButton#tombol_batal { height: 44px; padding: 0 24px; border: 1px solid; border-radius: 8px; background: rgba(229,231,235,0.8); color: rgb(31,41,55); font-size: 12pt; font-weight: 600; } QPushButton#tombol_batal:hover { background: rgba(209,213,219,0.8); } QPushButton#btn_batal.dark { background: rgba(55,65,81,0.5); color: rgb(229,231,235); } QPushButton#tombol_batal.dark:hover { background: rgba(75,85,99,0.5); }")

        self.layout5_horizontal.addWidget(self.tombol_batal)

        self.tombol_simpan = QPushButton(self.page_1)
        self.tombol_simpan.setObjectName(u"tombol_simpan")
        self.tombol_simpan.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.tombol_simpan.setStyleSheet(u"QPushButton#tombol_simpan { height: 44px; padding: 0 24px; border: 1px solid; border-radius: 8px; background: #7E99A3; color: black; font-size: 12pt; font-weight: 600; } QPushButton#tombol_simpan:hover { background: rgba(209,213,219,0.8); }")

        self.layout5_horizontal.addWidget(self.tombol_simpan)


        self.gridLayout_3.addLayout(self.layout5_horizontal, 4, 1, 1, 1)

        self.layout2_vertical = QVBoxLayout()
        self.layout2_vertical.setObjectName(u"layout2_vertical")
        self.layout2_vertical.setContentsMargins(10, 10, 10, 10)
        self.label_nama = QLabel(self.page_1)
        self.label_nama.setObjectName(u"label_nama")
        self.label_nama.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding-bottom: 5px;")

        self.layout2_vertical.addWidget(self.label_nama)

        self.input_nama = QLineEdit(self.page_1)
        self.input_nama.setObjectName(u"input_nama")
        self.input_nama.setStyleSheet(u"padding: 10px; font-size: 12pt;")

        self.layout2_vertical.addWidget(self.input_nama)


        self.gridLayout_3.addLayout(self.layout2_vertical, 1, 1, 1, 1)

        self.layout3_grid = QGridLayout()
        self.layout3_grid.setObjectName(u"layout3_grid")
        self.layout3_grid.setHorizontalSpacing(10)
        self.layout3_grid.setVerticalSpacing(6)
        self.layout3_grid.setContentsMargins(10, 10, 10, 10)
        self.satuan_label = QLabel(self.page_1)
        self.satuan_label.setObjectName(u"satuan_label")
        self.satuan_label.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px;")

        self.layout3_grid.addWidget(self.satuan_label, 0, 1, 1, 1)

        self.jumlah_label = QLabel(self.page_1)
        self.jumlah_label.setObjectName(u"jumlah_label")
        self.jumlah_label.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px;")

        self.layout3_grid.addWidget(self.jumlah_label, 0, 0, 1, 1)

        self.jumlah_input = QLineEdit(self.page_1)
        self.jumlah_input.setObjectName(u"jumlah_input")
        self.jumlah_input.setStyleSheet(u"padding: 10px; font-size: 12pt;")

        self.layout3_grid.addWidget(self.jumlah_input, 1, 0, 1, 1)

        self.tanggal_label = QLabel(self.page_1)
        self.tanggal_label.setObjectName(u"tanggal_label")
        self.tanggal_label.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px; margin-top: 5px;")

        self.layout3_grid.addWidget(self.tanggal_label, 2, 0, 1, 1)

        self.expire_label = QLabel(self.page_1)
        self.expire_label.setObjectName(u"expire_label")
        self.expire_label.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px; margin-top: 5px;")

        self.layout3_grid.addWidget(self.expire_label, 2, 1, 1, 1)

        self.satuan_combo = QComboBox(self.page_1)
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.setObjectName(u"satuan_combo")
        self.satuan_combo.setStyleSheet(u"padding: 10px; font-size: 12pt;")

        self.layout3_grid.addWidget(self.satuan_combo, 1, 1, 1, 1)

        self.tanggal_date = QDateEdit(self.page_1)
        self.tanggal_date.setObjectName(u"tanggal_date")
        self.tanggal_date.setStyleSheet(u"padding: 10px; font-size: 12pt;")
        self.tanggal_date.setReadOnly(False)
        self.tanggal_date.setMaximumDate(QDate(9999, 11, 30))
        self.tanggal_date.setDate(QDate(2025, 1, 12))

        self.layout3_grid.addWidget(self.tanggal_date, 3, 0, 1, 1)

        self.expire_date = QDateEdit(self.page_1)
        self.expire_date.setObjectName(u"expire_date")
        self.expire_date.setStyleSheet(u"padding: 10px; font-size: 12pt;")
        self.expire_date.setDate(QDate(2025, 1, 12))

        self.layout3_grid.addWidget(self.expire_date, 3, 1, 1, 1)

        self.layout3_grid.setColumnStretch(0, 1)
        self.layout3_grid.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.layout3_grid, 2, 1, 1, 1)

        self.layout4_grid = QGridLayout()
        self.layout4_grid.setObjectName(u"layout4_grid")
        self.layout4_grid.setContentsMargins(10, 10, 10, 10)
        self.radio_lainnya = QRadioButton(self.page_1)
        self.radio_lainnya.setObjectName(u"radio_lainnya")
        self.radio_lainnya.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_lainnya, 2, 2, 1, 1)

        self.radio_susu = QRadioButton(self.page_1)
        self.radio_susu.setObjectName(u"radio_susu")
        self.radio_susu.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_susu, 2, 0, 1, 1)

        self.radio_roti = QRadioButton(self.page_1)
        self.radio_roti.setObjectName(u"radio_roti")
        self.radio_roti.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_roti, 2, 1, 1, 1)

        self.radio_daging = QRadioButton(self.page_1)
        self.radio_daging.setObjectName(u"radio_daging")
        self.radio_daging.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_daging, 1, 0, 1, 1)

        self.radio_buah = QRadioButton(self.page_1)
        self.radio_buah.setObjectName(u"radio_buah")
        self.radio_buah.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_buah, 1, 2, 1, 1)

        self.radio_sayuran = QRadioButton(self.page_1)
        self.radio_sayuran.setObjectName(u"radio_sayuran")
        self.radio_sayuran.setStyleSheet(u"border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font family: Inter, sans-serif; margin: 5px; padding: 10px;")

        self.layout4_grid.addWidget(self.radio_sayuran, 1, 1, 1, 1)

        self.label_kategori = QLabel(self.page_1)
        self.label_kategori.setObjectName(u"label_kategori")
        self.label_kategori.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px;")

        self.layout4_grid.addWidget(self.label_kategori, 0, 0, 1, 3)


        self.gridLayout_3.addLayout(self.layout4_grid, 3, 1, 1, 1)

        self.sidebar_frame_1 = QFrame(self.page_1)
        self.sidebar_frame_1.setObjectName(u"sidebar_frame_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame_1.sizePolicy().hasHeightForWidth())
        self.sidebar_frame_1.setSizePolicy(sizePolicy)
        self.sidebar_frame_1.setStyleSheet(u"QFrame#sidebar_frame_1 { border: 1px solid; border-radius: 5px; border-color: LightGray; }")
        self.verticalLayout = QVBoxLayout(self.sidebar_frame_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.label_10 = QLabel(self.sidebar_frame_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; font-weight: bold; padding: 10px 10px 0px 10px;")

        self.verticalLayout.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_8 = QPushButton(self.sidebar_frame_1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.sidebar_frame_1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.sidebar_frame_1)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addWidget(self.sidebar_frame_1, 0, 0, 5, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.head = QLabel(self.page_2)
        self.head.setObjectName(u"head")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.head.sizePolicy().hasHeightForWidth())
        self.head.setSizePolicy(sizePolicy1)
        self.head.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif; margin: 10px;")

        self.verticalLayout_2.addWidget(self.head)

        self.headsub = QLabel(self.page_2)
        self.headsub.setObjectName(u"headsub")
        sizePolicy1.setHeightForWidth(self.headsub.sizePolicy().hasHeightForWidth())
        self.headsub.setSizePolicy(sizePolicy1)
        self.headsub.setStyleSheet(u"color: #666; font-size: 16px; margin: 10px;")

        self.verticalLayout_2.addWidget(self.headsub)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame { border: 1px solid; border-radius: 5px; border-color: LightGray; }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.label_2, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-Serif; padding: 10px; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 0px 5px 0px 5px; padding: 10px 0px 0px 0px;")

        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-Serif; padding: 10px; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.lineEdit, 5, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 20px 5px 10px 5px;")

        self.gridLayout_5.addWidget(self.pushButton_3, 6, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 20px 5px 10px 5px;")

        self.gridLayout_5.addWidget(self.pushButton_4, 6, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 0px 5px 0px 5px")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 2)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 0px 5px 0px 5px;")

        self.gridLayout_5.addWidget(self.dateEdit, 5, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalFrame = QFrame(self.page_2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"QFrame#verticalFrame { border: 1px solid; border-radius: 5px; border-color: lightgray; }")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.label_11 = QLabel(self.verticalFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; font-weight: bold; padding: 10px 10px 0px 10px;")

        self.verticalLayout_4.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_11 = QPushButton(self.verticalFrame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.verticalFrame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.verticalFrame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.pushButton_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.gridLayout_4.addWidget(self.verticalFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_8 = QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 26px; font-weight: bold; padding: 5px 10px 5px 10px;")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 16px; font-color: gray; padding: 5px 10px 5px 10px;")

        self.verticalLayout_7.addWidget(self.label_6)

        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame#frame_2 { border: 1px solid; border-color: lightgray; border-radius: 5px; }")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"padding: 10px; margin: 5px;")

        self.gridLayout_10.addWidget(self.tableView, 1, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.radioButton_2, 1, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet(u"font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.label_8, 0, 1, 1, 3)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.radioButton, 1, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.frame_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.radioButton_3, 1, 3, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.gridLayout_8.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalFrame_2 = QFrame(self.page_3)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setStyleSheet(u"QFrame#verticalFrame_2 { border: 1px solid; border-radius: 5px; border-color: lightgray; }")
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(8, 8, 8, 8)
        self.label_9 = QLabel(self.verticalFrame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; font-weight: bold; padding: 10px 10px 0px 10px;")

        self.verticalLayout_5.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_5 = QPushButton(self.verticalFrame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalFrame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.verticalFrame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_7.addWidget(self.verticalFrame_2, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_h1sub.setText(QCoreApplication.translate("MainWindow", u"Tambahkan item baru untuk memantau tanggal kedaluarsa", None))
        self.label_h1.setText(QCoreApplication.translate("MainWindow", u"Input Bahan Makanan", None))
        self.tombol_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.tombol_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.label_nama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.input_nama.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: Daging Sapi", None))
        self.satuan_label.setText(QCoreApplication.translate("MainWindow", u"Satuan", None))
        self.jumlah_label.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None))
        self.jumlah_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: 500", None))
        self.tanggal_label.setText(QCoreApplication.translate("MainWindow", u"Tanggal Pembelian", None))
        self.expire_label.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.satuan_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"gram", None))
        self.satuan_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"kg", None))
        self.satuan_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"pcs", None))
        self.satuan_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"ml", None))
        self.satuan_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"liter", None))

        self.radio_lainnya.setText(QCoreApplication.translate("MainWindow", u"Lainnya", None))
        self.radio_susu.setText(QCoreApplication.translate("MainWindow", u"Susu", None))
        self.radio_roti.setText(QCoreApplication.translate("MainWindow", u"Roti", None))
        self.radio_daging.setText(QCoreApplication.translate("MainWindow", u"Daging", None))
        self.radio_buah.setText(QCoreApplication.translate("MainWindow", u"Buah", None))
        self.radio_sayuran.setText(QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.label_kategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fauzi", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
        self.head.setText(QCoreApplication.translate("MainWindow", u"Transaksi Bahan Makanan", None))
        self.headsub.setText(QCoreApplication.translate("MainWindow", u"Isi form di bawah untuk mencatat transaksi bahan makanan", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi (kg)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Jenis Transaksi", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Masuk", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fauzi", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Laporan Kedaluwarsa", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pantau dan kelola bahan makanan yang akan kedaluwarsa", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fauzi", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
    # retranslateUi

