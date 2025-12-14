import streamlit as st
import os

PLIK = "magazyn.txt"

# ===== Funkcje =====
def wczytaj_magazyn():
    if not os.path.exists(PLIK):
        return []
    with open(PLIK, "r", encoding="utf-8") as f:
        return [linia.strip() for linia in f if linia.strip()]

def zapisz_magazyn(lista):
    with open(PLIK, "w", encoding="utf-8") as f:
        for towar in lista:
            f.write(towar + "\n")

# ===== Aplikacja =====
st.title("📦 Prosty magazyn")

magazyn = wczytaj_magazyn()

st.subheader("Aktualny stan magazynu")
st.write(magazyn)

# ===== Dodawanie towaru =====
st.subheader("➕ Dodaj towar")
nowy = st.text_input("Nazwa towaru")

if st.button("Dodaj"):
    if nowy:
        magazyn.append(nowy)
        zapisz_magazyn(magazyn)
        st.success(f"Dodano: {nowy}")
        st.experimental_rerun()
    else:
        st.warning("Podaj nazwę towaru")

# ===== Usuwanie towaru =====
st.subheader("➖ Usuń towar")
usun = st.text_input("Nazwa towaru do usunięcia")

if st.button("Usuń"):
    if usun in magazyn:
        magazyn.remove(usun)
        zapisz_magazyn(magazyn)
        st.success(f"Usunięto: {usun}")
        st.experimental_rerun()
    else:
        st.error("Towaru nie ma w magazynie")

# ===== Liczenie towaru =====
st.subheader("🔍 Sprawdź ilość")
sprawdz = st.text_input("Nazwa towaru do sprawdzenia")

if st.button("Sprawdź"):
    ilosc = magazyn.count(sprawdz)
    st.info(f"Towar '{sprawdz}' występuje {ilosc} razy")
