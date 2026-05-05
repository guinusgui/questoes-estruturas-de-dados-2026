import customtkinter as ctk
from codigo import ListaSimples,CarregarArquivos,InsertionSort
import threading
class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações do Sistema
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.geometry("400x400")
        self.title("Sistema de Gerenciamento de Nomes")
        
        # Estado do Aplicativo
        self.minha_lista = ListaSimples()
        self.resultado_ordenacao = None 
        self.foi_carregado = False
        self.foi_ordenado = False
        self.processando = False

        
        
        self.criar_menu()

    def criar_menu(self):
        self.botoes = []
        self.frame_menu = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_menu.pack(expand=True, fill="both")
        
        # Botão 1: Carregar os Dados
        frame_1 = self.criar_frame_no_menu()
        bnt_1 = ctk.CTkButton(frame_1, text="1. Carregar Dados do Arquivo", 
                      command=lambda: self.carregar_os_dados(self.statos_1))
        bnt_1.pack(pady=(5,0))
        self.statos_1 = ctk.CTkLabel(frame_1, text="", text_color="gray") #Como esse label vai
        #ser usado para aviso, começa com "text=''" 
        self.statos_1.pack()
        self.botoes.append(bnt_1)
            
        # Botão 2: Ordenar os Dados 
        frame_2 = self.criar_frame_no_menu()
        bnt_2 = ctk.CTkButton(frame_2, text="2. Ordenar Dados", 
                      command=lambda: self.ordenar_os_dados(self.statos_2))
        bnt_2.pack(pady=(5,0))
        self.statos_2 = ctk.CTkLabel(frame_2, text="", text_color="gray")
        self.statos_2.pack()
        self.botoes.append(bnt_2)

        # Botão 3: Listar Original 
        
        self.bnt_listar_sem_odernacao =  ctk.CTkButton(self.frame_menu, text="3. Listar sem Ordenação", 
                      command=self.listar_sem_ordenacao)
        self.bnt_listar_sem_odernacao.pack(pady=(10,20))
        self.botoes.append(self.bnt_listar_sem_odernacao)
    
        # Botão 4: Listar Ordenado
        
        self.bnt_listar_com_odernacao = ctk.CTkButton(self.frame_menu, text="4. Listar Ordenados", 
                      command=self.listar_com_ordenacao)
        self.bnt_listar_com_odernacao.pack(pady=20)
        self.botoes.append(self.bnt_listar_com_odernacao)

        # Botão 5: Estatísticas
        
        self.bnt_estatistica = ctk.CTkButton(self.frame_menu, text="5. Imprimir Estatísticas", 
                      command=self.imprimir_estatistica)
        self.bnt_estatistica.pack(pady=20)
        self.botoes.append(self.bnt_estatistica)


    def criar_frame_no_menu(self):
        frame = ctk.CTkFrame(self.frame_menu, fg_color="transparent")
        frame.pack(pady=2, fill='x')
        return frame

    def voltar_para_menu(self, frame_atual: ctk.CTkFrame):
        frame_atual.pack_forget() #Escondo o Frame
        frame_atual.destroy() # Limpo o frame da memória
        self.frame_menu.pack(expand=True, fill="both")

    def sair_do_menu(self, novo_frame: ctk.CTkFrame):
        self.frame_menu.pack_forget()
        novo_frame.pack(expand=True, fill="both")

    def travar_botoes(self):
            for botao in self.botoes:
                botao.configure(state="disabled")

    def destravar_botoes(self):
            for botao in self.botoes:
                botao.configure(state="normal")

    def carregar_os_dados(self, label: ctk.CTkLabel):
        if self.processando:
            return

        self.minha_lista = ListaSimples()#Reseto a lista, para que não seja acumulado os dados        
        #já anteriomento colocados

        self.processando = True
        resposta = CarregarArquivos(self.minha_lista)
        self.processando = False

        if "sucesso" in resposta:
            self.foi_carregado = True
            label.configure(text=resposta["sucesso"], text_color="#2ecc71")
            
        else:
            label.configure(text=resposta["erro"], text_color="#ea3013")



        self.after(3000, lambda: label.configure(text=""))#Basicamente vai esperar 3000ms(3segundos) para fazer com que 
        #o "label" volte a ter nada escrito nele


