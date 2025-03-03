import matplotlib.pyplot as plt
import numpy as np

coordenadas = {
    0: (35, 35),
    1: (41, 49),
    2: (35, 17),
    3: (55, 45),
    4: (55, 20),
    5: (15, 30),
    6: (25, 30),
    7: (20, 50),
    8: (10, 43),
    9: (55, 60),
}

rotas = [
    ("Rota 1", [0, 4, 5, 0]),
    ("Rota 2", [0, 1, 2, 3, 0]),
    ("Rota 3", [0, 6, 0]),
]

plt.figure(figsize=(8, 6))

cores = plt.cm.get_cmap("tab10", len(rotas))

for i, (nome_rota, pontos) in enumerate(rotas):
    xs, ys = zip(*[coordenadas[p] for p in pontos])
    plt.plot(xs, ys, marker="o", linestyle="-", color=cores(i), label=nome_rota)

for idx, (x, y) in coordenadas.items():
    if idx == 0:
        plt.scatter(x, y, color="red", s=150, marker="s", label="Depósito")  # Depósito quadrado vermelho
        plt.text(x, y+2.5, "0", fontsize=8, ha="center", va="center", color="black")
    else:
        plt.scatter(x, y, color="black", s=50, marker="o")  # Clientes pretos
        plt.text(x-0.2, y+1.7, str(idx), fontsize=8, ha="center", va="center", color="black")

plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Solução PRVC - Rotas Geradas")
plt.legend()
plt.grid()

plt.show()
