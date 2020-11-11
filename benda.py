histori = []

while True:
    print("\n----------------------------------------------------------"
          "------------------------")
    print("Program Penghitung Pemuaian Panjang Benda Padat\n"
          "1. Hitung Pemuaian Panjang\n"
          "2. Lihat Histori \n"
          "3. Exit\n"
          "Pilih Operasi ")

    menu = input()
    print("------------------------------------------------------------"
          "----------------------")

    if menu == "1":
        nama = input("Masukkan Nama Benda = ")
        panjang = float(input("Masukkan Panjang Mula Mula = "))
        koefisien = float(input("Masukkan Koefisien = "))
        suhu_mula = int(input("Masukkan Suhu Mula (Dalam C) = "))
        suhu_akhir = int(input("Masukkan Suhu Akhir (Dalam C) = "))
        hasil = panjang * koefisien * (suhu_akhir - suhu_mula)
        histori += [
            [nama, panjang, koefisien, suhu_mula, suhu_akhir, hasil]
        ]
        print(f"\nSebuah {nama} dengan koefisien {koefisien} memiliki "
              f"panjang {panjang} satuan.\nPemuaian panjang {nama} itu "
              f"jika suhu berubah dari {suhu_mula}C menjadi {suhu_akhir}C"
              f"\nadalah {hasil} satuan")

    elif menu == "2":
        for i in histori:
            print(f"\nSebuah {i[0]} dengan koefisien {i[2]} memiliki"
                  f" panjang {i[1]} satuan.\nPemuaian panjang {i[0]} itu "
                  f"jika suhu berubah dari {i[3]}C menjadi {i[4]}C\n"
                  f"adalah {i[5]} satuan ")

    elif menu == "3":
        break
    else:
        print("Operasi Invalid")
