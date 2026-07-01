import re
import time
from pathlib import Path
from collections import Counter, OrderedDict, defaultdict

import matplotlib.pyplot as plt


def extrair_palavras(caminho_arquivo: str):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    return [palavra for palavra in re.split(r"[\s\d\W_]+", texto) if palavra]


def benchmark_busca_counter(palavras, alvos):
    estrutura = Counter(palavras)
    inicio = time.perf_counter()
    for alvo in alvos:
        estrutura.get(alvo)
    return time.perf_counter() - inicio


def benchmark_busca_ordered_dict(palavras, alvos):
    estrutura = OrderedDict((palavra, True) for palavra in palavras)
    inicio = time.perf_counter()
    for alvo in alvos:
        estrutura.get(alvo)
    return time.perf_counter() - inicio


def benchmark_busca_defaultdict(palavras, alvos):
    estrutura = defaultdict(bool)
    for palavra in palavras:
        estrutura[palavra] = True

    inicio = time.perf_counter()
    for alvo in alvos:
        estrutura.get(alvo)
    return time.perf_counter() - inicio


def main():
    caminho = Path(__file__).resolve().parent / "leipzig100k.txt"

    if not caminho.exists():
        print("Arquivo não encontrado. Coloque 'leipzig100k.txt' na pasta do script.")
        return

    palavras = extrair_palavras(str(caminho))
    alvos = [
        "Lisbon",
        "NASA",
        "Kyunghee",
        "Konkuk",
        "Sogang",
        "momentarily",
        "rubella",
        "vaccinations",
        "government",
        "Authorities",
    ]

    tempo_counter = benchmark_busca_counter(palavras, alvos)
    tempo_ordered = benchmark_busca_ordered_dict(palavras, alvos)
    tempo_defaultdict = benchmark_busca_defaultdict(palavras, alvos)

    media_counter = tempo_counter / len(alvos)
    media_ordered = tempo_ordered / len(alvos)
    media_defaultdict = tempo_defaultdict / len(alvos)

    print("--- TEMPO MÉDIO DE BUSCA (por palavra) ---")
    print(f"Counter       : {media_counter:.8f} s")
    print(f"OrderedDict   : {media_ordered:.8f} s")
    print(f"defaultdict   : {media_defaultdict:.8f} s")

    estruturas = [
        "Counter\n(Hash O(1))",
        "OrderedDict\n(Busca por chave)",
        "defaultdict\n(Valor padrão)",
    ]
    tempos_medios = [media_counter, media_ordered, media_defaultdict]

    plt.figure(figsize=(9, 6))
    barras = plt.bar(estruturas, tempos_medios, color=["green", "orange", "red"])

    plt.title("Tempo Médio de Busca (10 Consultas)", fontsize=14, pad=15)
    plt.ylabel("Tempo em segundos", fontsize=12)

    for barra in barras:
        yval = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            yval + (max(tempos_medios) * 0.01),
            f"{yval:.8f}s",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
