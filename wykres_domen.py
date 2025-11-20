import pandas as pd
import plotly.express as px

# Przykładowe dane — plik CSV jak poprzednio
dane = pd.read_csv('ceny_domen.csv')

fig = px.bar(
    dane,
    x="domena",
    y="cena",
    title="Ceny domen",
    labels={"domena": "Domena", "cena": "Cena (PLN)", "status": "Status"},
    color="status",  # Pokoloruj słupki według statusu
    hover_data=["status"],  # Pokaż status w tooltip
)

# Interaktywność — domyślnie jest włączona!
fig.show()  # Otworzy wykres w przeglądarce

# Jeśli chcesz mieć wykres jako plik HTML do samodzielnego otwarcia:
fig.write_html("wykres_interaktywny.html")