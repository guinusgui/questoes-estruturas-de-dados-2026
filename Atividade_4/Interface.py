import os
from Fila import Fila

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu(tamanho_fila):
    print("\n" + "="*40)
    print(f"{'SISTEMA DE ATENDIMENTO 1:3':^40}")
    print("="*40)
    print(f" Pessoas aguardando: {tamanho_fila}")
    print("-"*40)
    print(" 1. Chegada de Pessoa (Nome ou arquivo.txt)")
    print(" 2. Listar pessoas na fila")
    print(" 3. Atender próxima pessoa")
    print(" 4. Finalizar programa")
    print("-"*40)

def main():
    fila = Fila()
    
    while True:
        tamanho_atual_da_fila = fila.tamanho_atual_da_fila()
        limpar_tela()
        exibir_menu(tamanho_atual_da_fila)
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[ERRO] Digite apenas números entre 1 e 4.")
            input("Pressione Enter para tentar novamente...")
            limpar_tela()
            continue

        if opcao == 1:
            entrada = input("\nDigite um nome, uma lista de nomes ou o caminho do arquivo(.txt): ")
            if not entrada=="":
                fila.criando_a_fila(entrada)
                print("\nPessoa(s) adicionada(s) com sucesso")
            else:
                print("\nNenhuma pessoa foi adicionada")
            input("Pressione Enter para voltar ao menu...")
            tamanho_atual_da_fila = fila.tamanho_atual_da_fila() # Atualiza o tamanho da fila
            limpar_tela()

        elif opcao == 2:
            limpar_tela()
            fila.mostrar_a_fila()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()

        elif opcao == 3:
            # O método atender_proximo já imprime quem foi chamado
            fila._1com_3sem()     
            input("\nPressione Enter para continuar...")
            limpar_tela()

        elif opcao == 4:
            if fila.tamanho_atual_da_fila() > 0:
                print(f"\n[NEGADO] Ainda restam {fila.tamanho_atual_da_fila()} pessoas na fila.")
                print("Atenda todos antes de sair.")
                input("Pressione Enter para continuar...")
                limpar_tela()
            else:
                break
        else:
            print("\nOpção inválida!")
            print("Será aceito apenas as opções listadas no menu")
            input("Pressione Enter para continuar...")
            limpar_tela()

    #Mostrar as estastísticas:
    limpar_tela()
    total,atendidos_com, atendidos_sem = fila.informacoes_sobre_a_fila()
    
    print("\n" + "-"*40)
    print(f"{'ESTATÍSTICAS DOS ATENDIMENTOS':^40}")
    print("-"*40)
    print(f" Total de atendimentos: {total}")
    
    if total > 0:
        perc_prio = (atendidos_com / total) * 100
        perc_sem = (atendidos_sem / total) * 100
        print(f" Atendimentos COM prioridade: {atendidos_com} ({perc_prio:.1f}%)")
        print(f" Atendimentos SEM prioridade: {atendidos_sem} ({perc_sem:.1f}%)")
    else:
        print(" Nenhum atendimento foi realizado nesta sessão.")
        
    print("-"*40)
    print("Programa encerrado. Até logo!\n")

if __name__ == "__main__":
    main()
