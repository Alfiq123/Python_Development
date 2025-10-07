class HewanPeliharaan:
    def __init__(self, persen):
        self._persen = persen

    def hitung_pakan(self, berat_badan):
        return berat_badan * self._persen


class Kucing(HewanPeliharaan):
    def __init__(self):
        super().__init__(persen=0.02)


class Anjing(HewanPeliharaan):
    def __init__(self):
        super().__init__(persen=0.03)


if __name__ == "__main__":
    kucing_1 = Kucing()
    anjing_1 = Anjing()

    print(
        "\n"
        "Kebutuhan Pakan Kucing: "
        f"{kucing_1.hitung_pakan(berat_badan=4000):,.0f} Gram\n"

        "Kebutuhan Pakan Anjing: "
        f"{anjing_1.hitung_pakan(berat_badan=15000):,.0f} Gram\n"
    )
