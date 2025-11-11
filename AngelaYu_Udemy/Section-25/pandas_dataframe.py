# Untuk memuat paket pandas dan mulai menggunakannya, impor paket ini.
# Alias yang disepakati oleh komunitas untuk pandas adalah `pd`,
#   └── sehingga memuat pandas sebagai `pd` dianggap sebagai praktik standar dalam seluruh dokumentasi pandas.
import pandas as pd

# ? Saya ingin menyimpan data penumpang Titanic. Untuk sejumlah penumpang, saya mengetahui data nama (karakter),
#   └── usia (bilangan bulat), dan jenis kelamin (laki-laki/perempuan).
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(f"{df}\n")
# Untuk menyimpan data secara manual dalam tabel, buatlah `DataFrame`. Saat menggunakan kamus Python yang berisi daftar,
#   └── kunci kamus akan digunakan sebagai header kolom dan nilai dalam setiap daftar sebagai kolom `DataFrame`.

# `DataFrame` adalah struktur data dua dimensi yang dapat menyimpan data berbagai jenis
#   └── (termasuk karakter, bilangan bulat, bilangan desimal, data kategorikal, dan lainnya) dalam kolom.
# Struktur ini mirip dengan spreadsheet, tabel SQL, atau `data.frame` dalam R.

#   • Tabel ini memiliki 3 kolom, masing-masing dengan label kolom.
#       └── Label kolom tersebut berturut-turut adalah `Name`, `Age`, dan `Sex`.
#
#   • Kolom `Name` berisi data teks dengan setiap nilainya berupa string,
#       └── kolom `Age` berisi angka, dan kolom `Sex` berisi data teks.

# ** Setiap kolom dalam DataFrame adalah Series. ** #

# Saat memilih satu kolom dari `DataFrame` pandas, hasilnya adalah `Series` pandas.
# Untuk memilih kolom, gunakan label kolom di antara kurung siku `[]`.

# ? Saya hanya tertarik untuk bekerja dengan data pada kolom `Age`.
print(f"{df['Age']}")

# Catatan:
#
# Jika Kamu familiar dengan `Dictionary` di Python,
#   └── pemilihan kolom tunggal sangat mirip dengan pemilihan nilai `dictionary` berdasarkan kunci.

# Kamu juga dapat membuat `Series` dari awal:

ages = pd.Series(data=[16, 32, 64], name="Age")
print(f"\n{ages}")

# Sebuah `Series` dalam pandas tidak memiliki label kolom, karena `Series` hanyalah satu kolom dari sebuah `DataFrame`.
# `Series` memang memiliki label baris.

# ** Melakukan sesuatu dengan `DataFrame` atau `Series` ** #

# ? Aku ingin mengetahui usia maksimum penumpang.
# Kita dapat melakukan ini pada `DataFrame` dengan memilih kolom `Age` dan menerapkan fungsi `max()`:

print(f"\n{df['Age'].max()}")

# Atau di `Series`

print(ages.max())

# Seperti yang ditunjukkan oleh metode `max()`, Kamu dapat melakukan berbagai hal dengan `DataFrame` atau `Series`.
# pandas menyediakan banyak fungsi, masing-masing merupakan metode yang dapat Kamu terapkan pada `DataFrame` atau
# `Series`. Karena metode adalah fungsi, jangan lupa untuk menggunakan tanda kurung `()`.

# ? Saya tertarik dengan beberapa statistik dasar dari data numerik pada tabel data saya.

print(df.describe())

# Metode `describe()` memberikan gambaran singkat tentang data numerik dalam sebuah `DataFrame`.
# Karena kolom `Name` dan `Sex` berisi data teks, kolom-kolom ini secara default tidak diperhitungkan
# oleh metode `describe()`.

# Catatan
#
# Ini hanyalah titik awal. Sama seperti perangkat lunak spreadsheet, pandas mewakili data sebagai tabel
# dengan kolom dan baris. Selain representasi data, pandas juga mendukung manipulasi data dan perhitungan
# yang biasa dilakukan dalam perangkat lunak spreadsheet. Lanjutkan membaca tutorial berikutnya untuk memulai!

# INGAT
#
#   • Impor paket, yaitu `import pandas as pd`
#   • Sebuah tabel data disimpan sebagai `DataFrame` pandas
#   • Setiap kolom dalam `DataFrame` adalah `Series`
#   • Kamu dapat melakukan tindakan dengan menerapkan metode pada `DataFrame` atau `Series`