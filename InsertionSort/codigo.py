
import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaSimples: #lista encadeada padrão com um descritor

    def __init__(self):
        self.head = None
        self.tamanho = 0

    def isEmpty(self):
        return self.head == None

    def add(self, novo_valor):
        novo = No(novo_valor)
        novo.next = self.head
        self.head = novo
        self.tamanho += 1
    
    def toList(self): 
        '''Converte a lista encadeada para uma lista padrão do Python.
        Isso facilita a exibição de dados na Interface Gráfica (GUI).'''
        resultado = []
        aux = self.head
        while aux:
            resultado.append(aux.valor)
            aux = aux.next
        return resultado

def InsertionSort(lista_original):

    if lista_original.isEmpty(): 
        return{"erro": "Os dados ainda não foram carregados ou estão vazios."}

    inicio = time.time() # Início da medição para estatísticas

    lista_ordenada = ListaSimples()
    atual = lista_original.head

    while atual:

        novo_no = No(atual.valor)

        if lista_ordenada.head is None or novo_no.valor < lista_ordenada.head.valor: #caso especial: inserir no começo ou lista vazia
            novo_no.next = lista_ordenada.head
            lista_ordenada.head = novo_no
        else: #Busca da posição correta no meio ou fim da lista
            aux = lista_ordenada.head
            while aux.next and aux.next.valor < novo_no.valor: # Percorre enquanto o próximo valor for menor que o valor atual
                aux = aux.next
            #atualiza os ponteiros do elemento anterior e do que estamos inserindo
            novo_no.next = aux.next 
            aux.next = novo_no
        
        #avança para o próximo e atualiza o tamanho
        atual = atual.next
        lista_ordenada.tamanho += 1
    
    fim = time.time()
    tempo = fim - inicio # tempo da ordenação

    return {
        "sucesso": {
            "lista_nomes": lista_ordenada.toList(),
            "estatisticas": {
                "tamanho": lista_ordenada.tamanho,
                "tempo": tempo
            }
        }
    }
        
def CarregarArquivos(lista):
    '''Carrega a lista de nomes e retorna erro caso o arquivo não seja encontrado ou algum outro erro inesperado aconteça.'''
    try: 
        with open("nomes.txt", "r", encoding= "utf-8")as arquivo:
            for linha in arquivo:
                lista.add(linha.strip())
        return {"sucesso": "Arquivo carregado com sucesso!"}

    except FileNotFoundError:
        return {"erro": "Arquivo não encontrado!"}

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}

def obterListaOriginal(lista_original):
    '''Retorna uma lista das palavras sem ordenação conforme foi carregada.'''
    if lista_original.isEmpty():
        return {"erro": "Os dados ainda não foram carregados ou estão vazios."}
    return {"sucesso": lista_original.toList()}
