# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_FInaldJZRrb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(503, 620)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_1_v = QVBoxLayout()
        self.layout_1_v.setObjectName(u"layout_1_v")
        self.layout_1_v.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.layout_1_v.addWidget(self.label)


        self.verticalLayout.addLayout(self.layout_1_v)

        self.layout_2_v = QVBoxLayout()
        self.layout_2_v.setObjectName(u"layout_2_v")
        self.layout_2_v.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"padding-bottom: 5px;")

        self.layout_2_v.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"padding: 10px;\n"
"                                        font-size: 12pt;")

        self.layout_2_v.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.layout_2_v)

        self.layout_3_g = QGridLayout()
        self.layout_3_g.setObjectName(u"layout_3_g")
        self.layout_3_g.setHorizontalSpacing(10)
        self.layout_3_g.setVerticalSpacing(6)
        self.layout_3_g.setContentsMargins(10, 10, 10, 10)
        self.satuan_label = QLabel(self.centralwidget)
        self.satuan_label.setObjectName(u"satuan_label")
        self.satuan_label.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin-bottom: 5px;")

        self.layout_3_g.addWidget(self.satuan_label, 0, 1, 1, 1)

        self.jumlah_label = QLabel(self.centralwidget)
        self.jumlah_label.setObjectName(u"jumlah_label")
        self.jumlah_label.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin-bottom: 5px;")

        self.layout_3_g.addWidget(self.jumlah_label, 0, 0, 1, 1)

        self.jumlah_edit = QLineEdit(self.centralwidget)
        self.jumlah_edit.setObjectName(u"jumlah_edit")
        self.jumlah_edit.setStyleSheet(u"padding: 10px;\n"
"                                        font-size: 12pt;")

        self.layout_3_g.addWidget(self.jumlah_edit, 1, 0, 1, 1)

        self.tanggal_label = QLabel(self.centralwidget)
        self.tanggal_label.setObjectName(u"tanggal_label")
        self.tanggal_label.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin-bottom: 5px;\n"
"margin-top: 5px;")

        self.layout_3_g.addWidget(self.tanggal_label, 2, 0, 1, 1)

        self.expire_label = QLabel(self.centralwidget)
        self.expire_label.setObjectName(u"expire_label")
        self.expire_label.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin-bottom: 5px;\n"
"margin-top: 5px;")

        self.layout_3_g.addWidget(self.expire_label, 2, 1, 1, 1)

        self.satuan_combo = QComboBox(self.centralwidget)
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.addItem("")
        self.satuan_combo.setObjectName(u"satuan_combo")
        self.satuan_combo.setStyleSheet(u"padding: 10px;\n"
"                                        font-size: 12pt;")

        self.layout_3_g.addWidget(self.satuan_combo, 1, 1, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"padding: 10px;\n"
"                                        font-size: 12pt;")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setMaximumDate(QDate(9999, 11, 30))
        self.dateEdit.setDate(QDate(2025, 1, 12))

        self.layout_3_g.addWidget(self.dateEdit, 3, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"padding: 10px;\n"
"                                        font-size: 12pt;")
        self.dateEdit_2.setDate(QDate(2025, 1, 12))

        self.layout_3_g.addWidget(self.dateEdit_2, 3, 1, 1, 1)

        self.layout_3_g.setColumnStretch(0, 1)
        self.layout_3_g.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.layout_3_g)

        self.layout_4_g = QGridLayout()
        self.layout_4_g.setObjectName(u"layout_4_g")
        self.layout_4_g.setContentsMargins(10, 10, 10, 10)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton_5, 2, 1, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton, 1, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton_3, 1, 2, 1, 1)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton_4, 2, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"border: 1px solid;\n"
