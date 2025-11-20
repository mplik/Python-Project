import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 1, 5, 11]

plt.plot(x, y, marker="o")
plt.title("Przykładowy wykres")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.grid(True)
plt.savefig('wykres.png')  # zapisz wykres do pliku
plt.show()