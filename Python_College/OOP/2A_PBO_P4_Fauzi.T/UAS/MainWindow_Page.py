# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_PageDryzvk.ui'
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
        self.label_headsub = QLabel(self.p12_heading)
        self.label_headsub.setObjectName(u"label_headsub")
        self.label_headsub.setStyleSheet(u"color: #666; font-size: 16px;")

        self.layout1_grid.addWidget(self.label_headsub, 1, 0, 1, 1)

        self.label_head = QLabel(self.p12_heading)
        self.label_head.setObjectName(u"label_head")
        self.label_head.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif;")

        self.layout1_grid.addWidget(self.label_head, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.p12_heading, 0, 1, 1, 1)

        self.p13_nama = QFrame(self.page_1)
        self.p13_nama.setObjectName(u"p13_nama")
        self.p13_nama.setStyleSheet(u"QLabel { font-size: 12pt; font-family: Inter, sans-serif; padding-bottom: 5px; } QLineEdit { padding: 10px; font-size: 12pt; }")
        self.layout2_vertical = QVBoxLayout(self.p13_nama)
        self.layout2_vertical.setObjectName(u"layout2_vertical")
        self.layout2_vertical.setContentsMargins(10, 10, 10, 10)
        self.p13_01_labelnama = QLabel(self.p13_nama)
        self.p13_01_labelnama.setObjectName(u"p13_01_labelnama")
        self.p13_01_labelnama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.p13_01_labelnama)

        self.p13_02_inputnama = QLineEdit(self.p13_nama)
        self.p13_02_inputnama.setObjectName(u"p13_02_inputnama")
        self.p13_02_inputnama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.p13_02_inputnama)


        self.gridLayout_3.addWidget(self.p13_nama, 1, 1, 1, 1)

        self.p15_kategori = QFrame(self.page_1)
        self.p15_kategori.setObjectName(u"p15_kategori")
        self.p15_kategori.setStyleSheet(u"QLabel { font-size: 12pt; font-family: Inter, sans-serif; margin-bottom: 5px; } QRadioButton { border: 1px solid; border-color: lightgray; border-radius: 5px; font-size: 12pt; font-family: Helvetica, Inter, Sans-serif; margin: 5px; padding: 10px; }")
        self.layout4_grid = QGridLayout(self.p15_kategori)
        self.layout4_grid.setObjectName(u"layout4_grid")
        self.layout4_grid.setContentsMargins(10, 10, 10, 10)
        self.p15_03_radiosayuran = QRadioButton(self.p15_kategori)
        self.p15_03_radiosayuran.setObjectName(u"p15_03_radiosayuran")
        self.p15_03_radiosayuran.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_03_radiosayuran.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_03_radiosayuran, 1, 1, 1, 1)

        self.p15_01_labelkategori = QLabel(self.p15_kategori)
        self.p15_01_labelkategori.setObjectName(u"p15_01_labelkategori")
        self.p15_01_labelkategori.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_01_labelkategori, 0, 0, 1, 3)

        self.p15_06_radioroti = QRadioButton(self.p15_kategori)
        self.p15_06_radioroti.setObjectName(u"p15_06_radioroti")
        self.p15_06_radioroti.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_06_radioroti.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_06_radioroti, 2, 1, 1, 1)

        self.p15_07_radiolainnya = QRadioButton(self.p15_kategori)
        self.p15_07_radiolainnya.setObjectName(u"p15_07_radiolainnya")
        self.p15_07_radiolainnya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_07_radiolainnya.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_07_radiolainnya, 2, 2, 1, 1)

        self.p15_02_radiodaging = QRadioButton(self.p15_kategori)
        self.p15_02_radiodaging.setObjectName(u"p15_02_radiodaging")
        self.p15_02_radiodaging.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_02_radiodaging.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_02_radiodaging, 1, 0, 1, 1)

        self.p15_05_radiosusu = QRadioButton(self.p15_kategori)
        self.p15_05_radiosusu.setObjectName(u"p15_05_radiosusu")
        self.p15_05_radiosusu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_05_radiosusu.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_05_radiosusu, 2, 0, 1, 1)

        self.p15_04_radiobuah = QRadioButton(self.p15_kategori)
        self.p15_04_radiobuah.setObjectName(u"p15_04_radiobuah")
        self.p15_04_radiobuah.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15_04_radiobuah.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15_04_radiobuah, 1, 2, 1, 1)


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
        self.tombol_batal.setStyleSheet(u"QPushButton#tombol_batal { background-color: hsl(30, 27%, 91%); } QPushButton#tombol_batal:hover { background-color: hsl(30, 27%, 81%); }")

        self.layout5_horizontal.addWidget(self.tombol_batal)

        self.tombol_simpan = QPushButton(self.p16_tombol)
        self.tombol_simpan.setObjectName(u"tombol_simpan")
        self.tombol_simpan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tombol_simpan.setStyleSheet(u"QPushButton#tombol_simpan { background-color: hsl(33, 29%, 70%); } QPushButton#tombol_simpan:hover { background-color: hsl(27, 19%, 82%); }")

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
        self.p14_03_labelsatuan = QLabel(self.p14_input)
        self.p14_03_labelsatuan.setObjectName(u"p14_03_labelsatuan")
        self.p14_03_labelsatuan.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_03_labelsatuan, 0, 1, 1, 1)

        self.p14_01_labeljumlah = QLabel(self.p14_input)
        self.p14_01_labeljumlah.setObjectName(u"p14_01_labeljumlah")
        self.p14_01_labeljumlah.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_01_labeljumlah, 0, 0, 1, 1)

        self.p14_02_inputjumlah = QLineEdit(self.p14_input)
        self.p14_02_inputjumlah.setObjectName(u"p14_02_inputjumlah")
        self.p14_02_inputjumlah.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_02_inputjumlah, 1, 0, 1, 1)

        self.p14_05_labeltanggal = QLabel(self.p14_input)
        self.p14_05_labeltanggal.setObjectName(u"p14_05_labeltanggal")
        self.p14_05_labeltanggal.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_05_labeltanggal, 2, 0, 1, 1)

        self.p14_07_labelexpire = QLabel(self.p14_input)
        self.p14_07_labelexpire.setObjectName(u"p14_07_labelexpire")
        self.p14_07_labelexpire.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_07_labelexpire, 2, 1, 1, 1)

        self.p14_04_combosatuan = QComboBox(self.p14_input)
        self.p14_04_combosatuan.addItem("")
        self.p14_04_combosatuan.addItem("")
        self.p14_04_combosatuan.addItem("")
        self.p14_04_combosatuan.addItem("")
        self.p14_04_combosatuan.addItem("")
        self.p14_04_combosatuan.setObjectName(u"p14_04_combosatuan")
        self.p14_04_combosatuan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p14_04_combosatuan.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14_04_combosatuan, 1, 1, 1, 1)

        self.p14_06_datetanggal = QDateEdit(self.p14_input)
        self.p14_06_datetanggal.setObjectName(u"p14_06_datetanggal")
        self.p14_06_datetanggal.setStyleSheet(u"")
        self.p14_06_datetanggal.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p14_06_datetanggal.setReadOnly(False)
        self.p14_06_datetanggal.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.p14_06_datetanggal.setMaximumDate(QDate(9999, 11, 30))
        self.p14_06_datetanggal.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.p14_06_datetanggal, 3, 0, 1, 1)

        self.p14_08_dateexpire = QDateEdit(self.p14_input)
        self.p14_08_dateexpire.setObjectName(u"p14_08_dateexpire")
        self.p14_08_dateexpire.setStyleSheet(u"")
        self.p14_08_dateexpire.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p14_08_dateexpire.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.p14_08_dateexpire.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.p14_08_dateexpire, 3, 1, 1, 1)

        self.layout3_grid.setColumnStretch(0, 1)
        self.layout3_grid.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.p14_input, 2, 1, 1, 1)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.p22_transaksi = QFrame(self.page_2)
        self.p22_transaksi.setObjectName(u"p22_transaksi")
        self.p22_transaksi.setStyleSheet(u"QFrame#p22_transaksi { border: 1px solid; border-color: lightgray; border-radius: 5px; padding: 20px 10px 20px 10px; } QPushButton { background-color: hsl(33, 29%, 70%); border: 1px solid; border-radius: 5px; font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; margin: 10px; padding: 10px; } QPushButton:hover { background-color: hsl(27, 19%, 82%); } QLabel { font-family: Helvetica, Inter, sans-serif; font-size: 12pt; }")
        self.gridLayout_6 = QGridLayout(self.p22_transaksi)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.p22_02_combonama = QComboBox(self.p22_transaksi)
        self.p22_02_combonama.setObjectName(u"p22_02_combonama")
        self.p22_02_combonama.setStyleSheet(u"QComboBox { border: 1px solid; border-color: LightGray; border-radius:5px; font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px; } QComboBox::drop-down { border: 1px solid; border-color: LightGray; border-radius:5px; padding: 5px; } QComboBox::down-arrow { image: url('Assets/caret-down.png'); width: 8px; height: 8px; }")

        self.gridLayout_6.addWidget(self.p22_02_combonama, 1, 0, 1, 2)

        self.p22_07_linetransaksi = QLineEdit(self.p22_transaksi)
        self.p22_07_linetransaksi.setObjectName(u"p22_07_linetransaksi")
        self.p22_07_linetransaksi.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px;")

        self.gridLayout_6.addWidget(self.p22_07_linetransaksi, 5, 0, 1, 1)

        self.p22_08_labeltanggal = QLabel(self.p22_transaksi)
        self.p22_08_labeltanggal.setObjectName(u"p22_08_labeltanggal")
        self.p22_08_labeltanggal.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_08_labeltanggal, 4, 1, 1, 1)

        self.p22_03_labeltransaksi = QLabel(self.p22_transaksi)
        self.p22_03_labeltransaksi.setObjectName(u"p22_03_labeltransaksi")
        self.p22_03_labeltransaksi.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_03_labeltransaksi, 2, 0, 1, 2)

        self.p22_10_tombolreset = QPushButton(self.p22_transaksi)
        self.p22_10_tombolreset.setObjectName(u"p22_10_tombolreset")
        self.p22_10_tombolreset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p22_10_tombolreset.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_10_tombolreset, 6, 0, 1, 1)

        self.p22_11_tombolproses = QPushButton(self.p22_transaksi)
        self.p22_11_tombolproses.setObjectName(u"p22_11_tombolproses")
        self.p22_11_tombolproses.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p22_11_tombolproses.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_11_tombolproses, 6, 1, 1, 1)

        self.p22_05_tombolkeluar = QPushButton(self.p22_transaksi)
        self.p22_05_tombolkeluar.setObjectName(u"p22_05_tombolkeluar")
        self.p22_05_tombolkeluar.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.p22_05_tombolkeluar.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_05_tombolkeluar, 3, 1, 1, 1)

        self.p22_01_labelnama = QLabel(self.p22_transaksi)
        self.p22_01_labelnama.setObjectName(u"p22_01_labelnama")
        self.p22_01_labelnama.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_01_labelnama, 0, 0, 1, 2)

        self.p22_04_tombolmasuk = QPushButton(self.p22_transaksi)
        self.p22_04_tombolmasuk.setObjectName(u"p22_04_tombolmasuk")
        self.p22_04_tombolmasuk.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.p22_04_tombolmasuk.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_04_tombolmasuk, 3, 0, 1, 1)

        self.p22_06_labeljumlah = QLabel(self.p22_transaksi)
        self.p22_06_labeljumlah.setObjectName(u"p22_06_labeljumlah")
        self.p22_06_labeljumlah.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.p22_06_labeljumlah, 4, 0, 1, 1)

        self.p22_09_datetanggal = QDateEdit(self.p22_transaksi)
        self.p22_09_datetanggal.setObjectName(u"p22_09_datetanggal")
        self.p22_09_datetanggal.setStyleSheet(u"font-size: 12pt; font-family: Inter, sans-serif; padding: 10px; margin: 5px;")
        self.p22_09_datetanggal.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p22_09_datetanggal.setDateTime(QDateTime(QDate(2025, 11, 30), QTime(0, 0, 0)))

        self.gridLayout_6.addWidget(self.p22_09_datetanggal, 5, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)

        self.gridLayout_4.addWidget(self.p22_transaksi, 3, 0, 1, 1)

        self.p21_heading = QFrame(self.page_2)
        self.p21_heading.setObjectName(u"p21_heading")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p21_heading.sizePolicy().hasHeightForWidth())
        self.p21_heading.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.p21_heading)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.p21_head = QLabel(self.p21_heading)
        self.p21_head.setObjectName(u"p21_head")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.p21_head.sizePolicy().hasHeightForWidth())
        self.p21_head.setSizePolicy(sizePolicy1)
        self.p21_head.setStyleSheet(u"font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif;")

        self.verticalLayout_5.addWidget(self.p21_head)

        self.p21_headsub = QLabel(self.p21_heading)
        self.p21_headsub.setObjectName(u"p21_headsub")
        sizePolicy1.setHeightForWidth(self.p21_headsub.sizePolicy().hasHeightForWidth())
        self.p21_headsub.setSizePolicy(sizePolicy1)
        self.p21_headsub.setStyleSheet(u"color: #666; font-size: 16px;")

        self.verticalLayout_5.addWidget(self.p21_headsub)


        self.gridLayout_4.addWidget(self.p21_heading, 2, 0, 1, 1)

        self.vspacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.vspacer2, 4, 0, 1, 1)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_8 = QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.p31_header = QFrame(self.page_3)
        self.p31_header.setObjectName(u"p31_header")
        self.p31_header_v = QVBoxLayout(self.p31_header)
        self.p31_header_v.setObjectName(u"p31_header_v")
        self.p31_head = QLabel(self.p31_header)
        self.p31_head.setObjectName(u"p31_head")
        self.p31_head.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 26px; font-weight: bold; padding: 5px 10px 5px 0px;")

        self.p31_header_v.addWidget(self.p31_head)

        self.p31_headsub = QLabel(self.p31_header)
        self.p31_headsub.setObjectName(u"p31_headsub")
        self.p31_headsub.setStyleSheet(u"font-family: Helvetica, Inter, Sans-serif; font-size: 16px; color: gray; padding: 5px 10px 5px 0px;")

        self.p31_header_v.addWidget(self.p31_headsub)


        self.gridLayout_8.addWidget(self.p31_header, 0, 0, 1, 1)

        self.p32_info = QFrame(self.page_3)
        self.p32_info.setObjectName(u"p32_info")
        self.p32_info.setStyleSheet(u"QFrame#p32_info { border: 1px solid; border-color: LightGray; border-radius: 5px; } QLabel,QComboBox,QRadioButton,QTableView { font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; } QLabel { padding: 5px 0px 5px 0px; }")
        self.p32_info_g = QGridLayout(self.p32_info)
        self.p32_info_g.setObjectName(u"p32_info_g")
        self.p32_05_radiobulan = QRadioButton(self.p32_info)
        self.p32_05_radiobulan.setObjectName(u"p32_05_radiobulan")
        self.p32_05_radiobulan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.p32_info_g.addWidget(self.p32_05_radiobulan, 1, 2, 1, 1)

        self.p32_03_labelkedaluwarsa = QLabel(self.p32_info)
        self.p32_03_labelkedaluwarsa.setObjectName(u"p32_03_labelkedaluwarsa")

        self.p32_info_g.addWidget(self.p32_03_labelkedaluwarsa, 0, 1, 1, 3)

        self.p32_01_labelkategori = QLabel(self.p32_info)
        self.p32_01_labelkategori.setObjectName(u"p32_01_labelkategori")

        self.p32_info_g.addWidget(self.p32_01_labelkategori, 0, 0, 1, 1)

        self.p32_06_radiosemua = QRadioButton(self.p32_info)
        self.p32_06_radiosemua.setObjectName(u"p32_06_radiosemua")
        self.p32_06_radiosemua.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p32_06_radiosemua.setChecked(True)

        self.p32_info_g.addWidget(self.p32_06_radiosemua, 1, 3, 1, 1)

        self.p32_04_radiominggu = QRadioButton(self.p32_info)
        self.p32_04_radiominggu.setObjectName(u"p32_04_radiominggu")
        self.p32_04_radiominggu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.p32_info_g.addWidget(self.p32_04_radiominggu, 1, 1, 1, 1)

        self.p32_02_combokategori = QComboBox(self.p32_info)
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.addItem("")
        self.p32_02_combokategori.setObjectName(u"p32_02_combokategori")
        self.p32_02_combokategori.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.p32_info_g.addWidget(self.p32_02_combokategori, 1, 0, 1, 1)

        self.p32_07_tabelhasil = QTableView(self.p32_info)
        self.p32_07_tabelhasil.setObjectName(u"p32_07_tabelhasil")

        self.p32_info_g.addWidget(self.p32_07_tabelhasil, 2, 0, 1, 4)


        self.gridLayout_8.addWidget(self.p32_info, 1, 0, 1, 1)

        self.pages.addWidget(self.page_3)

        self.gridLayout.addWidget(self.pages, 0, 1, 1, 1)

        self.base_sidebar = QFrame(self.centralwidget)
        self.base_sidebar.setObjectName(u"base_sidebar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.base_sidebar.sizePolicy().hasHeightForWidth())
        self.base_sidebar.setSizePolicy(sizePolicy2)
        self.base_sidebar.setStyleSheet(u"QFrame#base_sidebar { border: 1px solid; border-radius: 5px; border-color: LightGray; } QLabel { font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; font-weight: bold; padding: 10px 10px 10px 10px; } QPushButton { background-color: hsl(33, 29%, 70%); border: 1px solid; border-radius: 5px; font-family: Helvetica, Inter, Sans-serif; font-size: 12pt; padding: 10px; margin: 5px; } QPushButton:hover { background-color: hsl(27, 19%, 82%); }")
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
        self.label_headsub.setText(QCoreApplication.translate("MainWindow", u"Tambahkan item baru untuk memantau tanggal kedaluarsa", None))
        self.label_head.setText(QCoreApplication.translate("MainWindow", u"Input Bahan Makanan", None))
        self.p13_01_labelnama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.p13_02_inputnama.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: Daging Sapi", None))
        self.p15_03_radiosayuran.setText(QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.p15_01_labelkategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.p15_06_radioroti.setText(QCoreApplication.translate("MainWindow", u"Roti", None))
        self.p15_07_radiolainnya.setText(QCoreApplication.translate("MainWindow", u"Lainnya", None))
        self.p15_02_radiodaging.setText(QCoreApplication.translate("MainWindow", u"Daging", None))
        self.p15_05_radiosusu.setText(QCoreApplication.translate("MainWindow", u"Susu", None))
        self.p15_04_radiobuah.setText(QCoreApplication.translate("MainWindow", u"Buah", None))
        self.tombol_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.tombol_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.p14_03_labelsatuan.setText(QCoreApplication.translate("MainWindow", u"Satuan", None))
        self.p14_01_labeljumlah.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None))
        self.p14_02_inputjumlah.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: 500", None))
        self.p14_05_labeltanggal.setText(QCoreApplication.translate("MainWindow", u"Tanggal Pembelian", None))
        self.p14_07_labelexpire.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.p14_04_combosatuan.setItemText(0, QCoreApplication.translate("MainWindow", u"gram", None))
        self.p14_04_combosatuan.setItemText(1, QCoreApplication.translate("MainWindow", u"kg", None))
        self.p14_04_combosatuan.setItemText(2, QCoreApplication.translate("MainWindow", u"pcs", None))
        self.p14_04_combosatuan.setItemText(3, QCoreApplication.translate("MainWindow", u"ml", None))
        self.p14_04_combosatuan.setItemText(4, QCoreApplication.translate("MainWindow", u"liter", None))

        self.p14_06_datetanggal.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.p14_08_dateexpire.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.p22_08_labeltanggal.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None))
        self.p22_03_labeltransaksi.setText(QCoreApplication.translate("MainWindow", u"Jenis Transaksi", None))
        self.p22_10_tombolreset.setText(QCoreApplication.translate("MainWindow", u"Reset Form", None))
        self.p22_11_tombolproses.setText(QCoreApplication.translate("MainWindow", u"Proses Transaksi", None))
        self.p22_05_tombolkeluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.p22_01_labelnama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.p22_04_tombolmasuk.setText(QCoreApplication.translate("MainWindow", u"Masuk", None))
        self.p22_06_labeljumlah.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi", None))
        self.p22_09_datetanggal.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.p21_head.setText(QCoreApplication.translate("MainWindow", u"Transaksi Bahan Makanan Baru", None))
        self.p21_headsub.setText(QCoreApplication.translate("MainWindow", u"Isi form di bawah untuk mencatat bahan makanan", None))
        self.p31_head.setText(QCoreApplication.translate("MainWindow", u"Laporan Kedaluwarsa", None))
        self.p31_headsub.setText(QCoreApplication.translate("MainWindow", u"Pantau dan kelola bahan makanan yang akan kedaluwarsa", None))
        self.p32_05_radiobulan.setText(QCoreApplication.translate("MainWindow", u"Bulan Ini", None))
        self.p32_03_labelkedaluwarsa.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.p32_01_labelkategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.p32_06_radiosemua.setText(QCoreApplication.translate("MainWindow", u"Semua", None))
        self.p32_04_radiominggu.setText(QCoreApplication.translate("MainWindow", u"Minggu Ini", None))
        self.p32_02_combokategori.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua", None))
        self.p32_02_combokategori.setItemText(1, QCoreApplication.translate("MainWindow", u"Daging", None))
        self.p32_02_combokategori.setItemText(2, QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.p32_02_combokategori.setItemText(3, QCoreApplication.translate("MainWindow", u"Buah", None))
        self.p32_02_combokategori.setItemText(4, QCoreApplication.translate("MainWindow", u"Susu", None))
        self.p32_02_combokategori.setItemText(5, QCoreApplication.translate("MainWindow", u"Roti", None))
        self.p32_02_combokategori.setItemText(6, QCoreApplication.translate("MainWindow", u"Lainnya", None))

        self.label_profil.setText("")
        self.label_profilnama.setText(QCoreApplication.translate("MainWindow", u"Profil", None))
        self.side_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.side_transaksi.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.side_laporan.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
    # retranslateUi

