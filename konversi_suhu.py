
while True:
    print("\n---------------------------------------------------------")
    print("Program Konversi Suhu\n"
          "1. Celcius ke Fahrenheit\n"
          "2. Celcius ke Kelvin\n"
          "3. Celcius ke Reamur\n"
          "4. Exit\n"
          "Pilih Operasi")
    menu = input()
    print("---------------------------------------------------------\n")

    if menu == "1":
        celcius = int(input("Masukkan Derajat Celcius\n"))
        fahrenheit = (celcius*9/5)+32
        print(f"{celcius} derajat Celcius sama dengan {fahrenheit} "
              f"derajat fahrenheit")
    elif menu == "2":
        celcius = int(input("Masukkan Derajat Celcius\n"))
        kelvin = celcius + 273
        print(f"{celcius} derajat Celcius sama dengan {kelvin} "
              f"derajat kelvin")
    elif menu == "3":
        celcius = int(input("Masukkan Derajat Celcius\n"))
        reamur = celcius * 4/5
        print(f"{celcius} derajat Celcius sama dengan {reamur} "
              f"derajat reamur")
    elif menu == "4":
        break
    else:
        print("Operasi Invalid")

