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
        magazyn
