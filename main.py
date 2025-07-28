import tkinter as tk

def pokaz_tekst():
    tekst = pole_tekstowe.get()
    etykieta_wynik.config(text=f"Wpisałeś: {tekst}")

okno = tk.Tk()
okno.title("Prosty program GUI")

pole_tekstowe = tk.Entry(okno, width=30)
pole_tekstowe.pack(pady=10)

przycisk = tk.Button(okno, text="Wyświetl", command=pokaz_tekst)
przycisk.pack(pady=5)

etykieta_wynik = tk.Label(okno, text="")
etykieta_wynik.pack(pady=10)

okno.mainloop()