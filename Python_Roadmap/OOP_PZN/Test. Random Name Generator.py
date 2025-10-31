from faker import Faker


class RandomGenerator:
    def __init__(self, fake_indo=Faker('id_ID')):
        self.fake_indo = fake_indo

    # Fake Nama Lengkap
    def random_nama_lengkap(self):
        print("=== NAMA LENGKAP ===")
        print(f"Nama Lengkap 1: {self.fake_indo.name()}\n"
              f"Nama Lengkap 2: {self.fake_indo.name()}\n"
              f"Nama Lengkap 3: {self.fake_indo.name()}\n")

    # Fake Nama Depan dan Belakang
    def random_nama_depan_belakang(self):
        print("=== NAMA DEPAN DAN BELAKANG ===")
        print(f"Nama Depan 1: {self.fake_indo.first_name()}\n"
              f"Nama Belakang 1: {self.fake_indo.last_name()}\n"
              f"Nama Depan 2: {self.fake_indo.first_name()}\n"
              f"Nama Belakang 2: {self.fake_indo.last_name()}\n")

    # Fake Alamat
    def random_alamat(self):
        print("=== ALAMAT ===")
        print(f"Alamat Lengkap 1: {self.fake_indo.address()}\n"
              f"Alamat Lengkap 2: {self.fake_indo.address()}\n"
              f"\n"
              f"Alamat Jalan 1: {self.fake_indo.street_address()}\n"
              f"Alamat Jalan 2: {self.fake_indo.street_address()}\n"
              f"\n"
              f"Alamat Kota 1: {self.fake_indo.city()}\n"
              f"Alamat Kota 2: {self.fake_indo.city()}\n")

    # Fake Company
    def random_company(self):
        print("=== COMPANY ===")
        print(f"Company 1: {self.fake_indo.company()}\n"
              f"Company 2: {self.fake_indo.company()}\n"
              f"Company 3: {self.fake_indo.company()}\n")

    # Fake Text
    def random_text(self):
        print("=== TEXT ===")
        print(f"Text 1: {self.fake_indo.text()}\n")

    # Fake Profile
    def random_profile(self):
        print("=== PROFILE ===")
        for i, j in self.fake_indo.profile().items():
            print(f"{i.capitalize()}: {j}")


if __name__ == "__main__":
    app = RandomGenerator()

    app.random_nama_lengkap()
    app.random_nama_depan_belakang()
    app.random_alamat()
    app.random_company()
    app.random_text()
    app.random_profile()
