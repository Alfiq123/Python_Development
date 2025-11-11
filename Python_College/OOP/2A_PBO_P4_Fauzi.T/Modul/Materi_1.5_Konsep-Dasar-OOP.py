from OOP3 import Titik

dataTitik = []
while True:
    print("Masukan data titik tanpa spasi, isikan 0 (nol) untuk mengakhiri")
    data = input("Nama > X,Y : ").split(">")
    if data[0] == "0":
        break

    nama = data[0]
    XY = data[1].split(",")
    koordinat = Titik(nama, int(XY[0]), int(XY[1]))
    dataTitik.append(koordinat)

for titik in dataTitik:
    titik.info()

print("Banyak Titik =", len(dataTitik), "\nJarak Antar Titik :\n\t ", end="")

for data in dataTitik:
    print(data.getNama(), end="\t")

for tik1 in dataTitik:
    print("\n", tik1.getNama(), sep="", end="\t")

    for tik2 in dataTitik:

        if tik1 == tik2:
            print("~\t", end="")
        else:
            jarak = tik1.getJarak(tik2)
            print(f"{jarak:.2f}", end="\t")
