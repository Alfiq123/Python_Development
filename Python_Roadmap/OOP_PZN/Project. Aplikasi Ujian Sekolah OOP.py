from random import shuffle


class Soal:
    def __init__(self, pertanyaan, jawaban, jawaban_benar):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban
        self.jawaban_benar = jawaban_benar

        shuffle(self.jawaban)

    def cek_jawaban(self, jawaban_user):
        return jawaban_user == self.jawaban_benar


class SoalUjian:
    def __init__(self, soal_asli):
        self.daftar_soal = []

        shuffle(soal_asli)

        for i in range(10):
            soal = soal_asli[i]  # pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
            data = soal.split("|")  # ["pertanyaan", "jawaban1,jawaban2,jawaban3,jawaban4"]

            pertanyaan = data[0]  # pertanyaan
            semua_jawaban = data[1]  # "jawaban1,jawaban2,jawaban3,jawaban4"

            jawaban = semua_jawaban.split(",")  # ["jawaban1", "jawaban2", "jawaban3", "jawaban4"]
            jawaban_benar = jawaban[0]  # "jawaban1"

            soal = Soal(pertanyaan, jawaban, jawaban_benar)
            self.daftar_soal.append(soal)


class AplikasiUjianSekolah:
    def __init__(self, file_soal):
        soal_asli = []

        with open(file_soal, "r") as file:
            for line in file:
                soal_asli.append(line.strip())

        self.soal_ujian = SoalUjian(soal_asli)

    def run(self):
        opsi = ["A", "B", "C", "D"]

        jawaban_benar = 0
        jawaban_salah = 0

        for i in range(len(self.soal_ujian.daftar_soal)):
            soal = self.soal_ujian.daftar_soal[i]
            print("Pertanyaan", i + 1, ":", soal.pertanyaan)
            print("Jawaban:")

            for j in range(len(soal.jawaban)):
                jawaban = soal.jawaban[j]
                print(opsi[j], ".", jawaban)

            jawaban_user = input("Pilih jawaban (A/B/C/D): ").upper()
            jawaban_user_index = opsi.index(jawaban_user)
            jawaban_asli_user = soal.jawaban[jawaban_user_index]

            if soal.cek_jawaban(jawaban_asli_user):
                print("Jawaban benar\n")
                jawaban_benar += 1
            else:
                print("Jawaban salah\n")
                jawaban_salah += 1

        print("Hasil Ujian")
        print("Jawaban benar:", jawaban_benar)
        print("Jawaban salah:", jawaban_salah)
        print("Hasil Ujian:", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")


if __name__ == "__main__":
    app = AplikasiUjianSekolah(file_soal="Bank_Soal.txt")
    app.run()

    print("Program Selesai")
