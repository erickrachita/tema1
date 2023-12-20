import pandas as pd
import matplotlib.pyplot as plt

# Citeste datele din fisierul CSV
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Ploteaza toate valorile
plt.figure(figsize=(10, 6))
data.plot(title='Toate Valorile')
plt.show()

# Ploteaza primele X valori
X = 30  # Schimba valoarea lui X la numarul dorit de valori pe care vrei sa le afisezi
plt.figure(figsize=(10, 6))
data.head(X).plot(title=f'Primele {X} Valori')
plt.show()

# Ploteaza ultimele Y valori pentru coloanele Durata si Puls
Y = 20  # Schimba valoarea lui Y la numarul dorit de valori pe care vrei sa le afisezi
selected_data = data[['Durata', 'Puls']].tail(Y)
plt.figure(figsize=(10, 6))
selected_data.plot(title=f'Ultimele {Y} Valori pentru Durata si Puls')
plt.show()