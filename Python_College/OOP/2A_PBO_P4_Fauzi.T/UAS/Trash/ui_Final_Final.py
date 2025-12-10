# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Final_FinaltcZZAc.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(624, 457)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.head_v = QVBoxLayout()
        self.head_v.setObjectName(u"head_v")
        self.sub_1_v = QVBoxLayout()
        self.sub_1_v.setObjectName(u"sub_1_v")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.sub_1_v.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.sub_1_v.addWidget(self.label_2)


        self.head_v.addLayout(self.sub_1_v)

        self.sub_2_v = QVBoxLayout()
        self.sub_2_v.setObjectName(u"sub_2_v")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.sub_2_v.addWidget(self.label_3)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.sub_2_v.addWidget(self.lineEdit)


        self.head_v.addLayout(self.sub_2_v)

        self.sub_3_g = QGridLayout()
        self.sub_3_g.setObjectName(u"sub_3_g")
        self.tanggal_edit = QLineEdit(Form)
        self.tanggal_edit.setObjectName(u"tanggal_edit")

        self.sub_3_g.addWidget(self.tanggal_edit, 3, 0, 1, 1)

        self.satuan_label = QLabel(Form)
        self.satuan_label.setObjectName(u"satuan_label")

        self.sub_3_g.addWidget(self.satuan_label, 0, 1, 1, 1)

        self.jumlah_edit = QLineEdit(Form)
        self.jumlah_edit.setObjectName(u"jumlah_edit")

        self.sub_3_g.addWidget(self.jumlah_edit, 1, 0, 1, 1)

        self.expire_label = QLabel(Form)
        self.expire_label.setObjectName(u"expire_label")

        self.sub_3_g.addWidget(self.expire_label, 2, 1, 1, 1)

        self.jumlah_label = QLabel(Form)
        self.jumlah_label.setObjectName(u"jumlah_label")

        self.sub_3_g.addWidget(self.jumlah_label, 0, 0, 1, 1)

        self.tanggal_label = QLabel(Form)
        self.tanggal_label.setObjectName(u"tanggal_label")

        self.sub_3_g.addWidget(self.tanggal_label, 2, 0, 1, 1)

        self.expire_edit = QLineEdit(Form)
        self.expire_edit.setObjectName(u"expire_edit")

        self.sub_3_g.addWidget(self.expire_edit, 3, 1, 1, 1)

        self.satuan_edit = QLineEdit(Form)
        self.satuan_edit.setObjectName(u"satuan_edit")

        self.sub_3_g.addWidget(self.satuan_edit, 1, 1, 1, 1)


        self.head_v.addLayout(self.sub_3_g)

        self.sub_4_h = QHBoxLayout()
        self.sub_4_h.setObjectName(u"sub_4_h")
        self.btn_batal = QPushButton(Form)
        self.btn_batal.setObjectName(u"btn_batal")

        self.sub_4_h.addWidget(self.btn_batal)

        self.btn_simpan = QPushButton(Form)
        self.btn_simpan.setObjectName(u"btn_simpan")

        self.sub_4_h.addWidget(self.btn_simpan)


        self.head_v.addLayout(self.sub_4_h)


        self.verticalLayout_3.addLayout(self.head_v)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.satuan_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.expire_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.jumlah_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tanggal_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.btn_simpan.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

