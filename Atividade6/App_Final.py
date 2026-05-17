import os
import time
from typing import Callable


from src.tratamento import tratamento
from src.algoritimos import bubble_sort, insertion_sort, selection_sort, shell_sort, true_merge_sort, heap_sort, true_quick_sort

def limpar_tela():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def abrir_arquivo(file: str):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError as e:
        return {"erro": e}

def ordenar(lista: list[str], sort: Callable):
    tratamento(lista)
    start = time.time()
    sort(lista)
    end = time.time()
    return {"sucesso": {sort.__name__: f"{(end - start):.4f} segundos"}}

# Dicionário de funções
dicio = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Shell Sort": shell_sort,
    "Heap Sort": heap_sort,
    "Merge Sort": true_merge_sort,
    "Quick Sort": true_quick_sort
}

def menu():
    print("MENU DE TESTES DE ORDENAÇÃO:")
    print("1 - Carregar arquivo de dados")
    print("2 - Comparar dois métodos específicos")
    print("3 - Comparar métodos por grupo")
    print("4 - Sair")
    print()

def main():
    lista_dados = []
    chaves_dicio = list(dicio.keys())

    while True:
        limpar_tela()
        menu()
        
        try:
            escolha = int(input("Escolha alguma dessas opções: "))
            if escolha < 1 or escolha > 4:
                print("Serão aceitas apenas as opções entre 1 e 4.")
                input("\nPressione Enter para tentar novamente...")
                continue
        except Exception:
            print("Entrada inválida. Será aceito apenas as opções entre 1 e 4.")
            input("\nPressione Enter para tentar novamente...")
            continue

        match escolha:
            case 1:
                limpar_tela()
                print("--- 1. CARREGAR ARQUIVO ---")
                nome_arquivo = input("Digite o nome do arquivo (ex: nomes100k.txt): ")
                resultado = abrir_arquivo(nome_arquivo)
                
                
                if isinstance(resultado, dict) and "erro" in resultado:
                    print(f"\nErro ao carregar: {resultado['erro']}")
                else:
                    lista_dados = resultado
                    print(f"\nSucesso! Foram carregadas {len(lista_dados)} linhas na memória.")
                input("\nPressione Enter para voltar ao menu...")

            case 2:
                limpar_tela()
                if not lista_dados:
                    print("ERRO: Você precisa carregar um arquivo primeiro (Opção 1).")
                    input("\nPressione Enter para voltar ao menu...")
                    continue

                print("--- 2. COMPARAR DOIS MÉTODOS ---")
                for i, nome in enumerate(chaves_dicio):
                    print(f"{i + 1} - {nome}")
                
                try:
                    op1 = int(input("\nEscolha o número do 1º método: ")) - 1
                    op2 = int(input("Escolha o número do 2º método: ")) - 1
                    
                    if op1 not in range(len(chaves_dicio)) or op2 not in range(len(chaves_dicio)):
                        print("\nOpções de métodos inválidas!")
                    else:
                        nome_algo1, nome_algo2 = chaves_dicio[op1], chaves_dicio[op2]
                        
                        print(f"\nExecutando {nome_algo1}... (Aguarde)")
                        # Como a função "ordenar" muda a lista que está sendo passada, eu mando
                        #uma cópia que esta que vai ser alterada
                        resultado1 = ordenar(lista_dados.copy(), dicio[nome_algo1])
                        print(f"Resultado: {resultado1['sucesso']}")
                        
                        print(f"\nExecutando {nome_algo2}... (Aguarde)")
                        resultado2 = ordenar(lista_dados.copy(), dicio[nome_algo2])
                        print(f"Resultado: {resultado2['sucesso']}")
                        
                except Exception:
                    print("\nEntrada inválida para a escolha dos métodos.")
                input("\nPressione Enter para voltar ao menu...")

            case 3:
                limpar_tela()
                if not lista_dados:
                    print("ERRO: Você precisa carregar um arquivo primeiro (Opção 1).")
                    input("\nPressione Enter para voltar ao menu...")
                    continue

                print("--- 3. COMPARAR MÉTODOS POR GRUPO ---")
                print("1 - Grupo Quadrático O(n²) (Bubble, Insertion, Selection)")
                print("2 - Grupo Logarítmico O(n log n) (Shell, Heap, Merge, Quick)")
                
                try:
                    grupo = int(input("\nEscolha o grupo que deseja testar (1 ou 2): "))
                    algoritmos_teste = []
                    
                    if grupo == 1:
                        algoritmos_teste = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
                        print("\nATENÇÃO: Este grupo é O(n²). Para listas grandes (ex: 100k), isso pode demorar MUITO tempo.")
                    elif grupo == 2:
                        algoritmos_teste = ["Shell Sort", "Heap Sort", "Merge Sort", "Quick Sort"]
                    else:
                        print("\nOpção de grupo inválida.")
                        input("\nPressione Enter para voltar ao menu...")
                        continue

                    print("\nIniciando bateria de testes...")
                    for nome_algo in algoritmos_teste:
                        print(f" -> Executando {nome_algo}...")
                        resultado = ordenar(lista_dados.copy(), dicio[nome_algo])
                        print(f"    Tempo: {resultado['sucesso']}")

                except Exception:
                    print("\nEntrada inválida.")
                input("\nPressione Enter para voltar ao menu...")

            case 4:
                limpar_tela()
                print("Programa encerrado com sucesso ")
                break

if __name__ == "__main__":
    main()
