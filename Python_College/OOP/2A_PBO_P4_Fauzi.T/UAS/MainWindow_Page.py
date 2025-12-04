# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_PagembHohY.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(684, 664)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.p12_heading = QFrame(self.page_1)
        self.p12_heading.setObjectName(u"p12_heading")
        self.layout1_grid = QGridLayout(self.p12_heading)
        self.layout1_grid.setObjectName(u"layout1_grid")
        self.layout1_grid.setContentsMargins(10, 10, 10, 10)
        self.label_h1sub = QLabel(self.p12_heading)
        self.label_h1sub.setObjectName(u"label_h1sub")
        self.label_h1sub.setStyleSheet(u"color: #666; font-size: 16px;")

        self.layout1_grid.addWidget(self.label_h1sub, 1, 0, 1, 1)

        self.label_h1 = QLabel(self.p12_heading)
        self.label_h1.setObjectName(u"label_h1")
        self.label_h1.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif;")

        self.layout1_grid.addWidget(self.label_h1, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.p12_heading, 0, 1, 1, 1)

        self.p13_nama = QFrame(self.page_1)
        self.p13_nama.setObjectName(u"p13_nama")
        self.p13_nama.setStyleSheet(u"QLabel { font-size: 12pt; font-family: Inter, sans-serif; padding-bottom: 5px; } QLineEdit { padding: 10px; font-size: 12pt; }")
        self.layout2_vertical = QVBoxLayout(self.p13_nama)
        self.layout2_vertical.setObjectName(u"layout2_vertical")
        self.layout2_vertical.setContentsMargins(10, 10, 10, 10)
        self.label_nama = QLabel(self.p13_nama)
        self.label_nama.setObjectName(u"label_nama")
        self.label_nama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.label_nama)

        self.input_nama = QLineEdit(self.p13_nama)
        self.input_nama.setObjectName(u"input_nama")
        self.input_nama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.input_nama)


        self.gridLayout_3.addWidget(self.p13_nama, 1, 1, 1, 1)

        self.p15_kategori = QFrame(self.page_1)
        self.p15_kategori.setObjectName(u"p15_kategori")
        self.p15_kategori.setStyleSheet(u"QLabel { font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px; } QRadioButton { border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 5px; padding: 10px; }")
        self.layout4_grid = QGridLayout(self.p15_kategori)
        self.layout4_grid.setObjectName(u"layout4_grid")
        self.layout4_grid.setContentsMargins(10, 10, 10, 10)
        self.radio_sayuran = QRadioButton(self.p15_kategori)
        self.radio_sayuran.setObjectName(u"radio_sayuran")
        self.radio_sayuran.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_sayuran.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_sayuran, 1, 1, 1, 1)

        self.label_kategori = QLabel(self.p15_kategori)
        self.label_kategori.setObjectName(u"label_kategori")
        self.label_kategori.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.label_kategori, 0, 0, 1, 3)

        self.radio_roti = QRadioButton(self.p15_kategori)
        self.radio_roti.setObjectName(u"radio_roti")
        self.radio_roti.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_roti.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_roti, 2, 1, 1, 1)

        self.radio_lainnya = QRadioButton(self.p15_kategori)
        self.radio_lainnya.setObjectName(u"radio_lainnya")
        self.radio_lainnya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_lainnya.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_lainnya, 2, 2, 1, 1)

        self.radio_daging = QRadioButton(self.p15_kategori)
        self.radio_daging.setObjectName(u"radio_daging")
        self.radio_daging.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_daging.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_daging, 1, 0, 1, 1)

        self.radio_susu = QRadioButton(self.p15_kategori)
        self.radio_susu.setObjectName(u"radio_susu")
        self.radio_susu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_susu.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_susu, 2, 0, 1, 1)

        self.radio_buah = QRadioButton(self.p15_kategori)
        self.radio_buah.setObjectName(u"radio_buah")
        self.radio_buah.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_buah.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.radio_buah, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.p15_kategori, 3, 1, 1, 1)

        self.p16_tombol = QFrame(self.page_1)
        self.p16_tombol.setObjectName(u"p16_tombol")
        self.p16_tombol.setStyleSheet(u"QPushButton { border: 1px solid; border-radius: 5px; font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 10px; padding: 10px; }")
        self.layout5_horizontal = QHBoxLayout(self.p16_tombol)
        self.layout5_horizontal.setObjectName(u"layout5_horizontal")
        self.layout5_horizontal.setContentsMargins(10, 10, 10, 10)
        self.tombol_batal = QPushButton(self.p16_tombol)
        self.tombol_batal.setObjectName(u"tombol_batal")
        self.tombol_batal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tombol_batal.setStyleSheet(u"")

        self.layout5_horizontal.addWidget(self.tombol_batal)

        self.tombol_simpan = QPushButton(self.p16_tombol)
        self.tombol_simpan.setObjectName(u"tombol_simpan")
        self.tombol_simpan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tombol_simpan.setStyleSheet(u"")

        self.layout5_horizontal.addWidget(self.tombol_simpan)


        self.gridLayout_3.addWidget(self.p16_tombol, 4, 1, 1, 1)

        self.p14_input = QFrame(self.page_1)
        self.p14_input.setObjectName(u"p14_input")
        self.p14_input.setStyleSheet(u"QLabel { font-size: 12pt; font-family: Helvetica, Inter, sans-serif; } QLineEdit,QComboBox,QDateEdit { font-size: 12pt; padding: 10px; }")
        self.layout3_grid = QGridLayout(self.p14_input)
        self.layout3_grid.setObjectName(u"layout3_grid")
        self.layout3_grid.setHorizontalSpacing(10)
        self.layout3_grid.setVerticalSpacing(6)
        self.layout3_grid.setContentsMargins(10, 10, 10, 10)
        self.satuan_label = QLabel(self.p14_input)
        self.satuan_label.setObjectName(u"satuan_label")
        self.satuan_label.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.satuan_label, 0, 1, 1, 1)

        self.jumlah_label = QLabel(self.p14_input)
        self.jumlah_label.setObjectName(u"jumlah_label")
        self.jumlah_label.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.jumlah_label, 0, 0, 1, 1)

        self.jumlah_input = QLineEdit(self.p14_input)
        self.jumlah_input.setObjectName(u"jumlah_input")
        self.jumlah_input.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.jumlah_input, 1, 0, 1, 1)

        self.tanggal_label = QLabel(self.p14_input)
        self.tanggal_label.setObjectName(u"tanggal_label")
        self.tanggal_label.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.tanggal_label, 2, 0, 1, 1)

        self.expire_label = QLabel(self.p14_input)
        self.expire_label.setObjectName(u"expire_label")
        self.expire_label.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.expire_label, 2, 1, 1, 1)

        self.satuan_combo = QComboBox(self.p14_input)
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.setObjectName(u"satuan_combo")
        self.satuan_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.satuan_combo.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.satuan_combo, 1, 1, 1, 1)

        self.tanggal_date = QDateEdit(self.p14_input)
        self.tanggal_date.setObjectName(u"tanggal_date")
        self.tanggal_date.setStyleSheet(u"")
        self.tanggal_date.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.tanggal_date.setReadOnly(False)
        self.tanggal_date.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.tanggal_date.setMaximumDate(QDate(9999, 11, 30))
        self.tanggal_date.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.tanggal_date, 3, 0, 1, 1)

        self.expire_date = QDateEdit(self.p14_input)
        self.expire_date.setObjectName(u"expire_date")
        self.expire_date.setStyleSheet(u"")
        self.expire_date.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.expire_date.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.expire_date.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.expire_date, 3, 1, 1, 1)

        self.layout3_grid.setColumnStretch(0, 1)
        self.layout3_grid.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.p14_input, 2, 1, 1, 1)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.p32_transaksi = QFrame(self.page_2)
        self.p32_transaksi.setObjectName(u"p32_transaksi")
        self.p32_transaksi.setStyleSheet(u"QFrame#p32_transaksi { border: 1px solid; border-color: lightgray; border-radius: 5px; padding: 20px 10px 20px 10px; } QPushButton { border: 1px solid; border-radius: 5px; font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 10px; padding: 10px; } QPushButton:hover { background-color: AntiqueWhite; } QPushButton:pressed { background-color: Bisque; } QLabel { font-family: Helvetica, Inter, sans-serif; font-size: 12pt; }")
        self.gridLayout_6 = QGridLayout(self.p32_transaksi)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.p32_transaksi)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_9, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.p32_transaksi)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.pushButton_2.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.dateEdit = QDateEdit(self.p32_transaksi)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px;")
        self.dateEdit.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.dateEdit.setDateTime(QDateTime(QDate(2025, 11, 30), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.dateEdit, 5, 1, 1, 1)

        self.label_4 = QLabel(self.p32_transaksi)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 2)

        self.label_10 = QLabel(self.p32_transaksi)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_10, 4, 1, 1, 1)

        self.lineEdit = QLineEdit(self.p32_transaksi)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px;")

        self.gridLayout_6.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.p32_transaksi)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.pushButton_3, 6, 1, 1, 1)

        self.pushButton = QPushButton(self.p32_transaksi)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.p32_transaksi)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.pushButton_4, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.p32_transaksi)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px;")

        self.gridLayout_6.addWidget(self.lineEdit_2, 5, 0, 1, 1)

        self.label_3 = QLabel(self.p32_transaksi)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 2)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)

        self.gridLayout_4.addWidget(self.p32_transaksi, 3, 0, 1, 1)

        self.p31_heading = QFrame(self.page_2)
        self.p31_heading.setObjectName(u"p31_heading")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p31_heading.sizePolicy().hasHeightForWidth())
        self.p31_heading.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.p31_heading)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.p31_heading)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif;")

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.p31_heading)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"color: #666; font-size: 16px;")

        self.verticalLayout_5.addWidget(self.label_2)


        self.gridLayout_4.addWidget(self.p31_heading, 2, 0, 1, 1)

        self.vspacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.vspacer2, 4, 0, 1, 1)

        self.pages.addWidget(self.page_2)
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
        self.label_6.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 16px; color: gray; padding: 5px 10px 5px 10px;")

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
        self.tableView.setStyleSheet(u"font-family: Helvetica, Inter, sans-serif; font-size: 12pt;")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setWordWrap(False)

        self.gridLayout_10.addWidget(self.tableView, 1, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.radioButton_2, 1, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)
        self.comboBox_2.setStyleSheet(u"font-size: 12pt; margin: 5px; padding: 5px;")

        self.gridLayout_9.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
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


        self.gridLayout_8.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.pages.addWidget(self.page_3)

        self.gridLayout.addWidget(self.pages, 0, 1, 1, 1)

        self.base_sidebar = QFrame(self.centralwidget)
        self.base_sidebar.setObjectName(u"base_sidebar")
        sizePolicy2.setHeightForWidth(self.base_sidebar.sizePolicy().hasHeightForWidth())
        self.base_sidebar.setSizePolicy(sizePolicy2)
        self.base_sidebar.setStyleSheet(u"QFrame#base_sidebar { border: 1px solid; border-radius: 5px; border-color: LightGray; } QLabel { font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; font-weight: bold; padding: 10px 10px 10px 10px; } QPushButton { font-family: Helvetica, Inter, Sans-serif; padding: 10px; margin: 5px; font-size: 12pt; }")
        self.verticalLayout = QVBoxLayout(self.base_sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.foto_profil = QFrame(self.base_sidebar)
        self.foto_profil.setObjectName(u"foto_profil")
        self.horizontalLayout = QHBoxLayout(self.foto_profil)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_profil = QLabel(self.foto_profil)
        self.label_profil.setObjectName(u"label_profil")
        self.label_profil.setMaximumSize(QSize(32, 32))
        self.label_profil.setStyleSheet(u"margin: 0px 0px 0px 0px; padding: 0px 2px 0px 0px;")
        self.label_profil.setPixmap(QPixmap(u"Python_College/OOP/2A_PBO_P4_Fauzi.T/UAS/Assets/user.png"))
        self.label_profil.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_profil)

        self.label_profilnama = QLabel(self.foto_profil)
        self.label_profilnama.setObjectName(u"label_profilnama")
        self.label_profilnama.setStyleSheet(u"margin: 0px 0px 0px 0px; padding: 0px 0px 0px 2px;")

        self.horizontalLayout.addWidget(self.label_profilnama, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.foto_profil, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.side_input = QPushButton(self.base_sidebar)
        self.side_input.setObjectName(u"side_input")
        self.side_input.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_input.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.side_input)

        self.side_transaksi = QPushButton(self.base_sidebar)
        self.side_transaksi.setObjectName(u"side_transaksi")
        self.side_transaksi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_transaksi.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.side_transaksi)

        self.side_laporan = QPushButton(self.base_sidebar)
        self.side_laporan.setObjectName(u"side_laporan")
        self.side_laporan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_laporan.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.side_laporan)

        self.vspacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.vspacer1)


        self.gridLayout.addWidget(self.base_sidebar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_h1sub.setText(QCoreApplication.translate("MainWindow", u"Tambahkan item baru untuk memantau tanggal kedaluarsa", None))
        self.label_h1.setText(QCoreApplication.translate("MainWindow", u"Input Bahan Makanan", None))
        self.label_nama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.input_nama.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: Daging Sapi", None))
        self.radio_sayuran.setText(QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.label_kategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.radio_roti.setText(QCoreApplication.translate("MainWindow", u"Roti", None))
        self.radio_lainnya.setText(QCoreApplication.translate("MainWindow", u"Lainnya", None))
        self.radio_daging.setText(QCoreApplication.translate("MainWindow", u"Daging", None))
        self.radio_susu.setText(QCoreApplication.translate("MainWindow", u"Susu", None))
        self.radio_buah.setText(QCoreApplication.translate("MainWindow", u"Buah", None))
        self.tombol_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.tombol_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
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

        self.tanggal_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMMM yyyy", None))
        self.expire_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMMM yyyy", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd MMMM yyyy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jenis Transaksi", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Proses Transaksi", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Masuk", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset Form", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Transaksi Bahan Makanan Baru", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Isi form di bawah untuk mencatat bahan makanan", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Laporan Kedaluwarsa", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pantau dan kelola bahan makanan yang akan kedaluwarsa", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_profil.setText("")
        self.label_profilnama.setText(QCoreApplication.translate("MainWindow", u"Profil", None))
        self.side_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.side_transaksi.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.side_laporan.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
    # retranslateUi

