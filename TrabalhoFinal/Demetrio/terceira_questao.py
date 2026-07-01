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
        print("Arquivo não encontrado.")
        return

    # 1. Populando as estruturas (conforme exercício anterior)
    Simbolo = namedtuple('Simbolo', ['palavra'])
    tabela_namedtuple = [Simbolo(p) for p in palavras]
    tabela_deque = deque(palavras)
    tabela_chainmap = ChainMap({p: True for p in palavras})

    # Palavras a serem buscadas
    alvos = [
        "Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang",
        "momentarily", "rubella", "vaccinations", "government", "Authorities"
    ]

    # ==========================================
    # BENCHMARK DE BUSCA
    # ==========================================
    
    # 1. Busca na Lista de namedtuple
    inicio = time.perf_counter()
    for alvo in alvos:
        # Busca linear comparando atributos
        encontrado = any(obj.palavra == alvo for obj in tabela_namedtuple)
    tempo_nt = time.perf_counter() - inicio
    media_nt = tempo_nt / len(alvos)

    # 2. Busca no deque
    inicio = time.perf_counter()
    for alvo in alvos:
        # Busca linear nativa em C
        encontrado = alvo in tabela_deque
    tempo_dq = time.perf_counter() - inicio
    media_dq = tempo_dq / len(alvos)

    # 3. Busca no ChainMap
    inicio = time.perf_counter()
    for alvo in alvos:
        # Busca por Hash O(1)
        encontrado = alvo in tabela_chainmap
    tempo_cm = time.perf_counter() - inicio
    media_cm = tempo_cm / len(alvos)

    # ==========================================
    # RESULTADOS
    # ==========================================
    print("--- TEMPO MÉDIO DE BUSCA (por palavra) ---")
    print(f"ChainMap   : {media_cm:.8f} s")
    print(f"deque      : {media_dq:.8f} s")
    print(f"namedtuple : {media_nt:.8f} s")

    # ==========================================
    # GERAÇÃO DO GRÁFICO
    # ==========================================
    estruturas = ['ChainMap\n(Hash O(1))', 'deque\n(Busca C O(n))', 'namedtuple\n(Busca Python O(n))']
    tempos_medios = [media_cm, media_dq, media_nt]

    plt.figure(figsize=(9, 6))
    barras = plt.bar(estruturas, tempos_medios, color=['green', 'orange', 'red'])
    
    plt.title("Tempo Médio de Busca (10 Consultas)", fontsize=14, pad=15)
    plt.ylabel("Tempo em segundos", fontsize=12)
    
    # Adiciona os valores no topo de cada barra para melhor visualização
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + (max(tempos_medios)*0.01), 
                 f"{yval:.6f}s", ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
