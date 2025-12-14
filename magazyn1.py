# Prosty magazyn – towary z ilościami

magazyn = {
    "komputer": 5,
    "drabina": 2,
    "pralka": 3,
    "młotek": 10,
    "drukarka": 1
}

def wyswietl():
    print("\n📦 Stan magazynu:")
    for towar, ilosc in magazyn.items():
        print(f"- {towar}: {ilosc} szt.")

def dodaj():
    towar = input("Podaj nazwę towaru: ")
    try:
        ilosc = int(input("Podaj ilość: "))
    except ValueError:
        print("❌ Ilość musi być liczbą")
        return

    if towar in magazyn:
        magazyn[towar] += ilosc
    else:
        magazyn[towar] = ilosc

    print(f"✅ Dodano {ilosc} szt. towaru '{towar}'")

def usun():
    towar = input("Podaj nazwę towaru: ")
    if towar not in magazyn:
        print("❌ Towaru nie ma")
        return

    try:
        ilosc = int(input("Podaj ilość do usunięcia: "))
    except ValueError:
        print("❌ Ilość musi być liczbą")
        return

    if ilosc >= magazyn[towar]:
        del magazyn[towar]
        print(f"🗑 Usunięto cały towar '{towar}'")
    else:
        magazyn[towar] -= ilosc
        print(f"➖ Usunięto {ilosc} szt. towaru '{towar}'")

def sprawdz():
    towar = input("Podaj nazwę towaru: ")
    if towar in magazyn:
        print(f"🔍 {towar}: {magazyn[towar]} szt.")
    else:
        print("❌ Towaru nie ma")

def menu():
    while True:
        print("""
1 – Wyświetl magazyn
2 – Dodaj towar
3 – Usuń towar
4 – Sprawdź ilość
0 – Wyjście
""")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wyswietl()
        elif wybor == "2":
            dodaj()
        elif wybor == "3":
            usun()
        elif wybor == "4":
            sprawdz()
        elif wybor == "0":
            print("👋 Do widzenia")
            break
        else:
            print("❌ Nieprawidłowy wybór")

menu()
