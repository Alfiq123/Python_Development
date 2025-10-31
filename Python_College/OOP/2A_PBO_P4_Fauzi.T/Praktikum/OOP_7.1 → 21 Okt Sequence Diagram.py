from datetime import date


# 1. Kelas Induk: PegawaiRumahSakit
class PegawaiRumahSakit:
    """Kelas Induk untuk semua pegawai."""

    def __init__(self, id_pegawai, nama, tanggal_masuk):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.tanggal_masuk = tanggal_masuk

    def lihat_jadwal(self):
        return f"Pegawai {self.nama} melihat jadwal harian."

    def isi_absensi(self):
        return f"Pegawai {self.nama} berhasil mengisi absensi."


# 2. Kelas Anak 1: Dokter (Mewarisi PegawaiRumahSakit)
class Dokter(PegawaiRumahSakit):
    """Kelas Anak yang mewakili Dokter."""

    def __init__(self, id_pegawai, nama, tanggal_masuk, spesialisasi, no_izin_praktek):
        super().__init__(id_pegawai, nama, tanggal_masuk)
        # Memanggil konstruktor kelas induk
        self.spesialisasi = spesialisasi
        self.no_izin_praktek = no_izin_praktek

    def buat_diagnosis(self, gejala):
        print(f" Dokter {self.nama}: Menganalisis gejala:{gejala}")
        # Logika diagnosis sederhana
        if "demam" in gejala.lower() or "batuk" in gejala.lower():
            return "Flu Biasa"
        else:
            return "Diagnosis belum final, perlu tes lanjut."

    def resep_obat(self, diagnosis):
        print(f" Dokter {self.nama}: Membuat resep berdasarkan diagnosis '{diagnosis}'")
        if diagnosis == "Flu Biasa":
            return "Paracetamol dan Vitamin C"
        return "Instruksi: Tes Laboratorium"


# 3. Kelas Anak 2: StafAdministrasi (Mewarisi PegawaiRumahSakit)
class StafAdministrasi(PegawaiRumahSakit):
    """Kelas Anak yang mewakili Staf Administrasi."""

    def __init__(self, id_pegawai, nama, tanggal_masuk, area_tugas):
        super().__init__(id_pegawai, nama, tanggal_masuk)
        # Memanggil konstruktor kelas induk
        self.area_tugas = area_tugas

    def proses_pendaftaran(self, id_pasien):
        print(f" Staf Admin {self.nama}: Memeriksa janji untuk Pasien ID {id_pasien}")
        # Asumsi janji selalu ada
        return True

    def kelola_pembayaran(self, jumlah):
        return f" Staf Admin {self.nama}: Memproses pembayaran sejumlah Rp {jumlah}"


# Kelas Tambahan untuk Sequence
class Pasien:
    def __init__(self, id_pasien, nama):
        self.id_pasien = id_pasien
        self.nama = nama

    def jelaskan_gejala(self):
        return "Demam, Batuk, dan Sakit Kepala"  # Gejala Pasien

    def terima_resep(self, resep):
        print(f"\nPasien {self.nama}: Menerima resep: **{resep}**")


# --- Inisialisasi Objek ---
hari_ini = date.today()

dr_andi = Dokter(
    id_pegawai="D001",
    nama="Dr. Andi Pratama",
    tanggal_masuk=hari_ini,
    spesialisasi="Umum",
    no_izin_praktek="SIP-1234"
)
staf_ria = StafAdministrasi(
    id_pegawai="A005",
    nama="Ria Fitri",
    tanggal_masuk=hari_ini,
    area_tugas="Pendaftaran"
)
pasien_toni = Pasien(
    id_pasien="P101",
    nama="Toni Wijaya"
)
print("--- Start Sequence: Pelayanan Konsultasi ---")

# 1. Pasien -> Staf Administrasi: Konfirmasi Janji
print(f"Pasien {pasien_toni.nama}: Mendatangi Staf Administrasi.")
janji_status = staf_ria.proses_pendaftaran(
    id_pasien=pasien_toni.id_pasien
)

# Staf Administrasi.prosesPendaftaran()
if janji_status:
    print(f" Staf Admin {staf_ria.nama}: Janji dikonfirmasi. Silakan menunggu.")

# 2. Pasien dipanggil oleh Dokter (Simulasi Panggilan)
print(f"\n<< Konsultasi Dimulai >>")
gejala_pasien = pasien_toni.jelaskan_gejala()

# 3. Dokter (Self-Call): buatDiagnosis(gejala)
diagnosis = dr_andi.buat_diagnosis(
    gejala=gejala_pasien
)

# 4. Dokter (Self-Call): resepObat(diagnosis)
resep = dr_andi.resep_obat(
    diagnosis=diagnosis
)

# 5. Dokter -> Pasien: Berikan Resep dan Instruksi
pasien_toni.terima_resep(
    resep=resep
)

print("--- End Sequence ---")
