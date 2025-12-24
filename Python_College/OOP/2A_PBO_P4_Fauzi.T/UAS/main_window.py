# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_PageCUyUVp.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(638, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: hsl(210, 40%, 98%);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QWidget { color: black; font-family: Helvetica, Inter, sans-serif; font-size: 12pt; }")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.p12_lyheading = QFrame(self.page_1)
        self.p12_lyheading.setObjectName(u"p12_lyheading")
        self.layout1_grid = QGridLayout(self.p12_lyheading)
        self.layout1_grid.setObjectName(u"layout1_grid")
        self.layout1_grid.setContentsMargins(10, 10, 10, 10)
        self.lblheadsub = QLabel(self.p12_lyheading)
        self.lblheadsub.setObjectName(u"lblheadsub")
        self.lblheadsub.setStyleSheet(u"QLabel#lblheadsub { color: #666; font-size: 16px; }")

        self.layout1_grid.addWidget(self.lblheadsub, 1, 0, 1, 1)

        self.lblhead = QLabel(self.p12_lyheading)
        self.lblhead.setObjectName(u"lblhead")
        self.lblhead.setStyleSheet(u"QLabel#lblhead { font-size: 26px; font-weight: bold; }")

        self.layout1_grid.addWidget(self.lblhead, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.p12_lyheading, 0, 1, 1, 1)

        self.p13_lynama = QFrame(self.page_1)
        self.p13_lynama.setObjectName(u"p13_lynama")
        self.p13_lynama.setStyleSheet(u"QLabel { padding-bottom: 5px; } QLineEdit { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; padding: 10px; }")
        self.layout2_vertical = QVBoxLayout(self.p13_lynama)
        self.layout2_vertical.setObjectName(u"layout2_vertical")
        self.layout2_vertical.setContentsMargins(10, 10, 10, 10)
        self.p13a_lblnama = QLabel(self.p13_lynama)
        self.p13a_lblnama.setObjectName(u"p13a_lblnama")
        self.p13a_lblnama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.p13a_lblnama)

        self.p13b_lenama = QLineEdit(self.p13_lynama)
        self.p13b_lenama.setObjectName(u"p13b_lenama")
        self.p13b_lenama.setStyleSheet(u"")

        self.layout2_vertical.addWidget(self.p13b_lenama)


        self.gridLayout_3.addWidget(self.p13_lynama, 1, 1, 1, 1)

        self.p15_lykategori = QFrame(self.page_1)
        self.p15_lykategori.setObjectName(u"p15_lykategori")
        self.p15_lykategori.setStyleSheet(u"QLabel { margin-bottom: 5px; } QRadioButton { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; margin: 5px; padding: 10px; }")
        self.layout4_grid = QGridLayout(self.p15_lykategori)
        self.layout4_grid.setObjectName(u"layout4_grid")
        self.layout4_grid.setContentsMargins(10, 10, 10, 10)
        self.p15c_rbsayuran = QRadioButton(self.p15_lykategori)
        self.p15c_rbsayuran.setObjectName(u"p15c_rbsayuran")
        self.p15c_rbsayuran.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15c_rbsayuran.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15c_rbsayuran, 1, 1, 1, 1)

        self.p15a_lblkategori = QLabel(self.p15_lykategori)
        self.p15a_lblkategori.setObjectName(u"p15a_lblkategori")
        self.p15a_lblkategori.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15a_lblkategori, 0, 0, 1, 3)

        self.p15f_rbroti = QRadioButton(self.p15_lykategori)
        self.p15f_rbroti.setObjectName(u"p15f_rbroti")
        self.p15f_rbroti.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15f_rbroti.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15f_rbroti, 2, 1, 1, 1)

        self.p15g_rblainnya = QRadioButton(self.p15_lykategori)
        self.p15g_rblainnya.setObjectName(u"p15g_rblainnya")
        self.p15g_rblainnya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15g_rblainnya.setStyleSheet(u"")
        self.p15g_rblainnya.setChecked(True)

        self.layout4_grid.addWidget(self.p15g_rblainnya, 2, 2, 1, 1)

        self.p15b_rbdaging = QRadioButton(self.p15_lykategori)
        self.p15b_rbdaging.setObjectName(u"p15b_rbdaging")
        self.p15b_rbdaging.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15b_rbdaging.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15b_rbdaging, 1, 0, 1, 1)

        self.p15e_rbsusu = QRadioButton(self.p15_lykategori)
        self.p15e_rbsusu.setObjectName(u"p15e_rbsusu")
        self.p15e_rbsusu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15e_rbsusu.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15e_rbsusu, 2, 0, 1, 1)

        self.p15d_rbbuah = QRadioButton(self.p15_lykategori)
        self.p15d_rbbuah.setObjectName(u"p15d_rbbuah")
        self.p15d_rbbuah.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p15d_rbbuah.setStyleSheet(u"")

        self.layout4_grid.addWidget(self.p15d_rbbuah, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.p15_lykategori, 3, 1, 1, 1)

        self.p16_tombol = QFrame(self.page_1)
        self.p16_tombol.setObjectName(u"p16_tombol")
        self.p16_tombol.setStyleSheet(u"")
        self.layout5_horizontal = QHBoxLayout(self.p16_tombol)
        self.layout5_horizontal.setObjectName(u"layout5_horizontal")
        self.layout5_horizontal.setContentsMargins(10, 10, 10, 10)
        self.hspacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout5_horizontal.addItem(self.hspacer_1)

        self.btnsimpan = QPushButton(self.p16_tombol)
        self.btnsimpan.setObjectName(u"btnsimpan")
        self.btnsimpan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnsimpan.setStyleSheet(u"QPushButton { background-color: hsl(210, 31%, 80%); border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; margin: 10px; padding: 10px; } QPushButton:hover { background-color: hsl(210, 31%, 90%); }")

        self.layout5_horizontal.addWidget(self.btnsimpan)

        self.hspacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.layout5_horizontal.addItem(self.hspacer_2)


        self.gridLayout_3.addWidget(self.p16_tombol, 4, 1, 1, 1)

        self.p14_lyinput = QFrame(self.page_1)
        self.p14_lyinput.setObjectName(u"p14_lyinput")
        self.p14_lyinput.setStyleSheet(u"QSpinBox, QComboBox, QDateEdit { padding: 10px; } QDateEdit { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QDateEdit::drop-down { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QDateEdit::down-arrow { image: url(assets/caret-down.png); width: 8px; height: 8px; } QCalendarWidget { background-color: #2b2b2b; color: #f0f0f0; border-radius: 10px; padding: 8px; } QCalendarWidget QToolButton { color: #ffffff; background-color: #3c3f41; border: none; padding: 6px; border-radius: 6px; font-size: 14px; } QCalendarWidget QToolButton#qt_calendar_prevmonth, QCalendarWidget QToolButton#qt_calendar_nextmonth { width: 28px; height: 28px; border-radius: 6px; } QCalendarWidget QToolButton:hover { background-color: #505354; } QCalendarWidget QComboBox { background-color: #3c3f41; color: white; border-radius: 4px; padding: 3px; } QCalendarWidget QAbstractItemView:enabled { color: #ffffff; selection-background-color: #0078d7; selection-color: #ffffff; background-color: #2e2e2e; } QCalendarW"
                        "idget QWidget#qt_calendar_calendarview QWidget { alternate-background-color: #353535; } QCalendarWidget QAbstractItemView::item:hover { background-color: #444444; color: white; }\n"
"")
        self.layout3_grid = QGridLayout(self.p14_lyinput)
        self.layout3_grid.setObjectName(u"layout3_grid")
        self.layout3_grid.setHorizontalSpacing(10)
        self.layout3_grid.setVerticalSpacing(6)
        self.layout3_grid.setContentsMargins(10, 10, 10, 10)
        self.p14c_lblsatuan = QLabel(self.p14_lyinput)
        self.p14c_lblsatuan.setObjectName(u"p14c_lblsatuan")
        self.p14c_lblsatuan.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14c_lblsatuan, 0, 1, 1, 1)

        self.p14a_lbljumlah = QLabel(self.p14_lyinput)
        self.p14a_lbljumlah.setObjectName(u"p14a_lbljumlah")
        self.p14a_lbljumlah.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14a_lbljumlah, 0, 0, 1, 1)

        self.p14e_lbltanggal = QLabel(self.p14_lyinput)
        self.p14e_lbltanggal.setObjectName(u"p14e_lbltanggal")
        self.p14e_lbltanggal.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14e_lbltanggal, 2, 0, 1, 1)

        self.p14g_lblexpire = QLabel(self.p14_lyinput)
        self.p14g_lblexpire.setObjectName(u"p14g_lblexpire")
        self.p14g_lblexpire.setStyleSheet(u"")

        self.layout3_grid.addWidget(self.p14g_lblexpire, 2, 1, 1, 1)

        self.p14d_cbsatuan = QComboBox(self.p14_lyinput)
        self.p14d_cbsatuan.addItem("")
        self.p14d_cbsatuan.addItem("")
        self.p14d_cbsatuan.addItem("")
        self.p14d_cbsatuan.addItem("")
        self.p14d_cbsatuan.addItem("")
        self.p14d_cbsatuan.setObjectName(u"p14d_cbsatuan")
        self.p14d_cbsatuan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p14d_cbsatuan.setStyleSheet(u"QComboBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px;} QComboBox::drop-down { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QComboBox::down-arrow { image: url(assets/caret-down.png); width: 8px; height: 8px; }")

        self.layout3_grid.addWidget(self.p14d_cbsatuan, 1, 1, 1, 1)

        self.p14f_detanggal = QDateEdit(self.p14_lyinput)
        self.p14f_detanggal.setObjectName(u"p14f_detanggal")
        self.p14f_detanggal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p14f_detanggal.setStyleSheet(u"")
        self.p14f_detanggal.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p14f_detanggal.setReadOnly(False)
        self.p14f_detanggal.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.p14f_detanggal.setMaximumDate(QDate(9999, 11, 30))
        self.p14f_detanggal.setCalendarPopup(True)
        self.p14f_detanggal.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.p14f_detanggal, 3, 0, 1, 1)

        self.p14h_deeexpire = QDateEdit(self.p14_lyinput)
        self.p14h_deeexpire.setObjectName(u"p14h_deeexpire")
        self.p14h_deeexpire.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p14h_deeexpire.setStyleSheet(u"")
        self.p14h_deeexpire.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p14h_deeexpire.setDateTime(QDateTime(QDate(2025, 12, 1), QTime(0, 0, 0)))
        self.p14h_deeexpire.setCalendarPopup(True)
        self.p14h_deeexpire.setDate(QDate(2025, 12, 1))

        self.layout3_grid.addWidget(self.p14h_deeexpire, 3, 1, 1, 1)

        self.p14b_spjumlah = QSpinBox(self.p14_lyinput)
        self.p14b_spjumlah.setObjectName(u"p14b_spjumlah")
        self.p14b_spjumlah.setStyleSheet(u"QSpinBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QSpinBox::up-button, QSpinBox::down-button { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QSpinBox::up-arrow { image: url(assets/caret-up); width: 8px; height: 8px; } QSpinBox::down-arrow { image: url(assets/caret-down); width: 8px; height: 8px; }")
        self.p14b_spjumlah.setMaximum(1000000)

        self.layout3_grid.addWidget(self.p14b_spjumlah, 1, 0, 1, 1)

        self.layout3_grid.setColumnStretch(0, 1)
        self.layout3_grid.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.p14_lyinput, 2, 1, 1, 1)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget { color: black; font-family: Helvetica, Inter, sans-serif; font-size: 12pt; }")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.p22_lytransaksi = QFrame(self.page_2)
        self.p22_lytransaksi.setObjectName(u"p22_lytransaksi")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p22_lytransaksi.sizePolicy().hasHeightForWidth())
        self.p22_lytransaksi.setSizePolicy(sizePolicy)
        self.p22_lytransaksi.setStyleSheet(u"QFrame#p22_lytransaksi { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QComboBox, QSpinBox, QDateEdit { padding: 10px; } QRadioButton { border: 1px solid hsl(210, 13%, 65%); border-radius: 10px; padding: 10px 10px 10px 10px; }")
        self.verticalLayout_3 = QVBoxLayout(self.p22_lytransaksi)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.p22a_lynama = QFrame(self.p22_lytransaksi)
        self.p22a_lynama.setObjectName(u"p22a_lynama")
        self.lyp22a_nama = QVBoxLayout(self.p22a_lynama)
        self.lyp22a_nama.setObjectName(u"lyp22a_nama")
        self.p22aa_lblnama = QLabel(self.p22a_lynama)
        self.p22aa_lblnama.setObjectName(u"p22aa_lblnama")

        self.lyp22a_nama.addWidget(self.p22aa_lblnama)

        self.p22ab_cbnama = QComboBox(self.p22a_lynama)
        self.p22ab_cbnama.setObjectName(u"p22ab_cbnama")
        self.p22ab_cbnama.setStyleSheet(u"QComboBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px;} QComboBox::drop-down { border: 1px solidhsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QComboBox::down-arrow { image: url(assets/caret-down.png); width: 8px; height: 8px; }")

        self.lyp22a_nama.addWidget(self.p22ab_cbnama)


        self.verticalLayout_3.addWidget(self.p22a_lynama)

        self.p22b_lytransaksi = QFrame(self.p22_lytransaksi)
        self.p22b_lytransaksi.setObjectName(u"p22b_lytransaksi")
        self.p22b_lytransaksi.setStyleSheet(u"")
        self.lyp22b_jenis = QGridLayout(self.p22b_lytransaksi)
        self.lyp22b_jenis.setObjectName(u"lyp22b_jenis")
        self.lyp22b_jenis.setHorizontalSpacing(12)
        self.p22bb_rbkeluar = QRadioButton(self.p22b_lytransaksi)
        self.p22bb_rbkeluar.setObjectName(u"p22bb_rbkeluar")
        self.p22bb_rbkeluar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lyp22b_jenis.addWidget(self.p22bb_rbkeluar, 1, 0, 1, 1)

        self.p22bc_rbmasuk = QRadioButton(self.p22b_lytransaksi)
        self.p22bc_rbmasuk.setObjectName(u"p22bc_rbmasuk")
        self.p22bc_rbmasuk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lyp22b_jenis.addWidget(self.p22bc_rbmasuk, 1, 1, 1, 1)

        self.p22ba_lbltransaksi = QLabel(self.p22b_lytransaksi)
        self.p22ba_lbltransaksi.setObjectName(u"p22ba_lbltransaksi")

        self.lyp22b_jenis.addWidget(self.p22ba_lbltransaksi, 0, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.p22b_lytransaksi)

        self.p22c_lynominal = QFrame(self.p22_lytransaksi)
        self.p22c_lynominal.setObjectName(u"p22c_lynominal")
        self.p22c_lynominal.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.p22c_lynominal)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(12)
        self.p22cc_lbltanggal = QLabel(self.p22c_lynominal)
        self.p22cc_lbltanggal.setObjectName(u"p22cc_lbltanggal")
        self.p22cc_lbltanggal.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.p22cc_lbltanggal, 0, 1, 1, 1)

        self.p22ca_cajumlah = QLabel(self.p22c_lynominal)
        self.p22ca_cajumlah.setObjectName(u"p22ca_cajumlah")
        self.p22ca_cajumlah.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.p22ca_cajumlah, 0, 0, 1, 1)

        self.p22cb_spjumlah = QSpinBox(self.p22c_lynominal)
        self.p22cb_spjumlah.setObjectName(u"p22cb_spjumlah")
        self.p22cb_spjumlah.setStyleSheet(u"QSpinBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QSpinBox::up-button, QSpinBox::down-button { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QSpinBox::up-arrow { image: url(assets/caret-up); width: 8px; height: 8px; } QSpinBox::down-arrow { image: url(assets/caret-down); width: 8px; height: 8px; }")

        self.gridLayout_15.addWidget(self.p22cb_spjumlah, 1, 0, 1, 1)

        self.p22cd_detanggal = QDateEdit(self.p22c_lynominal)
        self.p22cd_detanggal.setObjectName(u"p22cd_detanggal")
        self.p22cd_detanggal.setStyleSheet(u"QSpinBox, QComboBox, QDateEdit { padding: 10px; } QDateEdit { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QDateEdit::drop-down { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QDateEdit::down-arrow { image: url(assets/caret-down.png); width: 8px; height: 8px; }")
        self.p22cd_detanggal.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.p22cd_detanggal.setReadOnly(True)
        self.p22cd_detanggal.setCalendarPopup(True)

        self.gridLayout_15.addWidget(self.p22cd_detanggal, 1, 1, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 1)
        self.gridLayout_15.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.p22c_lynominal)

        self.p22d_lytombol = QFrame(self.p22_lytransaksi)
        self.p22d_lytombol.setObjectName(u"p22d_lytombol")
        self.p22d_lytombol.setStyleSheet(u"QPushButton { background-color: hsl(210, 31%, 80%); border: 1px solid hsl(210, 31%, 80%); border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: hsl(210, 31%, 90%); }")
        self.horizontalLayout_5 = QHBoxLayout(self.p22d_lytombol)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.p22db_btnproses = QPushButton(self.p22d_lytombol)
        self.p22db_btnproses.setObjectName(u"p22db_btnproses")
        self.p22db_btnproses.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p22db_btnproses.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.p22db_btnproses)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.p22d_lytombol)


        self.gridLayout_4.addWidget(self.p22_lytransaksi, 3, 0, 1, 1)

        self.lyp21_heading = QFrame(self.page_2)
        self.lyp21_heading.setObjectName(u"lyp21_heading")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lyp21_heading.sizePolicy().hasHeightForWidth())
        self.lyp21_heading.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.lyp21_heading)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.p21a_head = QLabel(self.lyp21_heading)
        self.p21a_head.setObjectName(u"p21a_head")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.p21a_head.sizePolicy().hasHeightForWidth())
        self.p21a_head.setSizePolicy(sizePolicy2)
        self.p21a_head.setStyleSheet(u"QLabel#p21a_head { font-size: 26px; font-weight: bold; font-family: Helvetica, Inter, Sans-serif; }")

        self.verticalLayout_5.addWidget(self.p21a_head)

        self.p21a_headsub = QLabel(self.lyp21_heading)
        self.p21a_headsub.setObjectName(u"p21a_headsub")
        sizePolicy2.setHeightForWidth(self.p21a_headsub.sizePolicy().hasHeightForWidth())
        self.p21a_headsub.setSizePolicy(sizePolicy2)
        self.p21a_headsub.setStyleSheet(u"QLabel#p21a_headsub { color: #666; font-size: 16px; }")

        self.verticalLayout_5.addWidget(self.p21a_headsub)


        self.gridLayout_4.addWidget(self.lyp21_heading, 2, 0, 1, 1)

        self.p2_vspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.p2_vspacer, 4, 0, 1, 1)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QWidget { color: black; font-family: Helvetica, Inter, sans-serif; font-size: 12pt; }")
        self.gridLayout_8 = QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.p31_lyheader = QFrame(self.page_3)
        self.p31_lyheader.setObjectName(u"p31_lyheader")
        self.p31_header_v = QVBoxLayout(self.p31_lyheader)
        self.p31_header_v.setObjectName(u"p31_header_v")
        self.p31_head = QLabel(self.p31_lyheader)
        self.p31_head.setObjectName(u"p31_head")
        self.p31_head.setStyleSheet(u"QLabel#p31_head { font-size: 26px; font-weight: bold; padding: 5px 10px 5px 0px; }")

        self.p31_header_v.addWidget(self.p31_head)

        self.p31_headsub = QLabel(self.p31_lyheader)
        self.p31_headsub.setObjectName(u"p31_headsub")
        self.p31_headsub.setStyleSheet(u"QLabel#p31_headsub { font-size: 16px; color: gray; padding: 5px 10px 5px 0px; }")

        self.p31_header_v.addWidget(self.p31_headsub)


        self.gridLayout_8.addWidget(self.p31_lyheader, 0, 0, 1, 1)

        self.p32_lyinfo = QFrame(self.page_3)
        self.p32_lyinfo.setObjectName(u"p32_lyinfo")
        self.p32_lyinfo.setStyleSheet(u"QFrame#p32_lyinfo { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; } QLabel { padding: 5px 0px 5px 0px; } QTableCornerButton { background-color: hsl(210, 13%, 65%); } QRadioButton { margin-left: 10px; }")
        self.p32_info_g = QGridLayout(self.p32_lyinfo)
        self.p32_info_g.setObjectName(u"p32_info_g")
        self.p32_info_g.setContentsMargins(10, 10, 10, 10)
        self.p32g_rbsemua = QRadioButton(self.p32_lyinfo)
        self.p32g_rbsemua.setObjectName(u"p32g_rbsemua")
        self.p32g_rbsemua.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p32g_rbsemua.setChecked(True)

        self.p32_info_g.addWidget(self.p32g_rbsemua, 1, 3, 1, 1)

        self.p32f_rbbulan = QRadioButton(self.p32_lyinfo)
        self.p32f_rbbulan.setObjectName(u"p32f_rbbulan")
        self.p32f_rbbulan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.p32_info_g.addWidget(self.p32f_rbbulan, 1, 2, 1, 1)

        self.p32a_lblkategori = QLabel(self.p32_lyinfo)
        self.p32a_lblkategori.setObjectName(u"p32a_lblkategori")

        self.p32_info_g.addWidget(self.p32a_lblkategori, 0, 0, 1, 1)

        self.p32h_tbhasil = QTableView(self.p32_lyinfo)
        self.p32h_tbhasil.setObjectName(u"p32h_tbhasil")
        self.p32h_tbhasil.setStyleSheet(u"QHeaderView { background-color: hsl(210, 13%, 65%); border: 1px solid hsl(210, 13%, 65%);; border-radius: 5px; } QTableView { background-color: hsl(210, 31%, 80%); border: 1px solid hsl(210, 13%, 65%);; border-radius: 5px; }")
        self.p32h_tbhasil.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.p32h_tbhasil.horizontalHeader().setStretchLastSection(True)
        self.p32h_tbhasil.verticalHeader().setVisible(False)

        self.p32_info_g.addWidget(self.p32h_tbhasil, 2, 0, 1, 4)

        self.p32b_cbkategori = QComboBox(self.p32_lyinfo)
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.addItem("")
        self.p32b_cbkategori.setObjectName(u"p32b_cbkategori")
        self.p32b_cbkategori.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.p32b_cbkategori.setStyleSheet(u"QComboBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; padding: 5px; } QComboBox::drop-down { border: 1px solid hsl(210, 13%, 65%); border-radius: 0px 5px 5px 0px; } QComboBox::down-arrow { image: url(assets/caret-down.png); width: 8px; height: 8px; }")

        self.p32_info_g.addWidget(self.p32b_cbkategori, 1, 0, 1, 1)

        self.p32e_rbminggu = QRadioButton(self.p32_lyinfo)
        self.p32e_rbminggu.setObjectName(u"p32e_rbminggu")
        self.p32e_rbminggu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.p32_info_g.addWidget(self.p32e_rbminggu, 1, 1, 1, 1)

        self.p32d_lblkedaluwarsa = QLabel(self.p32_lyinfo)
        self.p32d_lblkedaluwarsa.setObjectName(u"p32d_lblkedaluwarsa")

        self.p32_info_g.addWidget(self.p32d_lblkedaluwarsa, 0, 1, 1, 2)

        self.p32i_chkedit = QCheckBox(self.p32_lyinfo)
        self.p32i_chkedit.setObjectName(u"p32i_chkedit")
        self.p32i_chkedit.setStyleSheet(u"QCheckBox { border: 1px solid hsl(210, 13%, 65%); border-radius: 5px; padding: 3px 5px 3px 5px; }")

        self.p32_info_g.addWidget(self.p32i_chkedit, 0, 3, 1, 1)


        self.gridLayout_8.addWidget(self.p32_lyinfo, 1, 0, 1, 1)

        self.pages.addWidget(self.page_3)

        self.gridLayout.addWidget(self.pages, 0, 1, 1, 1)

        self.base_sidebar = QFrame(self.centralwidget)
        self.base_sidebar.setObjectName(u"base_sidebar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.base_sidebar.sizePolicy().hasHeightForWidth())
        self.base_sidebar.setSizePolicy(sizePolicy3)
        self.base_sidebar.setStyleSheet(u"\n"
"QFrame#base_sidebar {\n"
"    border: 1px solid hsl(210, 13%, 65%);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: black;\n"
"    font-family: Helvetica, Inter, Sans-serif;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    padding: 10px 10px 10px 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: hsl(210, 31%, 80%);\n"
"    border: 1px solid hsl(210, 31%, 80%);\n"
"    border-radius: 5px;\n"
"    color:black;\n"
"    font-family: Helvetica, Inter, Sans-serif;\n"
"    font-size: 12pt;\n"
"    padding: 10px;\n"
"    margin: 5px;\n"
"    text-align: justify;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: hsl(210, 31%, 90%);\n"
"}")
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
        self.label_profil.setPixmap(QPixmap(u"assets/user.png"))
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
        icon = QIcon()
        icon.addFile(u"assets/input.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_input.setIcon(icon)

        self.verticalLayout.addWidget(self.side_input)

        self.side_transaksi = QPushButton(self.base_sidebar)
        self.side_transaksi.setObjectName(u"side_transaksi")
        self.side_transaksi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_transaksi.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"assets/transaction.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_transaksi.setIcon(icon1)

        self.verticalLayout.addWidget(self.side_transaksi)

        self.side_laporan = QPushButton(self.base_sidebar)
        self.side_laporan.setObjectName(u"side_laporan")
        self.side_laporan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.side_laporan.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"assets/report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.side_laporan.setIcon(icon2)

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
        self.lblheadsub.setText(QCoreApplication.translate("MainWindow", u"Tambahkan item baru untuk memantau tanggal kedaluarsa", None))
        self.lblhead.setText(QCoreApplication.translate("MainWindow", u"Input Bahan Makanan", None))
        self.p13a_lblnama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.p13b_lenama.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contoh: Daging Sapi", None))
        self.p15c_rbsayuran.setText(QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.p15a_lblkategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.p15f_rbroti.setText(QCoreApplication.translate("MainWindow", u"Roti", None))
        self.p15g_rblainnya.setText(QCoreApplication.translate("MainWindow", u"Lainnya", None))
        self.p15b_rbdaging.setText(QCoreApplication.translate("MainWindow", u"Daging", None))
        self.p15e_rbsusu.setText(QCoreApplication.translate("MainWindow", u"Susu", None))
        self.p15d_rbbuah.setText(QCoreApplication.translate("MainWindow", u"Buah", None))
        self.btnsimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.p14c_lblsatuan.setText(QCoreApplication.translate("MainWindow", u"Satuan", None))
        self.p14a_lbljumlah.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None))
        self.p14e_lbltanggal.setText(QCoreApplication.translate("MainWindow", u"Tanggal Pembelian", None))
        self.p14g_lblexpire.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.p14d_cbsatuan.setItemText(0, QCoreApplication.translate("MainWindow", u"gram", None))
        self.p14d_cbsatuan.setItemText(1, QCoreApplication.translate("MainWindow", u"kg", None))
        self.p14d_cbsatuan.setItemText(2, QCoreApplication.translate("MainWindow", u"pcs", None))
        self.p14d_cbsatuan.setItemText(3, QCoreApplication.translate("MainWindow", u"ml", None))
        self.p14d_cbsatuan.setItemText(4, QCoreApplication.translate("MainWindow", u"liter", None))

        self.p14f_detanggal.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy MMMM dd", None))
        self.p14h_deeexpire.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy MMMM dd", None))
        self.p22aa_lblnama.setText(QCoreApplication.translate("MainWindow", u"Nama Bahan Makanan", None))
        self.p22bb_rbkeluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
        self.p22bc_rbmasuk.setText(QCoreApplication.translate("MainWindow", u"Masuk", None))
        self.p22ba_lbltransaksi.setText(QCoreApplication.translate("MainWindow", u"Jenis Transaksi", None))
        self.p22cc_lbltanggal.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None))
        self.p22ca_cajumlah.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi", None))
        self.p22cd_detanggal.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy MMMM dd", None))
        self.p22db_btnproses.setText(QCoreApplication.translate("MainWindow", u"Proses Transaksi", None))
        self.p21a_head.setText(QCoreApplication.translate("MainWindow", u"Transaksi Bahan Makanan Baru", None))
        self.p21a_headsub.setText(QCoreApplication.translate("MainWindow", u"Isi form di bawah untuk mencatat bahan makanan", None))
        self.p31_head.setText(QCoreApplication.translate("MainWindow", u"Laporan Kedaluwarsa", None))
        self.p31_headsub.setText(QCoreApplication.translate("MainWindow", u"Pantau dan kelola bahan makanan yang akan kedaluwarsa", None))
        self.p32g_rbsemua.setText(QCoreApplication.translate("MainWindow", u"Semua", None))
        self.p32f_rbbulan.setText(QCoreApplication.translate("MainWindow", u"Bulan Ini", None))
        self.p32a_lblkategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.p32b_cbkategori.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua", None))
        self.p32b_cbkategori.setItemText(1, QCoreApplication.translate("MainWindow", u"Daging", None))
        self.p32b_cbkategori.setItemText(2, QCoreApplication.translate("MainWindow", u"Sayuran", None))
        self.p32b_cbkategori.setItemText(3, QCoreApplication.translate("MainWindow", u"Buah", None))
        self.p32b_cbkategori.setItemText(4, QCoreApplication.translate("MainWindow", u"Susu", None))
        self.p32b_cbkategori.setItemText(5, QCoreApplication.translate("MainWindow", u"Roti", None))
        self.p32b_cbkategori.setItemText(6, QCoreApplication.translate("MainWindow", u"Lainnya", None))

        self.p32e_rbminggu.setText(QCoreApplication.translate("MainWindow", u"Minggu Ini", None))
        self.p32d_lblkedaluwarsa.setText(QCoreApplication.translate("MainWindow", u"Tanggal Kedaluwarsa", None))
        self.p32i_chkedit.setText(QCoreApplication.translate("MainWindow", u"Edit Mode", None))
        self.label_profil.setText("")
        self.label_profilnama.setText(QCoreApplication.translate("MainWindow", u"Profil", None))
        self.side_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.side_transaksi.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        self.side_laporan.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
    # retranslateUi

