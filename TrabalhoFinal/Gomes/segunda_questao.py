import re
import time
from pathlib import Path
from collections import Counter, OrderedDict, defaultdict


import matplotlib.pyplot as plt



def extrair_palavras(caminho_arquivo: str):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    return [palavra for palavra in re.split(r"[\s\d\W_]+", texto) if palavra]


def benchmark_counter(palavras):
    estrutura = Counter()
    inicio = time.perf_counter()
    for palavra in palavras:
        estrutura[palavra] += 1
    return estrutura, time.perf_counter() - inicio


def benchmark_ordered_dict(palavras):
    estrutura = OrderedDict()
    inicio = time.perf_counter()
    for palavra in palavras:
        estrutura[palavra] = estrutura.get(palavra, 0) + 1
    return estrutura, time.perf_counter() - inicio


def benchmark_defaultdict(palavras):
    estrutura = defaultdict(int)
    inicio = time.perf_counter()
    for palavra in palavras:
        estrutura[palavra] += 1
    return estrutura, time.perf_counter() - inicio


def main():
    caminho = Path(__file__).resolve().parent / "leipzig100k.txt"

    if not caminho.exists():
        print("Arquivo não encontrado. Coloque 'leipzig100k.txt' na pasta do script.")
        return

    palavras = extrair_palavras(str(caminho))

    counter, tempo_counter = benchmark_counter(palavras)
    ordered_dict, tempo_ordered = benchmark_ordered_dict(palavras)
    default_dict, tempo_defaultdict = benchmark_defaultdict(palavras)

    print(f"--- BENCHMARK DE INSERÇÃO DE PALAVRAS ({len(palavras)} palavras) ---")
    print(f"Counter       : {tempo_counter:.6f} s")
    print(f"OrderedDict   : {tempo_ordered:.6f} s")
    print(f"defaultdict   : {tempo_defaultdict:.6f} s")
    print(f"Quantidade de chaves únicas: Counter={len(counter)}, OrderedDict={len(ordered_dict)}, defaultdict={len(default_dict)}")

    
    estruturas = [
        "Counter\n(O(1) com hash)",
        "OrderedDict\n(Ordem preservada)",
        "defaultdict\n(Valor padrão)",
    ]
    tempos = [tempo_counter, tempo_ordered, tempo_defaultdict]

    plt.figure(figsize=(9, 6))
    barras = plt.bar(estruturas, tempos, color=["orange", "green", "red"])

    plt.title("Tempo Total de Inclusão (Aprox. 2.1M palavras)", fontsize=14, pad=15)
    plt.ylabel("Tempo em segundos", fontsize=12)

    for barra in barras:
        yval = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width() / 2,
            yval + (max(tempos) * 0.01),
            f"{yval:.6f}s",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

    