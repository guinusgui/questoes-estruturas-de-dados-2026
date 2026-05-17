from src.tratamento import tratamento
from src.algoritimos import bubble_sort, insertion_sort, selection_sort, shell_sort, true_merge_sort, heap_sort, true_quick_sort
import time
from typing import Callable

def abrir_arquivo(file:str):
    try:
        with open(file, "r") as f:
            return f.readlines()
    except FileNotFoundError as e:
            return {"erro":e}

#Não sei por que tu precisa de "sucesso" no dicionário, mas o retorno é
#Um dicionário com o nome da função de um lado e o tempo formatado do outro
def ordenar(lista:list[str], sort:Callable):
    tratamento(lista)
    start = time.time()
    sort(lista)
    end = time.time()
    return {"sucesso":{sort.__name__ : f"{(end - start):.4f}"}}


#Talvez ajude na interface
dicio = {
     "Bubble Sort":bubble_sort,
     "Insertion Sort":insertion_sort,
     "Selection Sort":selection_sort,
     "Shell Sort":shell_sort,
     "Heap Sort": heap_sort,
     "Merge Sort":true_merge_sort,
     "Quick Sort":true_quick_sort
}

if __name__ == "__main__":
    
    lista = abrir_arquivo("nomes100k.txt")
    for i in range(10):
         print(lista[i])

    print(ordenar(lista, bubble_sort))
    for i in range(10):
         print(lista[i])

    """
            INTERFACE
        1. Carregar arquivo -> solicite o nome ao usuário, chame abrir_arquivo
        2. Comparar metodos -> solicite dois métodos, chame sortear
            ou
        2. Comparar metodos -> solicite o grupo (O(n^2) ou O(n)) e compare com sort
        conforme o arquivo do profrssor

        ps: o bublle, o insert e o selection tão demorando bastante, se achar que sabe otimizar,
        por favor faça 
    """
    

    



    