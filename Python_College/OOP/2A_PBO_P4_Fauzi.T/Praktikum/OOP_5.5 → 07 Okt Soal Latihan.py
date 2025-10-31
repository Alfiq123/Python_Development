# Soal 5: Analisis Investasi

# Buat fungsi polimorfik `analisis_return(objek_investasi)`
# yang menerima objek dari kelas `InvestasiTernak`
# dan memanggil metode `hitung_return_tahunan()`.

# Buat subclass `InvestasiDomba` dan `InvestasiBebek`
# yang mengimplementasikan metode tersebut.

# • `InvestasiDomba`: Return.
# • `InvestasiBebek`: Return.

# Tugas: Analisis return untuk investasi domba (Modal Rp 10.000.000,00)
#        dan investasi bebek (Modal Rp 5.000.000,00).

class InvestasiTernak:
    def __init__(self, modal): self.modal = modal
    def hitung_return_tahunan(self):
        raise NotImplementedError("Harus diimplementasikan di subclass.")


class InvestasiDomba(InvestasiTernak):
    def __init__(self): super().__init__(modal=10000000)
    def hitung_return_tahunan(self): return self.modal * 0.15


class InvestasiBebek(InvestasiTernak):
    def __init__(self): super().__init__(modal=5000000)
    def hitung_return_tahunan(self): return self.modal * 0.10


def analisis_return(objek_investasi):
    hasil = objek_investasi.hitung_return_tahunan()
    print(f"Modal: Rp {objek_investasi.modal:,.0f}")
    print(f"Return Tahunan: Rp {hasil:,.0f}\n")


if __name__ == "__main__":
    invest_domba = InvestasiDomba()
    invest_bebek = InvestasiBebek()

    print("═════ Analisis Investasi Domba ═════")
    analisis_return(invest_domba)

    print("═════ Analisis Investasi Bebek ═════")
    analisis_return(invest_bebek)
