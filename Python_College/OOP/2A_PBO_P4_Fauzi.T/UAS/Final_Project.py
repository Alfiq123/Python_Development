import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QComboBox, QDateEdit,
                               QRadioButton, QPushButton, QGridLayout, QFrame,
                               QScrollArea, QButtonGroup, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont, QIcon

class FoodInputForm(QWidget):
    def __init__(self):
        super().__init__()

        # Konfigurasi Window
        self.setWindowTitle("Form Input Bahan Makanan")
        self.resize(600, 750)

        # Warna Utama dari desain HTML
        self.primary_color = "#19e65e"
        self.bg_dark = "#112116"
        self.bg_card = "#1a2c20" # Sedikit lebih terang dari bg utama
        self.text_color = "#ffffff"
        self.text_gray = "#9ca3af"
        self.border_color = "#374151"

        # Setup UI
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        # Layout Utama
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Scroll Area (untuk memastikan responsif jika layar kecil)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        # Container di dalam Scroll Area
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setSpacing(24) # Gap antar elemen (mirip gap-6 Tailwind)
        self.content_layout.setContentsMargins(32, 32, 32, 32)

        # --- 1. Header ---
        header_layout = QVBoxLayout()
        title = QLabel("Input Bahan Makanan")
        title.setObjectName("h1")
        subtitle = QLabel("Tambahkan item baru untuk memantau tanggal kedaluwarsanya.")
        subtitle.setObjectName("subtitle")
        subtitle.setWordWrap(True)

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        self.content_layout.addLayout(header_layout)

        # --- 2. Nama Bahan Makanan ---
        name_group = QVBoxLayout()
        lbl_name = QLabel("Nama Bahan Makanan")
        lbl_name.setObjectName("label")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Contoh: Daging Sapi")
        self.input_name.setFixedHeight(45)

        name_group.addWidget(lbl_name)
        name_group.addWidget(self.input_name)
        self.content_layout.addLayout(name_group)

        # --- 3. Jumlah & Satuan (Grid Layout) ---
        qty_unit_layout = QHBoxLayout()
        qty_unit_layout.setSpacing(24)

        # Jumlah
        qty_group = QVBoxLayout()
        lbl_qty = QLabel("Jumlah")
        lbl_qty.setObjectName("label")
        self.input_qty = QLineEdit() # Bisa diganti QSpinBox
        self.input_qty.setPlaceholderText("Contoh: 500")
        self.input_qty.setFixedHeight(45)
        qty_group.addWidget(lbl_qty)
        qty_group.addWidget(self.input_qty)

        # Satuan
        unit_group = QVBoxLayout()
        lbl_unit = QLabel("Satuan")
        lbl_unit.setObjectName("label")
        self.input_unit = QComboBox()
        self.input_unit.addItems(["kg", "gram", "pcs", "liter", "ml"])
        self.input_unit.setFixedHeight(45)
        unit_group.addWidget(lbl_unit)
        unit_group.addWidget(self.input_unit)

        qty_unit_layout.addLayout(qty_group, 1) # Stretch factor 1
        qty_unit_layout.addLayout(unit_group, 1)
        self.content_layout.addLayout(qty_unit_layout)

        # --- 4. Tanggal Pembelian & Kedaluwarsa ---
        date_layout = QHBoxLayout()
        date_layout.setSpacing(24)

        # Tgl Beli
        buy_date_group = QVBoxLayout()
        lbl_buy = QLabel("Tanggal Pembelian")
        lbl_buy.setObjectName("label")
        self.input_buy_date = QDateEdit()
        self.input_buy_date.setCalendarPopup(True)
        self.input_buy_date.setDate(QDate.currentDate())
        self.input_buy_date.setFixedHeight(45)
        buy_date_group.addWidget(lbl_buy)
        buy_date_group.addWidget(self.input_buy_date)

        # Tgl Expired
        exp_date_group = QVBoxLayout()
        lbl_exp = QLabel("Tanggal Kedaluwarsa")
        lbl_exp.setObjectName("label")
        self.input_exp_date = QDateEdit()
        self.input_exp_date.setCalendarPopup(True)
        self.input_exp_date.setDate(QDate.currentDate().addDays(7)) # Default +7 hari
        self.input_exp_date.setFixedHeight(45)
        exp_date_group.addWidget(lbl_exp)
        exp_date_group.addWidget(self.input_exp_date)

        date_layout.addLayout(buy_date_group)
        date_layout.addLayout(exp_date_group)
        self.content_layout.addLayout(date_layout)

        # --- 5. Kategori (Radio Buttons) ---
        cat_group = QVBoxLayout()
        lbl_cat = QLabel("Kategori")
        lbl_cat.setObjectName("label-header")
        cat_group.addWidget(lbl_cat)

        self.cat_grid = QGridLayout()
        self.cat_grid.setSpacing(12)

        categories = ["Daging", "Sayuran", "Buah", "Susu", "Roti", "Lainnya"]
        self.cat_buttons = QButtonGroup(self)

        row, col = 0, 0
        for i, cat in enumerate(categories):
            radio = QRadioButton(cat)
            radio.setCursor(Qt.PointingHandCursor)
            self.cat_buttons.addButton(radio, i)
            self.cat_grid.addWidget(radio, row, col)

            col += 1
            if col > 2: # 3 kolom per baris
                col = 0
                row += 1

        cat_group.addLayout(self.cat_grid)
        self.content_layout.addLayout(cat_group)

        # Spacer agar tombol ada di bawah
        self.content_layout.addStretch()

        # --- 6. Action Buttons ---
        btn_layout = QHBoxLayout()
        btn_layout.addStretch() # Dorong tombol ke kanan

        self.btn_cancel = QPushButton("Batal")
        self.btn_cancel.setObjectName("btn-cancel")
        self.btn_cancel.setCursor(Qt.PointingHandCursor)
        self.btn_cancel.setFixedSize(100, 44)

        self.btn_save = QPushButton("Simpan")
        self.btn_save.setObjectName("btn-save")
        self.btn_save.setCursor(Qt.PointingHandCursor)
        self.btn_save.setFixedSize(100, 44)

        # Connect signal (contoh fungsi)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_save.clicked.connect(self.on_save)

        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)

        self.content_layout.addLayout(btn_layout)

        # Set scroll widget
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def apply_styles(self):
        # Menggunakan CSS mirip Tailwind
        # Font family 'Inter' atau default sans-serif
        self.setStyleSheet(f"""
QWidget {{
                           background-color: {self.bg_dark};
                           color: {self.text_color};
font-family: 'Segoe UI', 'Inter', sans-serif;
font-size: 14px;
}}

/* Header Styles */
QLabel#h1 {{
font-size: 24px;
font-weight: bold;
                           color: {self.text_color};
margin-bottom: 4px;
}}
QLabel#subtitle {{
font-size: 14px;
                           color: {self.text_gray};
}}
QLabel#label {{
font-size: 14px;
font-weight: 500;
                           color: {self.text_color};
margin-bottom: 2px;
}}
QLabel#label-header {{
font-size: 14px;
font-weight: 600;
margin-bottom: 8px;
}}

/* Input Fields (Text, Date, Combo) */
QLineEdit, QComboBox, QDateEdit {{
                           background-color: {self.bg_card};
                           border: 1px solid {self.border_color};
border-radius: 8px;
padding: 0 12px;
color: white;
                           selection-background-color: {self.primary_color};
selection-color: black;
}}
QLineEdit:focus, QComboBox:focus, QDateEdit:focus {{
                           border: 2px solid {self.primary_color};
}}

/* Dropdown Arrow Styling */
QComboBox::drop-down {{
border: 0px;
margin-right: 10px;
}}
QComboBox::down-arrow {{
image: none;
border-left: 5px solid transparent;
border-right: 5px solid transparent;
                           border-top: 5px solid {self.text_gray};
margin-top: 2px;
}}

/* Date Picker Styling */
QCalendarWidget QWidget {{
                           background-color: {self.bg_card};
color: white;
}}

/* Radio Buttons (Card Style) */
QRadioButton {{
                           background-color: {self.bg_card};
                           border: 1px solid {self.border_color};
border-radius: 8px;
padding: 12px;
                           color: {self.text_color};
}}
QRadioButton::indicator {{
width: 16px;
height: 16px;
border-radius: 8px;
                           border: 1px solid {self.text_gray};
background: transparent;
margin-right: 8px;
}}
QRadioButton::indicator:checked {{
                           border: 4px solid {self.primary_color};
background: white;
}}
QRadioButton:checked {{
                           border: 1px solid {self.primary_color};
background-color: rgba(25, 230, 94, 0.1); /* Primary color with opacity */
}}

/* Buttons */
QPushButton#btn-cancel {{
background-color: #374151;
color: white;
border: none;
border-radius: 8px;
font-weight: 600;
}}
QPushButton#btn-cancel:hover {{
background-color: #4b5563;
}}

QPushButton#btn-save {{
                           background-color: {self.primary_color};
color: black;
border: none;
border-radius: 8px;
font-weight: 600;
}}
QPushButton#btn-save:hover {{
background-color: #4ade80; /* Lighter green */
}}
QPushButton#btn-save:pressed {{
padding-top: 2px; /* Efek klik */
}}
                           """)

    def on_save(self):
        # Logika sederhana untuk mengambil data
        print("--- Data Disimpan ---")
        print(f"Nama: {self.input_name.text()}")
        print(f"Jumlah: {self.input_qty.text()} {self.input_unit.currentText()}")
        print(f"Beli: {self.input_buy_date.date().toString('yyyy-MM-dd')}")
        print(f"Exp: {self.input_exp_date.date().toString('yyyy-MM-dd')}")

        selected_cat = self.cat_buttons.checkedButton()
        if selected_cat:
            print(f"Kategori: {selected_cat.text()}")
        else:
            print("Kategori: Belum dipilih")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set font aplikasi global
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = FoodInputForm()
    window.show()
    sys.exit(app.exec())
