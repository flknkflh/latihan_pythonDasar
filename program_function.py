import json


# Fungsi untuk membaca JSON
def baca_json(nama_file):
    with open(nama_file, "r") as file:
        return json.load(file)


# Fungsi 1 : Menampilkan menu ke layar
def tampilkan_menu(harga_daging):
    print("\n=== DAFTAR HARGA DAGING ===")
    for jenis, harga in harga_daging.items():
        print(f"{jenis.capitalize():<10} : Rp{harga:,.0f}/kg")


# Fungsi 2 : Menghitung diskon
def hitung_diskon(jenis_daging, jumlah_kilo, subtotal):
    # Nested IF
    if jenis_daging == "ayam":
        if jumlah_kilo >= 5:
            diskon = subtotal * 0.10
            print("Diskon 10% untuk pembelian ayam minimal 5 kg")
        else:
            diskon = 0

    elif jenis_daging == "sapi":
        if jumlah_kilo >= 2:
            diskon = subtotal * 0.15
            print("Diskon 15% untuk pembelian sapi minimal 2 kg")
        else:
            diskon = 0

    elif jenis_daging == "babi":
        if jumlah_kilo >= 3:
            diskon = subtotal * 0.12
            print("Diskon 12% untuk pembelian babi minimal 3 kg")
        else:
            diskon = 0

    return diskon


# Fungsi 3 : Fungsi utama aplikasi kasir
def jalankan_kasir():
    harga_daging = baca_json("harga_daging.json")

    # Variabel untuk nota
    total_kotor = 0
    total_diskon = 0
    transaksi = []

    tampilkan_menu(harga_daging)

    while True:
        jenis_daging = input(
            "\nMasukkan jenis daging (sapi/ayam/babi) (ketik 'cukup' untuk selesai)👌: "
        ).lower()

        if jenis_daging == "cukup":
            break

        if jenis_daging not in harga_daging:
            print("Jenis daging tidak tersedia!🤷‍♂️")
            continue

        while True:
            jumlah = input("Masukkan jumlah kilo (ketik 'cukup' untuk selesai)👌: ")

            if jumlah.lower() == "cukup":
                break

            try:
                jumlah_kilo = float(jumlah)
                break
            except ValueError:
                print("Salah input! Masukkan angka, misalnya 2 atau 2.5.🙊")

        harga = harga_daging[jenis_daging]
        subtotal = harga * jumlah_kilo

        diskon = hitung_diskon(jenis_daging, jumlah_kilo, subtotal)

        total_bayar = subtotal - diskon

        print(f"\nHarga            : Rp{harga:,.0f}/kg")
        print(f"Jumlah           : {jumlah_kilo} kg")
        print(f"Subtotal         : Rp{subtotal:,.0f}")
        print(f"Diskon           : Rp{diskon:,.0f}")
        print(f"Total Bayar      : Rp{total_bayar:,.0f}")

        transaksi.append({
            "jenis": jenis_daging,
            "harga": harga,
            "jumlah": jumlah_kilo,
            "subtotal": subtotal,
            "diskon": diskon,
            "total": total_bayar
        })

        # Akumulasi untuk nota
        total_kotor += subtotal
        total_diskon += diskon

    # Cetak nota
    total_bersih = total_kotor - total_diskon

    print("\n" + "=" * 65)
    print("                     NOTA PEMBAYARAN")
    print("=" * 65)
    print(f"{'No':<4}{'Jenis':<10}{'Kg':>8}{'Harga/Kg':>15}{'Subtotal':>15}")
    print("-" * 65)

    for i, item in enumerate(transaksi, start=1):
        print(f"{i:<4}"
              f"{item['jenis']:<10}"
              f"{item['jumlah']:>8.2f}"
              f"{item['harga']:>15,.0f}"
              f"{item['subtotal']:>15,.0f}")

    print("-" * 65)
    print(f"{'Total Belanja Kotor':<35}: Rp{total_kotor:>15,.0f}")
    print(f"{'Total Diskon':<35}: Rp{total_diskon:>15,.0f}")
    print(f"{'Total Bersih':<35}: Rp{total_bersih:>15,.0f}")
    print("=" * 65)
    print("        Terima kasih telah berbelanja.")
    print("=" * 65)


if __name__ == "__main__":
    jalankan_kasir()