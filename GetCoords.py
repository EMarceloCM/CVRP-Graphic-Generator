import numpy as np

def coordenadas_formatadas(caminho_arquivo):
    coordenadas = []
    with open("cod.txt", 'r') as f:
        leitura = False
        for linha in f:
            if linha.strip() == 'NODE_COORD_SECTION':
                leitura = True
                continue
            if leitura:
                partes = linha.strip().split()
                if len(partes) >= 3:
                    x = float(partes[1])
                    y = float(partes[2])
                    coordenadas.append(f"[{x}, {y}]")
    return ', '.join(coordenadas)

coords = coordenadas_formatadas("coordenadas.txt")
print(coords)