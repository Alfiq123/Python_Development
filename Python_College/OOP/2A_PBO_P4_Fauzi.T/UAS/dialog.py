from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QMessageBox, QPushButton, QTableView, QVBoxLayout,
    QHeaderView
)


# noinspection PyUnresolvedReferences
class EditTabel(QDialog):
    """Membuat Edit Tabel karena kode sebelumnya kacau"""

    def __init__(self, parent=None, table_name="Bahan Makanan"):
        super().__init__(parent)

        self.setWindowTitle(f"Edit Mode - {table_name}")
        self.resize(900, 500)

        # --- MODEL --- #
        self.model = QSqlTableModel(self)
        self.model.setTable(table_name)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        # --- TABLE VIEW --- #
        self.tb = QTableView()
        self.tb.setModel(self.model)
        self.tb.resizeColumnsToContents()
        self.tb.verticalHeader().setVisible(False)
        self.tb.hideColumn(0)
        self.tb.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tb.setSortingEnabled(True)

        # --- BUTTONS --- #
        self.btnsave = QPushButton("Simpan")
        self.btncancel = QPushButton("Cancel")

        self.btnsave.clicked.connect(self.save_changes)
        self.btncancel.clicked.connect(self.cancel_changes)

        self.btnsave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btncancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # --- STYLING --- #
        self.setStyleSheet("""
            QHeaderView { 
                background-color: #1B3C53; 
                border: 1px solid; 
                border-radius: 5px;
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
            }
            QTableView {
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
            }
            QPushButton { 
                background-color: #234C6A; 
                border: 1px solid #234C6A; 
                border-radius: 5px; 
                font-family: Helvetica, Inter, Sans-serif; 
                font-size: 12pt; 
                margin: 10px; 
                padding: 10px; 
            } 
            QPushButton:hover { 
                background-color: #456882; 
            }
        """)

        # Layout button horizontal
        btnly = QHBoxLayout()
        btnly.addWidget(self.btnsave)
        btnly.addWidget(self.btncancel)

        # Layout utama
        layout = QVBoxLayout(self)
        layout.addWidget(self.tb)
        layout.addLayout(btnly)

    def save_changes(self):
        if not self.model.submitAll():
            QMessageBox.warning(
                self, "Error", self.model.lastError().text()
            )
        else:
            QMessageBox.information(
                self, "Sukses", "Perubahan Berhasil Disimpan!"
            )
            self.accept()

    def cancel_changes(self):
        self.model.revertAll()
        self.reject()
