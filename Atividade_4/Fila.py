import os

class Fila:
    def __init__(self):
        # Definindo os valores inciais da fila:
        self.capacidade_com_prioridade = 100
        self.capacidade_sem_prioridade = 100
        
        self.com_prioridade = [None] * self.capacidade_com_prioridade
        self.sem_prioridade = [None] * self.capacidade_sem_prioridade
        
        self.flag = 0
        
        # Final da fila
        self.fim_com = 0
        self.fim_sem = 0
        
        # Inicio da fila
        self.inicio_com = 0
        self.inicio_sem = 0

    def redimensionar_array(self, fila, capacidade_antiga,fim_da_fila):
        nova_capacidade = capacidade_antiga * 2
        novo_array = [None] * nova_capacidade
       
        novo_array[:fim_da_fila] = fila[:fim_da_fila]
        
        return novo_array, nova_capacidade
    


    def criando_a_fila(self, entrada):
        conteudo = entrada
        if entrada.endswith(".txt"): #Verificar se é possívelmente um arquivo
            if os.path.exists(entrada):
                with open(entrada, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
            else:
                print("Arquivo não encontrado.")
                return

        pessoas = conteudo.split(",")
        for pessoa in pessoas:
            nome = pessoa.strip()
            if nome:
                self.categorizar_as_pessoas(nome)

    def categorizar_as_pessoas(self, nome):
        if "*" in nome:
            # Verifica se o array tá cheio:
            if self.fim_com >= self.capacidade_com_prioridade:
                capacidade_atual = self.capacidade_com_prioridade
                fim_da_fila = self.fim_com

                self.com_prioridade, self.capacidade_com_prioridade=self.redimensionar_array(self.com_prioridade, 
                                              capacidade_atual,fim_da_fila)

            self.com_prioridade[self.fim_com] = nome
            self.fim_com += 1
        else:
            # Verifica se o array tá cheio:
            if self.fim_sem >= self.capacidade_sem_prioridade:
                capacidade_atual = self.capacidade_sem_prioridade
                fim_da_fila = self.fim_sem

                self.sem_prioridade, self.capacidade_sem_prioridade=self.redimensionar_array(self.sem_prioridade, 
                                              capacidade_atual,fim_da_fila)

            self.sem_prioridade[self.fim_sem] = nome
            self.fim_sem += 1

    def mostrar_a_fila(self):

        print("\n--- SITUAÇÃO ATUAL DA FILA ---")
        
        if self.inicio_com < self.fim_com:
            print("FILA COM PRIORIDADE:")

            posicao_na_fila = 1
            inicio_da_fila = self.inicio_com
            fim_da_fila = self.fim_com

            for i in range(inicio_da_fila, fim_da_fila):
                print(f"{posicao_na_fila}°- {self.com_prioridade[i]}")
                posicao_na_fila+=1
                
        else:
            print("Fila de Prioridade vazia.")

        if self.inicio_sem < self.fim_sem:
            print("FILA SEM PRIORIDADE:")

            posicao_na_fila = 1
            inicio_da_fila = self.inicio_sem
            fim_da_fila = self.fim_sem
            
            for i in range(inicio_da_fila, fim_da_fila):
                print(f"{posicao_na_fila}°- {self.sem_prioridade[i]}")
                posicao_na_fila+=1

        else:
            print("Fila Sem Prioridade vazia.")

    def tamanho_atual_da_fila(self):
        tamanho_da_fila_com_prioridade = self.fim_com - self.inicio_com
        tamanho_da_fila_sem_prioridade =self.fim_sem - self.inicio_sem

        return  tamanho_da_fila_com_prioridade+ tamanho_da_fila_sem_prioridade 

    def informacoes_sobre_a_fila(self):
        
        atendidos_com = self.inicio_com
        atendidos_sem = self.inicio_sem
        total = atendidos_com + atendidos_sem
        return total,atendidos_com,atendidos_sem


    def _1com_3sem(self):

        if self.tamanho_atual_da_fila() == 0:
            print("Não há ninguém para ser atendido.")
            return


        tem_prioridade = self.inicio_com < self.fim_com
        tem_sem_prioridade = self.inicio_sem < self.fim_sem

        if (self.flag == 0 and tem_prioridade) or not tem_sem_prioridade:
            pessoa = self.com_prioridade[self.inicio_com]
            self.inicio_com += 1 # "Remove" movendo o ponteiro de início
            print(f"ATENDENDO [PRIORIDADE]: {pessoa}")
            
        else:

            pessoa = self.sem_prioridade[self.inicio_sem]
            self.inicio_sem += 1
            print(f"ATENDENDO [COMUM]: {pessoa}")
        
        self.flag = (self.flag + 1) % 4 #Pirmite a lógica de atende um com prioridade e 3 sem prioridade
