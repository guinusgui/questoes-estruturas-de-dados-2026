import time
import re
import matplotlib.pyplot as plt
from collections import namedtuple, deque, ChainMap

def extrair_palavras(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    return [p for p in re.split(r'[\s\d\W_]+', texto) if p]

def main():
    caminho = "leipzig100k.txt"
    try:
        palavras = extrair_palavras(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado. Certifique-se de que 'leipzig100k.txt' está no diretório.")
        return

    # ==========================================
    # BENCHMARK DE INCLUSÃO
    # ==========================================
    
    # 1. Inclusão na Lista de namedtuple
    Simbolo = namedtuple('Simbolo', ['palavra'])
    tabela_namedtuple = []
    
    inicio = time.perf_counter()
    for p in palavras:
        tabela_namedtuple.append(Simbolo(p))
    tempo_nt = time.perf_counter() - inicio

    # 2. Inclusão no deque
    tabela_deque = deque()
    
    inicio = time.perf_counter()
    for p in palavras:
        tabela_deque.append(p)
    tempo_dq = time.perf_counter() - inicio

    # 3. Inclusão no ChainMap
    tabela_chainmap = ChainMap()
    
    inicio = time.perf_counter()
    for p in palavras:
        tabela_chainmap[p] = True
    tempo_cm = time.perf_counter() - inicio

    # ==========================================
    # RESULTADOS
    # ==========================================
    print(f"--- TEMPO TOTAL DE INCLUSÃO ({len(palavras)} palavras) ---")
    print(f"deque      : {tempo_dq:.6f} s")
    print(f"ChainMap   : {tempo_cm:.6f} s")
    print(f"namedtuple : {tempo_nt:.6f} s")

    # ==========================================
    # GERAÇÃO DO GRÁFICO
    # ==========================================
    estruturas = [
        'deque\n(O(1) C Nativo)', 
        'ChainMap\n(Cálculo de Hash)', 
        'namedtuple\n(Alocação de Objeto)'
    ]
    tempos = [tempo_dq, tempo_cm, tempo_nt]

    plt.figure(figsize=(9, 6))
    
    # Cores indicando a performance: Laranja (Mais rápido), Verde (Médio), Vermelho (Mais lento)
    barras = plt.bar(estruturas, tempos, color=['orange', 'green', 'red'])
    
    plt.title("Tempo Total de Inclusão (Aprox. 140.000 palavras)", fontsize=14, pad=15)
    plt.ylabel("Tempo em segundos", fontsize=12)
    
    # Adiciona os valores numéricos no topo das barras
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + (max(tempos)*0.01), 
                 f"{yval:.6f}s", ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
