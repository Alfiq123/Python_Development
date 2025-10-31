# Parent
class Aset:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga


class AsetKendaraan(Aset):
    def __init__(self, kode, nama, harga, stnk, tahun):
        super().__init__(kode, nama, harga)
        self.stnk = stnk
        self.tahun = tahun


class AsetElektronik(Aset):
    def __init__(self, kode, nama, harga, nomor_serial):
        super().__init__(kode, nama, harga)
        self.nomor_serial = nomor_serial


class AsetTanahBangunan(Aset):
    def __init__(self, kode, nama, harga, sertifikat, njop, luas):
        super().__init__(kode, nama, harga)
        self.sertifikat = sertifikat
        self.njop = njop
        self.luas = luas


class DaftarAset:
    def __init__(self):
        self.daftar_aset = []

    def tambah_aset(self, aset):
        self.daftar_aset.append(aset)

    def ambil_aset(self, kode):
        for aset in self.daftar_aset:
            if aset.kode == kode:
                return aset
        return None

    def hapus_aset(self, kode):
        for i, aset in enumerate(self.daftar_aset):
            if aset.kode == kode:
                del self.daftar_aset[i]
                return True
        return False


class AplikasiAsetManagemen:
    def __init__(self):
        self.daftar_aset = DaftarAset()

    def run(self):
        while True:
            print("=== Aplikasi Managemen Aset ===\n"
                  "  1. Tambah Aset\n"
                  "  2. Lihat Daftar Aset\n"
                  "  3. Keluar\n")

            pilih = int(input("Pilih Menu: "))

            if pilih == 1:
                self.run_tambah_aset()
            elif pilih == 2:
                self.run_lihat_daftar_aset()
            elif pilih == 3:
                break

    def run_tambah_aset(self):
        while True:
            print("=== Menambah Aset ===\n"
                  "  1. Tambah Kendaraan\n"
                  "  2. Tambah Elektronik\n"
                  "  3. Tambah Tanah Bangunan\n"
                  "  4. Kembali\n")

            pilih = int(input("Pilih Menu: "))

            if pilih == 1:
                self.run_tambah_aset_kendaraan()
            elif pilih == 2:
                self.run_tambah_aset_elektronik()
            elif pilih == 3:
                self.run_tambah_aset_tanah_bangunan()
            elif pilih == 4:
                break

    def run_lihat_daftar_aset(self):
        for aset in self.daftar_aset.daftar_aset:
            if isinstance(aset, AsetKendaraan):
                print(f"Aset Kendaraan\n"
                      f"  - Kode: {aset.kode}\n"
                      f"  - Nama: {aset.nama}\n"
                      f"  - Harga: {aset.harga}\n"
                      f"  - STNK: {aset.stnk}\n"
                      f"  - Tahun: {aset.tahun}\n")

            elif isinstance(aset, AsetElektronik):
                print(f"Aset Elektronik\n"
                      f"  - Kode: {aset.kode}\n"
                      f"  - Nama: {aset.nama}\n"
                      f"  - Harga: {aset.harga}\n"
                      f"  - Nomor Serial: {aset.nomor_serial}\n")

            elif isinstance(aset, AsetTanahBangunan):
                print(f"Aset Tanah Bangunan\n"
                      f"  - Kode: {aset.kode}\n"
                      f"  - Nama: {aset.nama}\n"
                      f"  - Harga: {aset.harga}\n"
                      f"  - Sertifikat: {aset.sertifikat}\n"
                      f"  - NJOP: {aset.njop}\n"
                      f"  - Luas: {aset.luas} m\n")

            print("Menu"
                  "  1. Ubah Aset\n"
                  "  2. Hapus Aset\n"
                  "  3. Kembali\n")

            pilih = int(input("Pilih Menu: "))

            if pilih == 1:
                self.run_ubah_aset()
            elif pilih == 2:
                self.run_hapus_aset()

    def run_tambah_aset_kendaraan(self):
        print("Tambah Aset Kendaraan")

        kode = str(input("Kode: "))
        nama = str(input("Nama: "))
        harga = int(input("Harga: "))
        stnk = str(input("STNK: "))
        tahun = int(input("Tahun: "))

        aset_kendaraan = AsetKendaraan(kode, nama, harga, stnk, tahun)
        self.daftar_aset.tambah_aset(aset_kendaraan)

    def run_tambah_aset_elektronik(self):
        print("Tambah Aset Elektronik")

        kode = str(input("Kode: "))
        nama = str(input("Nama: "))
        harga = int(input("Harga: "))
        nomor_serial = int(input("Nomor Serial: "))

        aset_elektronik = AsetElektronik(kode, nama, harga, nomor_serial)
        self.daftar_aset.tambah_aset(aset_elektronik)

    def run_tambah_aset_tanah_bangunan(self):
        print("Tambah Aset Tanah Bangunan")

        kode = str(input("Kode: "))
        nama = str(input("Nama: "))
        harga = int(input("Harga: "))
        sertifikat = str(input("Sertifikat: "))
        njop = str(input("NJOP: "))
        luas = int(input("Luas: "))

        aset_tanah_bangunan = AsetTanahBangunan(kode, nama, harga, sertifikat, njop, luas)
        self.daftar_aset.tambah_aset(aset_tanah_bangunan)

    def run_ubah_aset(self):
        print("Ubah Aset")

        kode = str(input("Kode: "))
        aset = self.daftar_aset.ambil_aset(kode)

        if aset is None:
            print(f"Aset tidak ditemukan, Kode: {kode}")
        else:
            if isinstance(aset, AsetKendaraan):
                nama = str(input("Nama: "))
                harga = int(input("Harga: "))
                stnk = str(input("STNK: "))
                tahun = int(input("Tahun: "))

                aset.nama = nama
                aset.harga = harga
                aset.stnk = stnk
                aset.tahun = tahun

                print("Aset berhasil diubah")

    def run_hapus_aset(self):
        print("Hapus Aset")

        kode = str(input("Kode: "))

        if self.daftar_aset.hapus_aset(kode):
            print("Aset berhasil dihapus")
        else:
            print(f"Aset tidak ditemukan, Kode: {kode}")


if __name__ == "__main__":
    app = AplikasiAsetManagemen()
    app.run()

    print("Program Selesai")
