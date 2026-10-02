# Define a interface gráfica utilizada para comunicação com o usuário


import tkinter as tk
from tkinter import ttk
import main


# Função que faz com que o botão inicie o programa
def iniciar(periodo):

    chave = periodo.get()
    
    main.main(chave)


# Função que insere o título na janela
def criar_titulo(janela):
        # Insere o título na janela
        titulo = tk.Label(
            janela,
            text="Automação de relatórios",
            font=("Calibri", 25, "bold"),
            fg="#111827",
            bg="#F3F4F6"
        )

        titulo.pack(pady=20)


# Função que cria um botão na janela
def criar_botão(periodo, janela):
    # Cria um botão 
    botao = tk.Button(
        janela,
        text="Iniciar automação",
        command=lambda: iniciar(periodo), # Botão que indica para iniciar a automação
        font=("Calibri", 20, "bold"),
        bg="#464559",
        fg="white",
        relief="flat",
        width=20,
        height=2
    )

    botao.pack(pady=20)

# Função que cria a caixa de seleção que permite selecionar o período
def criar_periodo(janela):
    # Insere um texto antes da caixa de seleção
    
    texto_periodo = tk.Label(
        janela,
        text="Selecione um período",
        font=("Calibri", 11),
        bg="#F3F3F6"
    )
    
    texto_periodo.pack(pady=(15,5))
    
    # Cria uma caixa de opções
    
    style = ttk.Style()

    style.configure(
        "TCombobox",
        font=("Calibri", 12)
    )
    
    periodo = ttk.Combobox(
        janela,
        values = [
            "01_31",
            "20_19"
        ],
        state="readonly"
    )
    # Faz com que a seleção já abra na primeira opção
    periodo.current(0)


    periodo.pack(pady=50)


    return(periodo)


def criar_interface():
    
    
    # Cria a janela onde serão exibidas as informações
    janela = tk.Tk()


    # Define o título da janela
    janela.title("Automação Python")


    # Define o tamanho da janela
    janela.geometry("600x400")
    # Define a cor da janela
    janela.configure(bg="#F3F4F6")


    criar_titulo(janela)


    periodo = criar_periodo(janela)


    criar_botão(periodo, janela)


    # Mantem a janela aberta, até que o usuário interaja com ela
    janela.mainloop()


criar_interface()



