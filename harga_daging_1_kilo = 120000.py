harga_daging_1_kilo = 120000

jumlah = input("Masukkan jumlah kilo daging (ketik 'cukup' untuk selesai): ")

while jumlah.lower() != "cukup":
    jumlah_kilo = int(jumlah)

    total_harga = harga_daging_1_kilo * jumlah_kilo
    print("Total harga yang harus dibayar:", total_harga)

    if jumlah_kilo >= 5:
        print("Anda mendapatkan diskon 7000!")
        total_harga -= 7000
        print("Total harga setelah diskon:", total_harga)

    elif jumlah_kilo >= 2:
        print("Anda mendapatkan diskon 5000!")
        total_harga -= 5000
        print("Total harga setelah diskon:", total_harga)

    else:
        print("Tidak ada diskon yang diberikan.")

    jumlah = input("\nMasukkan jumlah kilo lagi (ketik 'cukup' untuk selesai): ")

print("Terima kasih telah berbelanja.")
