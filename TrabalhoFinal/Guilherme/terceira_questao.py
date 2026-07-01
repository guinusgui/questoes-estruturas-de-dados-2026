import re
import time
import matplotlib.pyplot as plt
from collections import UserList, UserDict, UserString

# ---------------------------------------------------------
# 1. Funções de Preparação (Reaproveitadas da Etapa Anterior)
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
    print("Carregando estruturas na memória (isso pode levar alguns segundos)...")
    
    tabela_lista = UserList(palavras)
    
    tabela_dict = UserDict()
    for i, palavra in enumerate(palavras):
        tabela_dict[i] = palavra
        
    # Usando .join para otimizar a criação da string base
    tabela_string = UserString(" ".join(palavras))
    
    print("Estruturas prontas!\n")
    return tabela_lista, tabela_dict, tabela_string

# ---------------------------------------------------------
# 2. Lógica de Busca e Medição de Tempo
# ---------------------------------------------------------
def realizar_buscas(tabela_lista, tabela_dict, tabela_string, palavras_alvo):
    print(f"Iniciando busca pelas {len(palavras_alvo)} palavras...\n")
    
    tempos_medios = [] # Guardará [Media_List, Media_Dict, Media_String]

    # --- Busca no UserList ---
    tempos_lista = []
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        # Busca linear nativa em listas
        encontrado = alvo in tabela_lista 
        fim = time.perf_counter()
        tempos_lista.append(fim - inicio)
        
    media_lista = sum(tempos_lista) / len(palavras_alvo)
    tempos_medios.append(media_lista)
    print(f"Tempo MÉDIO UserList:   {media_lista:.8f} segundos")

    # --- Busca no UserDict ---
    tempos_dict = []
    # Como armazenamos as palavras nos VALORES do dicionário (tabela_dict[i] = palavra)
    # precisamos extrair os valores para buscar.
    valores_dict = tabela_dict.values() 
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        encontrado = alvo in valores_dict
        fim = time.perf_counter()
        tempos_dict.append(fim - inicio)
        
    media_dict = sum(tempos_dict) / len(palavras_alvo)
    tempos_medios.append(media_dict)
    print(f"Tempo MÉDIO UserDict:   {media_dict:.8f} segundos")

    # --- Busca no UserString ---
    tempos_string = []
    for alvo in palavras_alvo:
        inicio = time.perf_counter()
        # Busca de substring. Adicionamos espaços para buscar a palavra exata
        # e não pedaços de outras palavras (ex: evitar que ' NASA ' ache ' NASAL ')
        encontrado = f" {alvo} " in tabela_string 
        fim = time.perf_counter()
        tempos_string.append(fim - inicio)
        
    media_string = sum(tempos_string) / len(palavras_alvo)
    tempos_medios.append(media_string)
    print(f"Tempo MÉDIO UserString: {media_string:.8f} segundos")

    return tempos_medios

# ---------------------------------------------------------
# 3. Geração do Gráfico
# ---------------------------------------------------------
def plotar_grafico(tempos_medios):
    classes = ['UserList', 'UserDict', 'UserString']
    
    plt.figure(figsize=(8, 5))
    barras = plt.bar(classes, tempos_medios, color=['#4C72B0', '#DD8452', '#55A868'])
    
    plt.title('Tempo Médio de Busca de Palavras por Classe', fontsize=14)
    plt.ylabel('Tempo Médio (Segundos)', fontsize=12)
    plt.xlabel('Estrutura de Dados', fontsize=12)
    
    # Adicionando os valores exatos em cima das barras
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.6f} s',
                 ha='center', va='bottom', fontsize=10)
                 
    # Escala logarítmica pode ser útil se um for MUITO mais lento que os outros
    # plt.yscale('log') 

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
        tempos = realizar_buscas(t_lista, t_dict, t_string, alvos)
        plotar_grafico(tempos)
