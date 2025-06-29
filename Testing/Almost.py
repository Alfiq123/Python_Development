import json
from tabulate import tabulate

class Program:
    def __init__(self):
        self.filename = "Product_Lists_2.json"
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def user_validation(self, prompt):
        while True:
            try:
                valid_value = int(input(prompt))
                if valid_value < 0:
                    print("\nError: Nilai tidak boleh dibawah nol!\n")
                    continue
                return valid_value
            except ValueError:
                print("\nError: Input tidak valid! Masukkan angka bulat.\n")

    def display_data(self):
        if not self.data:
            print("\nInventori kosong.")
            return

        # Tambahkan peringatan stok rendah
        low_stock_items = []
        table = []
        for idx, item in enumerate(self.data, start=1):
            stock_warning = "⚠️" if item['kuantitas'] < 5 else ""
            table.append([
                idx,
                item['nama'],
                f"{item['kuantitas']} {stock_warning}",
                item['harga']
            ])
            if item['kuantitas'] < 5:
                low_stock_items.append(item['nama'])

        print(tabulate(table, headers=["ID", "Item", "Quantity", "Price"], tablefmt="fancy_grid"))
        
        # Tampilkan peringatan stok rendah
        if low_stock_items:
            print("\nPERINGATAN: Stok hampir habis untuk barang:")
            for item in low_stock_items:
                print(f"- {item}")

    def add_item(self):
        print("\n--- TAMBAH BARANG BARU ---")
        nama = input("Nama Barang: ").strip()
        kuantitas = self.user_validation("Kuantitas: ")
        harga = self.user_validation("Harga: ")
        
        self.data.append({
            "nama": nama,
            "kuantitas": kuantitas,
            "harga": harga
        })
        self.save_data()
        print(f"\n✅ {nama} berhasil ditambahkan!")

    def delete_item(self):
        self.display_data()
        if not self.data:
            return
            
        try:
            item_id = int(input("\nMasukkan ID barang yang akan dihapus: ")) - 1
            if 0 <= item_id < len(self.data):
                deleted = self.data.pop(item_id)
                self.save_data()
                print(f"\n✅ {deleted['nama']} berhasil dihapus!")
            else:
                print("\n❌ ID tidak valid!")
        except ValueError:
            print("\n❌ Input harus angka!")

    def search_item(self):
        keyword = input("\nCari barang: ").lower().strip()
        results = []
        
        for item in self.data:
            if keyword in item['nama'].lower():
                results.append(item)
                
        if not results:
            print("\n❌ Barang tidak ditemukan")
            return
            
        print(f"\n🔍 Hasil pencarian ({len(results)} item):")
        table = []
        for idx, item in enumerate(results, start=1):
            table.append([idx, item['nama'], item['kuantitas'], item['harga']])
        print(tabulate(table, headers=["ID", "Item", "Quantity", "Price"], tablefmt="fancy_grid"))

    def sort_items(self):
        if not self.data:
            print("\nInventori kosong.")
            return
            
        print("\nPilih metode pengurutan:")
        print("1. Berdasarkan Nama (A-Z)")
        print("2. Berdasarkan Kuantitas (terbanyak)")
        print("3. Berdasarkan Harga (termurah)")
        
        choice = input("Pilihan: ")
        
        if choice == "1":
            self.data.sort(key=lambda x: x['nama'].lower())
            print("\n✅ Berhasil diurutkan berdasarkan Nama")
        elif choice == "2":
            self.data.sort(key=lambda x: x['kuantitas'], reverse=True)
            print("\n✅ Berhasil diurutkan berdasarkan Kuantitas")
        elif choice == "3":
            self.data.sort(key=lambda x: x['harga'])
            print("\n✅ Berhasil diurutkan berdasarkan Harga")
        else:
            print("\n❌ Pilihan tidak valid!")
            return
            
        self.save_data()
        self.display_data()

    def main_menu(self):
        while True:
            print("\n" + "="*50)
            print("MANAJEMEN INVENTORI TOKO".center(50))
            print("="*50)
            print("1. Tampilkan Inventori")
            print("2. Tambah Barang")
            print("3. Hapus Barang")
            print("4. Cari Barang")
            print("5. Urutkan Barang")
            print("6. Keluar")
            
            choice = input("\nPilih menu: ")
            
            if choice == "1":
                self.display_data()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.search_item()
            elif choice == "5":
                self.sort_items()
            elif choice == "6":
                print("\nTerima kasih. Program selesai!")
                break
            else:
                print("\n❌ Pilihan tidak valid!")

class QuickSorter:
    def __init__(self, arr):
        """
        Inisialisasi objek QuickSorter dengan array yang akan diurutkan.
        Kita membuat salinan array untuk menghindari modifikasi array asli
        jika diinginkan, atau langsung bekerja pada referensi jika tidak.
        Untuk contoh ini, kita akan memodifikasi array in-place.
        """
        self.arr = arr

    def partition(self, low, high):
        """
        Metode helper untuk partisi array.
        Ini adalah metode internal (diawali dengan underscore) karena
        biasanya tidak dipanggil langsung dari luar kelas.
        """
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def sort(self):
        """
        Metode publik untuk memulai proses pengurutan QuickSort secara iteratif.
        """
        if not self.arr:
            return []

        stack = [(0, len(self.arr) - 1)]

        while stack:
            low, high = stack.pop()

            if low < high:
                pi = self.partition(low, high)

                # Dorong subarray kanan ke stack terlebih dahulu untuk optimasi
                # (memastikan subarray yang lebih kecil diproses lebih dulu,
                # tapi ini bukan keharusan mutlak untuk kebenaran algoritma)
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))
        return self.arr

if __name__ == "__main__":
    Program().main_menu()