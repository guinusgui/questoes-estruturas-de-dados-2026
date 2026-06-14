import customtkinter as ctk
from tkinter import filedialog
import threading


from tree_plotter import gui_plot

from bst import BST 
class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações do Sistema
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.geometry("450x600")
        self.title("Gerenciador de Árvore Binária de Busca (BST)")
        
        # Estado do Aplicativo
        self.bst = BST()
        self.processando = False

        self.criar_menu()

    def criar_menu(self):
        self.botoes = []
        self.frame_menu = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_menu.pack(expand=True, fill="both", padx=20, pady=20)
        
        ctk.CTkLabel(self.frame_menu, text="Árvore Binária de Busca", font=("Arial", 22, "bold")).pack(pady=(0, 30))

        # 1. Inserção Individual
        btn_insert = ctk.CTkButton(self.frame_menu, text="1. Inserir Elemento", command=self.inserir_individual)
        btn_insert.pack(pady=10, fill='x')
        self.botoes.append(btn_insert)

        # 2. Inserção em Lote 
        btn_lote = ctk.CTkButton(self.frame_menu, text="2. Inserir em Lote", command=self.inserir_lote_menu)
        btn_lote.pack(pady=10, fill='x')
        self.botoes.append(btn_lote)

        # 3. Busca de Elemento 
        btn_search = ctk.CTkButton(self.frame_menu, text="3. Buscar Elemento", command=self.buscar_chave)
        btn_search.pack(pady=10, fill='x')
        self.botoes.append(btn_search)

        # 4. Limpar Árvore
        btn_limpar = ctk.CTkButton(self.frame_menu, text="4. Limpar Árvore (Esvaziar)", fg_color="#c0392b", hover_color="#e74c3c", command=self.limpar_arvore)
        btn_limpar.pack(pady=10, fill='x')
        self.botoes.append(btn_limpar)

        # 5. Informações da Árvore
        btn_info = ctk.CTkButton(self.frame_menu, text="5. Mostrar Informações", command=self.mostrar_info)
        btn_info.pack(pady=10, fill='x')
        self.botoes.append(btn_info)

        # 6. Travessias (Percursos)
        btn_travessias = ctk.CTkButton(self.frame_menu, text="6. Mostrar Percursos (Travessias)", command=self.mostrar_travessias)
        btn_travessias.pack(pady=10, fill='x')
        self.botoes.append(btn_travessias)

        # 7. Plotar Árvore
        btn_plot = ctk.CTkButton(self.frame_menu, text="7. Plotar Desenho da Árvore", command=self.plotar_arvore)
        btn_plot.pack(pady=10, fill='x')
        self.botoes.append(btn_plot)

        # Label de Status (para feedback rápido)
        self.lbl_status = ctk.CTkLabel(self.frame_menu, text="", text_color="gray")
        self.lbl_status.pack(pady=(20, 0))

    # ==================NAVEGAÇÃO ==================

    def voltar_para_menu(self, frame_atual: ctk.CTkFrame):
        frame_atual.pack_forget()
        frame_atual.destroy()
        self.frame_menu.pack(expand=True, fill="both", padx=20, pady=20)

    def sair_do_menu(self, novo_frame: ctk.CTkFrame):
        self.frame_menu.pack_forget()
        novo_frame.pack(expand=True, fill="both", padx=20, pady=20)

    def travar_botoes(self):
        for botao in self.botoes:
            botao.configure(state="disabled")

    def destravar_botoes(self):
        for botao in self.botoes:
            botao.configure(state="normal")

    def mostrar_status(self, mensagem, cor="#2ecc71"):
        self.lbl_status.configure(text=mensagem, text_color=cor)
        self.after(3000, lambda: self.lbl_status.configure(text=""))

    # ================== AÇÃO ==================

    def inserir_individual(self):
        if self.processando: return
        
        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="INSERIR ELEMENTO", font=("Arial", 22, "bold")).pack(pady=40)
        
        input_field = ctk.CTkEntry(novo_frame, placeholder_text="Digite um número natural...", width=300, height=45)
        input_field.pack(pady=20)
        
        def confirmar():
            try:
                chave = int(input_field.get())
                self.bst.put(chave)
                self.mostrar_status(f"Chave {chave} inserida!", "#2ecc71")
                self.voltar_para_menu(novo_frame)
            except ValueError:
                ctk.CTkLabel(novo_frame, text="Erro: Digite um número inteiro válido.", text_color="#ea3013").pack(pady=5)

        ctk.CTkButton(novo_frame, text="Confirmar Inserção", command=confirmar, height=40).pack(pady=10)
        ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", hover_color="#555555", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=10)
        
        self.sair_do_menu(novo_frame)

    def buscar_chave(self):
        if self.processando: return
        
        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="BUSCAR CHAVE", font=("Arial", 22, "bold")).pack(pady=40)
        
        input_field = ctk.CTkEntry(novo_frame, placeholder_text="Digite a chave para busca...", width=300, height=45)
        input_field.pack(pady=20)
        
        lbl_resultado = ctk.CTkLabel(novo_frame, text="", font=("Arial", 14))
        lbl_resultado.pack(pady=5)

        def confirmar():
            try:
                chave = int(input_field.get())
                try:
                    self.bst.search_by_key(chave)
                    lbl_resultado.configure(text=f"✓ Chave {chave} encontrada na árvore!", text_color="#2ecc71")
                except KeyError:
                    lbl_resultado.configure(text=f"✗ Chave {chave} não existe na árvore.", text_color="#ea3013")
            except ValueError:
                lbl_resultado.configure(text="Erro: Digite um número inteiro válido.", text_color="#ea3013")

        ctk.CTkButton(novo_frame, text="Realizar Busca", command=confirmar, height=40).pack(pady=10)
        ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", hover_color="#555555", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=10)
        
        self.sair_do_menu(novo_frame)

    def inserir_lote_menu(self):
        if self.processando: return
        
        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="INSERIR EM LOTE", font=("Arial", 22, "bold")).pack(pady=(20, 10))

        # OPÇÃO 1: Digitar na interface
        ctk.CTkLabel(novo_frame, text="Opção 1: Digite os números (separados por vírgula ou espaço)", font=("Arial", 12)).pack(pady=(10, 0))
        txt_box = ctk.CTkTextbox(novo_frame, width=350, height=80)
        txt_box.pack(pady=5)

        lbl_feedback = ctk.CTkLabel(novo_frame, text="", font=("Arial", 12))
        lbl_feedback.pack(pady=0)

        def inserir_digitados():
            raw_text = txt_box.get("1.0", "end-1c")
            if not raw_text.strip(): return

            try:
                # Substitui vírgulas por espaços e converte tudo para inteiros
                texto_limpo = raw_text.replace(',', ' ')
                numeros = [int(x) for x in texto_limpo.split()]
                
                self.bst.batch_put(*numeros)
                self.mostrar_status(f"{len(numeros)} valores inseridos com sucesso!", "#2ecc71")
                self.voltar_para_menu(novo_frame)
            except ValueError:
                lbl_feedback.configure(text="Erro: Certifique-se de digitar apenas números inteiros.", text_color="#ea3013")

        ctk.CTkButton(novo_frame, text="Inserir Valores Digitados", command=inserir_digitados).pack(pady=5)

        ctk.CTkLabel(novo_frame, text="— OU —", font=("Arial", 14, "bold"), text_color="gray").pack(pady=15)

        # OPÇÃO 2: Carregar de um arquivo .txt
        ctk.CTkLabel(novo_frame, text="Opção 2: Carregar de um arquivo .txt", font=("Arial", 12)).pack(pady=(0, 5))

        def carregar_arquivo():
            filepath = filedialog.askopenfilename(title="Selecione o arquivo txt", filetypes=[("Text Files", "*.txt")])
            if not filepath: return

            self.processando = True
            
            def fluxo_trabalho():
                try:
                    with open(filepath, 'r') as f:
                        conteudo = f.read()
                        texto_limpo = conteudo.replace(',', ' ')
                        numeros = [int(x) for x in texto_limpo.split()]
                        self.bst.batch_put(*numeros)
                        
                        self.after(0, lambda: [
                            self.mostrar_status(f"{len(numeros)} elementos do arquivo inseridos!", "#2ecc71"),
                            self.voltar_para_menu(novo_frame)
                        ])
                except Exception as e:
                    self.after(0, lambda: lbl_feedback.configure(text="Erro ao ler o arquivo. Arquivo inválido.", text_color="#ea3013"))
                finally:
                    self.after(0, lambda: setattr(self, 'processando', False))

            threading.Thread(target=fluxo_trabalho, daemon=True).start()

        ctk.CTkButton(novo_frame, text="Selecionar Arquivo .txt", fg_color="#2980b9", hover_color="#3498db", command=carregar_arquivo).pack(pady=5)

        ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", hover_color="#555555", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=(25, 0))

        self.sair_do_menu(novo_frame)

    def limpar_arvore(self):
        self.bst.clear()
        self.mostrar_status("Árvore esvaziada com sucesso!", "#f1c40f")

    def mostrar_info(self):
        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="ESTATÍSTICAS DA ÁRVORE", font=("Arial", 22, "bold")).pack(pady=20)

        if self.bst.head is None:
            info_texto = "A árvore está vazia no momento."
        else:
            tamanho = self.bst.size
            altura = self.bst.get_height()
            
            menor_no = self.bst.get_min_node()
            maior_no = self.bst.get_max_node()
            menor_chave = menor_no.key if menor_no else "N/A"
            maior_chave = maior_no.key if maior_no else "N/A"
            
            c_interno = self.bst.get_internal_path_length()
            balanceada = "Sim (Regra AVL)" if self.bst.is_balanced() else "Não"

            info_texto = (
                f"Tamanho (Qtd Nós): {tamanho}\n\n"
                f"Altura: {altura}\n\n"
                f"Menor Elemento: {menor_chave}\n\n"
                f"Maior Elemento: {maior_chave}\n\n"
                f"Comprimento Interno: {c_interno}\n\n"
                f"Está Balanceada?: {balanceada}"
            )

        lbl_info = ctk.CTkLabel(novo_frame, text=info_texto, font=("Arial", 16), justify="left")
        lbl_info.pack(pady=20)

        ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", hover_color="#555555", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=20)
        self.sair_do_menu(novo_frame)

    def mostrar_travessias(self):
        if self.processando: return

        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="PERCURSOS (TRAVESSIAS)", font=("Arial", 22, "bold")).pack(pady=20)

        txt_box = ctk.CTkTextbox(novo_frame, width=400, height=350, font=("Arial", 14))
        txt_box.pack(pady=10)
        
        lbl_carregando = ctk.CTkLabel(novo_frame, text="Processando percursos... Por favor, aguarde.", text_color="#f1c40f")
        lbl_carregando.pack(pady=5)


        btn_voltar = ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", state="disabled", command=lambda: self.voltar_para_menu(novo_frame))
        btn_voltar.pack(pady=10)

        self.sair_do_menu(novo_frame)

        def fluxo_trabalho():
            if self.bst.head is None:
                self.after(0, lambda: [
                    txt_box.insert("end", "A árvore está vazia."),
                    lbl_carregando.pack_forget(),
                    btn_voltar.configure(state="normal")
                ])
                return

            # Executa os percursos em background
            pre = self.bst.pre_order()
            em = self.bst.in_order()
            pos = self.bst.post_order()
            larg = self.bst.level()

            # Se a árvore for muito grande, é limitado o texto para não travar a renderização da janela
            limite = 1000
            aviso = f"\n\n⚠️ Exibindo apenas os primeiros {limite} elementos para evitar travamento visual." if len(em) > limite else ""


            def atualizar_tela():
                txt_box.insert("end", "1. Pré-ordem (Raiz-Esq-Dir):\n")
                txt_box.insert("end", f"{str(pre[:limite])}{aviso}\n\n")

                txt_box.insert("end", "2. Em-ordem (Esq-Raiz-Dir):\n")
                txt_box.insert("end", f"{str(em[:limite])}{aviso}\n\n")

                txt_box.insert("end", "3. Pós-ordem (Esq-Dir-Raiz):\n")
                txt_box.insert("end", f"{str(pos[:limite])}{aviso}\n\n")

                txt_box.insert("end", "4. Largura (Level Order):\n")
                txt_box.insert("end", f"{str(larg[:limite])}{aviso}\n")

                txt_box.configure(state="disabled")
                lbl_carregando.pack_forget() # Remove o aviso de carregando
                btn_voltar.configure(state="normal", fg_color="gray", hover_color="#555555") # Ativa o botão de voltar

            self.after(0, atualizar_tela)

        # Dispara a thread de processamento em segundo plano

        threading.Thread(target=fluxo_trabalho, daemon=True).start()

    def plotar_arvore(self):
        novo_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(novo_frame, text="DESENHO DA ÁRVORE", font=("Arial", 22, "bold")).pack(pady=20)

        altura = self.bst.get_height()
        
        if self.bst.head is None:
            ctk.CTkLabel(novo_frame, text="Árvore está vazia. Não há o que desenhar.", font=("Arial", 14)).pack(pady=40)
        elif altura > 3:
            ctk.CTkLabel(novo_frame, text=f"Árvore muito grande (Altura {altura} > 3).\nNão será plotada graficamente.", text_color="#ea3013", font=("Arial", 14)).pack(pady=40)
        else:
            resultado = gui_plot(self.bst)
            if "imagem" in resultado:
                img = resultado["imagem"]
                lbl_img = ctk.CTkLabel(novo_frame, image=img, text="")
                lbl_img.image = img 
                lbl_img.pack(pady=10)
            else:
                msg_erro = resultado.get("erro", "Erro desconhecido ao renderizar.")
                ctk.CTkLabel(novo_frame, text=msg_erro, text_color="#ea3013").pack(pady=40)

        ctk.CTkButton(novo_frame, text="Voltar", fg_color="gray", hover_color="#555555", command=lambda: self.voltar_para_menu(novo_frame)).pack(pady=20)
        self.sair_do_menu(novo_frame)

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
