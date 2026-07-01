import re
import time
import matplotlib.pyplot as plt
from collections import UserList, UserDict, UserString

# ---------------------------------------------------------
# 1. Funções de Preparação
# ---------------------------------------------------------
def carregar_e_limpar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
        return re.findall(r'[^\W\d_]+', texto)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []

def popular_estruturas(palavras):
    print("Carregando estruturas para o teste de exclusão...\n")
    tabela_lista = UserList(palavras)
    
    tabela_dict = UserDict()
    for i, palavra in enumerate(palavras):
        tabela_dict[i] = palavra
        
    tabela_string = UserString(" ".join(palavras))
    return tabela_lista, tabela_dict, tabela_string

# ---------------------------------------------------------
# 2. Lógica de Exclusão e Medição de Tempo
# ---------------------------------------------------------
def realizar_exclusoes(tabela_lista, tabela_dict, tabela_string, palavras_alvo):
    print(f"Iniciando exclusão de {len(palavras_alvo)} palavras...\n")
    
    tempos_medios = [] # [Media_List, Media_Dict, Media_String]

    # --- Exclusão no UserList ---
    tempos_lista = []
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        try:
            # remove() apaga a primeira ocorrência da palavra
            tabela_lista.remove(alvo)
        except ValueError:
            pass # Ignora se a palavra não existir
        fim = time.perf_counter()
        tempos_lista.append(fim - inicio)
        
    media_lista = sum(tempos_lista) / len(palavras_alvo)
    tempos_medios.append(media_lista)
    print(f"Tempo MÉDIO Exclusão UserList:   {media_lista:.8f} segundos")

    # --- Exclusão no UserDict ---
    tempos_dict = []
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        # Passo 1: Descobrir a chave que contém o valor
        chave_para_apagar = None
        for k, v in tabela_dict.items():
            if v == alvo:
                chave_para_apagar = k
                break
                
        # Passo 2: Apagar a chave
        if chave_para_apagar is not None:
            del tabela_dict[chave_para_apagar]
        fim = time.perf_counter()
        tempos_dict.append(fim - inicio)
        
    media_dict = sum(tempos_dict) / len(palavras_alvo)
    tempos_medios.append(media_dict)
    print(f"Tempo MÉDIO Exclusão UserDict:   {media_dict:.8f} segundos")

    # --- Exclusão no UserString ---
    tempos_string = []
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        # Modificamos o .data diretamente. O "1" no final garante que 
        # apagaremos apenas a primeira ocorrência encontrada.
        tabela_string.data = tabela_string.data.replace(f" {alvo} ", " ", 1)
        fim = time.perf_counter()
        tempos_string.append(fim - inicio)
        
    media_string = sum(tempos_string) / len(palavras_alvo)
    tempos_medios.append(media_string)
    print(f"Tempo MÉDIO Exclusão UserString: {media_string:.8f} segundos")

    return tempos_medios

# ---------------------------------------------------------
# 3. Geração do Gráfico
# ---------------------------------------------------------
def plotar_grafico(tempos_medios):
    classes = ['UserList', 'UserDict', 'UserString']
    
    plt.figure(figsize=(8, 5))
    barras = plt.bar(classes, tempos_medios, color=['#E74C3C', '#F1C40F', '#8E44AD'])
    
    plt.title('Tempo Médio de Exclusão de Palavras por Classe', fontsize=14)
    plt.ylabel('Tempo Médio (Segundos)', fontsize=12)
    plt.xlabel('Estrutura de Dados', fontsize=12)
    
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.6f} s',
                 ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()

# --- Execução Principal ---
if __name__ == "__main__":
    arquivo = "leipzig100k.txt"
    alvos = [
        "Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", 
        "momentarily", "rubella", "vaccinations", "government", "Authorities"
    ]
    
    palavras_extraidas = carregar_e_limpar_arquivo(arquivo)
    
    if palavras_extraidas:
        t_lista, t_dict, t_string = popular_estruturas(palavras_extraidas)
        tempos = realizar_exclusoes(t_lista, t_dict, t_string, alvos)
        plotar_grafico(tempos)
