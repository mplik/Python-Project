print("Witaj świecie!")
print("to jest drugi komunikat")
imie = input("Podaj swoje imię: ")
print("Cześć, " + imie + "!")
# Pobierz dwie liczby od użytkownika
a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

iloczyn = a * b

if iloczyn <= 100:
    print("Iloczyn liczb:", iloczyn)
else:
    suma = a + b
    print("Suma liczb:", suma)