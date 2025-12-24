class Redesign:
    def __init__(self, ui):
        self.ui = ui
        self.design()
        self.properties()

    def design(self):
        # === FIXING ARROW - PAGE 1 === #
        self.ui.p13b_lenama.setStyleSheet("""
            border: 2px solid #456882;
            border-radius: 5px;
        """)

        self.ui.p14b_spjumlah.setStyleSheet("""
            QSpinBox::up-arrow {
                image: url(Assets/caretup_white.png); 
            }

            QSpinBox::down-arrow {
                image: url(Assets/caretdown_white.png); 
            }
        """)

        self.ui.p14d_cbsatuan.setStyleSheet("""
            QComboBox::down-arrow {
                image: url(Assets/caretdown_white.png); 
            }
        """)

        self.ui.p14f_detanggal.setStyleSheet("""
            QCalendarWidget QSpinBox::up-arrow {
                image: url(Assets/caretup_white.png);
                height: 8px;
                width: 8px;
            }

            QCalendarWidget QSpinBox::down-arrow {
                image: url(Assets/caretdown_white.png);
                height: 8px;
                width: 8px;
            }

            QDateEdit::down-arrow {
                image: url(Assets/caretdown_white.png);
            }
        """)

        self.ui.p14h_deeexpire.setStyleSheet("""
            QDateEdit::down-arrow {
                image: url(Assets/caretdown_white.png);
            }

            QCalendarWidget QSpinBox::up-arrow {
                image: url(Assets/caretup_white.png);
                height: 8px;
                width: 8px;
            }

            QCalendarWidget QSpinBox::down-arrow {
                image: url(Assets/caretdown_white.png);
                height: 8px;
                width: 8px;
            }
        """)

        # === FIXING ARROW - PAGE 2 === #
        self.ui.p22ab_cbnama.setStyleSheet("""
            QComboBox::down-arrow {
                image: url(Assets/caretdown_white.png);
            }
        """)
        self.ui.p22cb_spjumlah.setStyleSheet("""
            QSpinBox::up-arrow {
                image: url(Assets/caretup_white.png);
            }

            QSpinBox::down-arrow {
                image: url(Assets/caretdown_white.png);
            }
        """)
        self.ui.p22cd_detanggal.setStyleSheet("""
            QDateEdit::down-arrow {
                image: url(Assets/caretdown_white.png);
            }

            QCalendarWidget QSpinBox::up-arrow {
                image: url(Assets/caretup_white.png);
                height: 8px;
                width: 8px;
            }

            QCalendarWidget QSpinBox::down-arrow {
                image: url(Assets/caretdown_white.png);
                height: 8px;
                width: 8px;
            }
        """)

        # === FIXING ARROW - PAGE 3 === #
        self.ui.p32b_cbkategori.setStyleSheet("""
            QComboBox::down-arrow {
                image: url(Assets/caretdown_white.png);
            }
        """)

    def properties(self):
        self.ui.p14f_detanggal.calendarWidget().setMinimumWidth(400)
        self.ui.p14h_deeexpire.calendarWidget().setMinimumWidth(400)
        self.ui.p22cd_detanggal.calendarWidget().setMinimumWidth(400)
