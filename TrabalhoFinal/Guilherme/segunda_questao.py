import re
import time
from collections import UserList, UserDict, UserString

def carregar_e_limpar_arquivo(nome_arquivo):
    """Lê o arquivo e extrai as palavras, ignorando pontuação e dígitos."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
            
        # O regex r'[^\W\d_]+' extrai apenas sequências de letras (incluindo acentos),
        # ignorando espaços, quebras de linha, números e pontuações.
        palavras = re.findall(r'[^\W\d_]+', texto)
        return palavras
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []

def realizar_benchmark(palavras):
    # Lista onde guardaremos os tempos: [Tempo_List, Tempo_Dict, Tempo_String]
    tempos_de_execucao = []
    
    print(f"Iniciando inserção de {len(palavras)} palavras...\n")

    # ==========================================
    # 1. Teste com UserList
    # ==========================================
    tabela_lista = UserList()
    
    inicio = time.perf_counter()
    for palavra in palavras:
        tabela_lista.append(palavra)
    fim = time.perf_counter()
    
    tempo_lista = fim - inicio
    tempos_de_execucao.append(tempo_lista)
    print(f"Tempo UserList:   {tempo_lista:.5f} segundos")

    # ==========================================
    # 2. Teste com UserDict
    # ==========================================
    tabela_dict = UserDict()
    
    inicio = time.perf_counter()
    for i, palavra in enumerate(palavras):
        # Usamos o índice (i) como chave para garantir que NENHUMA 
        # palavra repetida seja sobreposta ou ignorada (regra da questão).
        tabela_dict[i] = palavra
    fim = time.perf_counter()
    
    tempo_dict = fim - inicio
    tempos_de_execucao.append(tempo_dict)
    print(f"Tempo UserDict:   {tempo_dict:.5f} segundos")

    # ==========================================
    # 3. Teste com UserString
    # ==========================================
    tabela_string = UserString("")
    
    inicio = time.perf_counter()
    # Aviso: A concatenação de strings em um loop é propositalmente 
    # ineficiente no Python. Isso demorará consideravelmente mais!
    for palavra in palavras:
        tabela_string += palavra + " "
    fim = time.perf_counter()
    
    tempo_string = fim - inicio
    tempos_de_execucao.append(tempo_string)
    print(f"Tempo UserString: {tempo_string:.5f} segundos")

    # ==========================================
    # Retorno dos dados para o gráfico
    # ==========================================
    print("\nLista final com os tempos [List, Dict, String]:")
    print(tempos_de_execucao)
    
    return tempos_de_execucao

# --- Execução Principal ---
if __name__ == "__main__":
    arquivo = "nomes100k.txt"
    
    # Passo 1: Isolar a leitura de disco do teste de tempo
    lista_de_palavras = carregar_e_limpar_arquivo(arquivo)
    
    if lista_de_palavras:
        # Passo 2: Rodar o teste e salvar os tempos
        tempos_para_grafico = realizar_benchmark(lista_de_palavras)
