import matplotlib.pyplot as plt

# Przykładowe dane – ceny domen w kolejnych dniach
dni = ["Pon", "Wt", "Śr", "Czw", "Pt"]
cena_domenaA = [100, 110, 105, 115, 120]
cena_domenaB = [90, 95, 93, 100, 99]

plt.plot(dni, cena_domenaA, marker="o", label="domenaA.pl")
plt.plot(dni, cena_domenaB, marker="s", label="domenaB.pl")
plt.title("Zmiany cen domen na giełdzie")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Cena [PLN]")
plt.legend()
plt.grid(True)
plt.savefig('ceny_domen.png')
plt.show()