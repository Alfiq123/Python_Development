from datetime import datetime

from PySide6.QtCore import QDate, QDateTime
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QStyledItemDelegate


# noinspection PyUnresolvedReferences
class GantiTanggal(QStyledItemDelegate):
    """Mengubah Format tanggal Amerika ke Standar Internasional, F**K USA"""

    def displayText(self, value, locale):
        if isinstance(value, (QDate, QDateTime)):
            return value.toString("yyyy MMMM dd")

        elif isinstance(value, (datetime.date, datetime.datetime)):
            return value.strftime("%Y/%m/%d")

        else:
            return super().displayText(value, locale)


class WarnaSisaHari(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)

        # Kolom ke-? sesuaikan dengan posisinya di tabelmu
        # misal sisa hari ada di kolom 3 (index mulai 0 → 0,1,2,3)
        if index.column() == 6:
            sisa = index.data()

            if sisa is not None:
                try:
                    sisa = int(sisa)

                    if sisa > 7:
                        option.backgroundBrush = QBrush(
                            QColor("#B3FFB3"))  # hijau

                    elif 1 <= sisa <= 7:
                        option.backgroundBrush = QBrush(
                            QColor("#FFF9A6"))  # kuning

                    elif sisa <= 0:
                        option.backgroundBrush = QBrush(
                            QColor("#FFB3B3"))  # merah

                except ValueError:
                    pass
