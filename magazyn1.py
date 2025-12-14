# Prosty magazyn – Python

magazyn = [
    "komputer",
    "drabina",
    "pralka",
    "młotek",
    "drukarka",
    "pralka"
]

def wyswietl():
    print("\n📦 Aktualny stan magazynu:")
    for towar in magazyn:
        print("-", towar)

def dodaj():
    towar = input("Podaj nazwę towaru do dodania: ")
    if towar:
        magazyn.append(towar)
        print("✅ Dodano:", towar)
    else:
        print("❌ Nie podano nazwy")

def usun():
    towar = input("Podaj nazwę towaru do usunięcia: ")
    if towar in magazyn:
        magazyn.remove(towar)
        print("🗑 Usunięto:", towar)
    else:
        print("❌ Towaru nie ma")

def sprawdz():
    towar = input("Podaj nazwę towaru do sprawdzenia: ")
    ilosc = magazyn.count(towar)
    print(f"🔍 Towar '{towar}' występuje {ilosc} razy")

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