"border-color: lightgray;\n"
"border-radius: 5px;\n"
"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin: 5px;\n"
"padding: 10px;")

        self.layout_4_g.addWidget(self.radioButton_6, 2, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 12pt;\n"
"font-family: Inter, sans-serif;\n"
"margin-bottom: 5px;")

        self.layout_4_g.addWidget(self.label_3, 0, 0, 1, 3)


        self.verticalLayout.addLayout(self.layout_4_g)

        self.layout_5_h = QHBoxLayout()
        self.layout_5_h.setObjectName(u"layout_5_h")
        self.layout_5_h.setContentsMargins(10, 10, 10, 10)
        self.btn_batal = QPushButton(self.centralwidget)
        self.btn_batal.setObjectName(u"btn_batal")
        self.btn_batal.setStyleSheet(u"QPushButton#btn_batal {\n"
"                                        height: 44px; /* h-11 */\n"
"                                        padding: 0 24px; /* px-6 */\n"
"                                        border: 1px solid;\n"
"                                        border-radius: 8px; /* rounded-lg */\n"
"                                        background: rgba(229,231,235,0.8); /* bg-gray-200/80\n"
"                                        */\n"
"                                        color: rgb(31,41,55); /* text-gray-800 */\n"
"                                        font-size: 12pt; /* text-sm */\n"
"                                        font-weight: 600; /* font-semibold */\n"
"                                        }\n"
"\n"
"                                        /* Hover */\n"
"                                        QPushButton#btn_batal:hover {\n"
"                                        background: rgba(209,213,219,0.8); /*\n"
"                                        hover:bg-gray-300/80 *"
                        "/\n"
"                                        }\n"
"\n"
"                                        /* Dark mode (Qt tidak punya otomatis, jadi harus\n"
"                                        manual) */\n"
"                                        /* Biasanya diganti via setStyleSheet() ketika mode\n"
"                                        gelap aktif */\n"
"                                        QPushButton#btn_batal.dark {\n"
"                                        background: rgba(55,65,81,0.5); /*\n"
"                                        dark:bg-gray-700/50 */\n"
"                                        color: rgb(229,231,235); /* dark:text-gray-200 */\n"
"                                        }\n"
"\n"
"                                        QPushButton#btn_batal.dark:hover {\n"
"                                        background: rgba(75,85,99,0.5); /*\n"
"                                        dark:hover:bg-gray-600/50 */\n"
"                                        }")

        self.layout_5_h.addWidget(self.btn_batal)

        self.btn_simpan = QPushButton(self.centralwidget)
        self.btn_simpan.setObjectName(u"btn_simpan")
        self.btn_simpan.setStyleSheet(u"QPushButton#btn_simpan {\n"
"                                        height: 44px; /* h-11 */\n"
"                                        padding: 0 24px; /* px-6 */\n"
"                                        border: 1px solid;\n"
"                                        border-radius: 8px; /* rounded-lg */\n"
"                                        background: rgb(25, 230, 94); /* bg-primary \u2192 pilih\n"
"                                        warna sendiri */\n"
"                                        color: black; /* text-black */\n"
"                                        font-size: 12pt; /* text-sm */\n"
"                                        font-weight: 600; /* font-semibold */\n"
"                                        }\n"
"\n"
"                                        /* QSS TIDAK BISA scale transform di hover */\n"
"                                        QPushButton#btn_simpan:hover {\n"
"                                        /* workarounds */\n"
"                                       "
                        " padding: 0 26px; /* buat seolah-olah membesar */\n"
"                                        }\n"
"\n"
"                                        /* active:scale-95 \u2192 tidak ada, jadi manual */\n"
"                                        QPushButton#btn_simpan:pressed {\n"
"                                        padding: 0 22px;\n"
"                                        }")

        self.layout_5_h.addWidget(self.btn_simpan)


        self.verticalLayout.addLayout(self.layout_5_h)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<style>\n"
"    h1 {\n"
"        border: 1px solid;\n"
"        color: #333;\n"
"        margin-top: 15px;\n"
"        margin-bottom: 5px;\n"
"        font-family: Inter, sans-serif;\n"
"    }\n"
"\n"
"    p {\n"
"        color: #666;\n"
"        margin-top: 5px;\n"
"        margin-bottom: 15px;\n"
"        font-size: 12pt;\n"
"        font-family: Inter, sans-serif;\n"
"    }\n"
"</style>\n"
"\n"
"<h1>Input Bahan Makanan</h1>\n"
"<p>Tambahkan item baru untuk memantau tanggal.</p>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: Daging Sapi", None))
        self.satuan_label.setText(QCoreApplication.translate("MainWindow", u"Satuan", None))
        self.jumlah_label.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None))
        self.jumlah_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: 500", None))
        self.tanggal_label.setText(QCoreApplication.translate("MainWindow", u"Tanggal Pembelian", None))
        self.expire_label.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.satuan_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"gram", None))
        self.satuan_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"kg", None))
        self.satuan_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"pcs", None))
        self.satuan_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"ml", None))
        self.satuan_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"liter", None))

        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.btn_batal.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.btn_simpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
    # retranslateUi