def ordenar_os_dados(self, label: ctk.CTkLabel):
    # 1. Bloqueio de entrada
    if self.processando:
        return

    # 2. Configuração inicial
    self.processando = True
    self.travar_botoes()

    # 3. Função única que encapsula o trabalho e a atualização da GUI
    def fluxo_de_trabalho():
        # Executa o cálculo (pesado)
        resultado = InsertionSort(self.minha_lista)
        
        # Volta para a Thread Principal para atualizar a interface (obrigatório)
        self.after(0, lambda: [
            self.destravar_botoes(),
            setattr(self, 'processando', False),
            label.configure(
                text="Ordenação concluída!" if "sucesso" in resultado else resultado["erro"],
                text_color="#2ecc71" if "sucesso" in resultado else "#ea3013"
            ),
            self.after(3000, lambda: label.configure(text=""))
        ])

    # 4. Inicia a thread disparando a função interna
    threading.Thread(target=fluxo_de_trabalho, daemon=True).start()

    def listar_sem_ordenacao(self):
        if self.processando:
            return

        if not self.foi_carregado:
            self.statos_1.configure(text="⚠️ Carregue os dados primeiro!", text_color="#e67e22")
            self.after(3000, lambda: self.statos_1.configure(text=""))
            return

        

        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="DADOS ORIGINAIS(20 PRIMEIROS)", font=("Arial", 18, "bold")).pack(pady=10)
        
        txt_box = ctk.CTkTextbox(novo_frame, width=300, height=250)
        txt_box.pack(pady=10)
        
        nomes = self.minha_lista.toList() #Método que transfarma em uma lista sem ser
        #encadeada, senvindo apenas para facilitar na hora de exibir os nomes
        count = 1
        
        for nome in reversed(nomes): #Inverte a lista, pois quando ela é inserida acaba
        #invertendo a ordem que está no arquivo 
            if count> 20:
                break
            txt_box.insert("end", f"{count}- {nome}\n")
            count +=1
        txt_box.configure(state="disabled")#Basicamente é para impossibilitar que o que foi escrito no "txt_box"
        #seja alterado

        ctk.CTkButton(novo_frame, text="Voltar ao menu", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=10)
        self.sair_do_menu(novo_frame) # Troca a tela para voltar ao menu

    def listar_com_ordenacao(self):
        if self.processando:
            return
        
        if not self.foi_ordenado:
            self.statos_2.configure(text="⚠️ Ordene os dados primeiro!", text_color="#e67e22")
            self.after(3000, lambda: self.statos_2.configure(text=""))
            return

        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="DADOS ORDENADOS(20 PRIMEIROS)", font=("Arial", 18, "bold")).pack(pady=10)
        
        txt_box = ctk.CTkTextbox(novo_frame, width=300, height=250)
        txt_box.pack(pady=10)
        
        nomes_ordenados = self.resultado_ordenacao["sucesso"]["lista_nomes"]
        count = 1
        
        for nome in nomes_ordenados:
            if count> 20:
                break
            txt_box.insert("end", f"{count}- {nome}\n")
            count +=1
        txt_box.configure(state="disabled")

        ctk.CTkButton(novo_frame, text="Voltar ao menu", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=10)
        self.sair_do_menu(novo_frame)

    def imprimir_estatistica(self):
        if self.processando:
            return
        
        if not self.foi_ordenado:
            self.statos_2.configure(text="⚠️ Ordene os dados primeiro!", text_color="#e67e22")
            return

        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="ESTATÍSTICAS DA ORDENAÇÃO", font=("Arial", 18, "bold")).pack(pady=20)
        
        status = self.resultado_ordenacao["sucesso"]["estatisticas"]
        info = f"Quantidade de nomes: {status['tamanho']}\n\nTempo de execução:\n{status['tempo']:.6f} segundos"
        
        ctk.CTkLabel(novo_frame, text=info, font=("Arial", 14), justify="center").pack(pady=10)
        ctk.CTkButton(novo_frame, text="Voltar ao menu", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=20)

        self.sair_do_menu(novo_frame)



if __name__ == "__main__":
    app = Interface()
    app.mainloop()
    
