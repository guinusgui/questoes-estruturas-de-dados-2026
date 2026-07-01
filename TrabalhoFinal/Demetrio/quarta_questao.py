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

    # 1. Populando as estruturas
    Simbolo = namedtuple('Simbolo', ['palavra'])
    tabela_namedtuple = [Simbolo(p) for p in palavras]
    tabela_deque = deque(palavras)
    tabela_chainmap = ChainMap({p: True for p in palavras})

    alvos = [
        "Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang",
        "momentarily", "rubella", "vaccinations", "government", "Authorities"
    ]

    # ==========================================
    # BENCHMARK DE EXCLUSÃO
    # ==========================================
    
    # 1. Exclusão na Lista de namedtuple
    inicio = time.perf_counter()
    for alvo in alvos:
        # Precisamos encontrar o índice para deletar
        for i in range(len(tabela_namedtuple)):
            if tabela_namedtuple[i].palavra == alvo:
                del tabela_namedtuple[i] # Exclusão O(n) devido ao deslocamento de memória
                break
    tempo_nt = time.perf_counter() - inicio
    media_nt = tempo_nt / len(alvos)

    # 2. Exclusão no deque
    inicio = time.perf_counter()
    for alvo in alvos:
        try:
            tabela_deque.remove(alvo) # Busca O(n), mas exclusão de ponteiros é rápida
        except ValueError:
            pass # Ignora se a palavra não existir
    tempo_dq = time.perf_counter() - inicio
    media_dq = tempo_dq / len(alvos)

    # 3. Exclusão no ChainMap
    inicio = time.perf_counter()
    for alvo in alvos:
        try:
            del tabela_chainmap[alvo] # Exclusão via Hash O(1)
        except KeyError:
            pass
    tempo_cm = time.perf_counter() - inicio
    media_cm = tempo_cm / len(alvos)

    # ==========================================
    # RESULTADOS
    # ==========================================
    print("--- TEMPO MÉDIO DE EXCLUSÃO (por palavra) ---")
    print(f"ChainMap   : {media_cm:.8f} s")
    print(f"deque      : {media_dq:.8f} s")
    print(f"namedtuple : {media_nt:.8f} s")

    # ==========================================
    # GERAÇÃO DO GRÁFICO
    # ==========================================
    estruturas = ['ChainMap\n(Hash O(1))', 'deque\n(Busca + Ponteiro)', 'namedtuple\n(Busca + Deslocamento)']
    tempos_medios = [media_cm, media_dq, media_nt]

    plt.figure(figsize=(9, 6))
    barras = plt.bar(estruturas, tempos_medios, color=['green', 'orange', 'red'])
    
    plt.title("Tempo Médio de Exclusão (10 Palavras)", fontsize=14, pad=15)
    plt.ylabel("Tempo em segundos", fontsize=12)
    
    # Adiciona os valores numéricos no topo das barras
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + (max(tempos_medios)*0.01), 
                 f"{yval:.6f}s", ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
