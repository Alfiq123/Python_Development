# Latihan 2: Pengaturan Kelembaban Otomatis

# Sistem irigasi otomatis memiliki pengaturan kelembaban tanah minimum yang
# diinginkan. Nilai kelembaban ini harus berada dalam rentang hingga.

# Buatlah kelas `SistemIrigasi` dengan atribut private `__kelembaban_target`.
#   • Sediakan Getter untuk `__kelembaban_target`.
#   • Sediakan Setter untuk `__kelembaban_target` yang membatasi nilai hanya antara dan (inklusif).

class SistemIrigasi:
    def __init__(self, kelembaban_target):
        self.__kelembaban_target = kelembaban_target
    
    # Getter → Kelembaban Target
    def getKelembabanTarget(self):
        return self.__kelembaban_target
    
    # Setter → Kelembaban Target
    def setKelembabanTarget(self, nilai_baru):
        MIN = 30
        MAX = 70

        if nilai_baru >= MIN and nilai_baru <= MAX:
            self.__kelembaban_target = nilai_baru
        else:
            print(f"❌ Nilai kelembaban harus antara {MIN} dan {MAX}")

if __name__ == "__main__":
    sittem_irigasi = SistemIrigasi(50)

    # Menampilkan kelembaban tanah
    print(
        f"Kelembaban tanah saat ini: "
        f"{sittem_irigasi.getKelembabanTarget()}"
    )

    # Mengubah kelembaban tanah
    sittem_irigasi.setKelembabanTarget(60)
    print(
        f"Kelembaban tanah saat ini: "
        f"{sittem_irigasi.getKelembabanTarget()}"
    )
    sittem_irigasi.setKelembabanTarget(70)
    print(
        f"Kelembaban tanah saat ini: "
        f"{sittem_irigasi.getKelembabanTarget()}"
    )

    # Mengubah kelembaban tanah tapi melebihi batas
    sittem_irigasi.setKelembabanTarget(80)
    print(
        f"Kelembaban tanah saat ini: "
        f"{sittem_irigasi.getKelembabanTarget()}"
    )
