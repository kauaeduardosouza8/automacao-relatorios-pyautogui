# Automação com foco em emissão de relatórios para fechamento de convênios
# Desenvolvido para uso no Sistema ERP Linx Big Farma


import pyautogui
from time import sleep
from datetime import date
import base_de_dados


# Funções do programa 


# Define o tempo de pausa do pyautogui
pyautogui.PAUSE = 0.5

# Função que seleciona um convenio no visualizador de relatórios
def selecionar_convenio(convenio):
    pyautogui.doubleClick(x=468, y=170) # clica no filtro de convenio
    sleep(1)
    pyautogui.press('f7') # limpa o campo de seleção
    pyautogui.click(x=504, y=257) # clica na caixa de texto do filtro
    pyautogui.write(convenio) # informa o nome do convênio
    pyautogui.press('f5')
    pyautogui.press('f3')


#  Função que realiza a abertura da aba de relatórios atualizada
def abrir_aba_relatorio():
    # Clica na aba financeiro
    pyautogui.click(x=33, y=290) 


    # Rola a tela para encontrar a aba de relatório
    pyautogui.moveTo(x=242, y=297)
    for _ in range(5):
        pyautogui.scroll(-10)
    

    # clica na aba de relatório contas a receber
    pyautogui.click(x=243, y=628) 
    # clica na aba de convênio sintético por funcionário
    pyautogui.click(x=249, y=299) 
    pyautogui.press('enter')


# Função que define data de ínicio e fim do período de vendas
def  inserir_data_inicio_fim(inicio, fim):

    # clica no campo de data de inicio
    pyautogui.click(x=81, y=231) 


    # Preenche a data de ínicio
    pyautogui.write(inicio[:2])
    pyautogui.press('right')
    pyautogui.write(inicio[2:4])
    pyautogui.press('right')
    pyautogui.write(inicio[4:])


    # Clica no campo de data limite
    pyautogui.click(x=252, y=234) 


    # Preenche data limite
    pyautogui.write(fim[:2])
    pyautogui.press('right')
    pyautogui.write(fim[2:4])
    pyautogui.press('right')
    pyautogui.write(fim[4:])

    # Ajusta estrutura do relatório
    pyautogui.click(x=256, y=345) # clica no campo estrutura do relatório
    pyautogui.press('down') # muda para sem agrupamento por cliente


def impressao_relatorio():
            # Envia o documento para impressão


            pyautogui.doubleClick(x=1271, y=345) # Clica em imprimir / exportar


            # Intervalo para que o sistema de impressão carregue
            sleep(3)


            # Ajusta a orientação do relatório
            pyautogui.click(x=496, y=72) # Clica em orientation
            pyautogui.click(x=512, y=129) # seleciona portrait


            # Envia o documento para impressão
            #pyautogui.click(x=158, y=63) # Clica em quick print

            # Fecha o documento da impressão
            sleep(2)
            pyautogui.click(x=1325, y=61)


def loop_impressao_relatorios(chave):
    # Passa por todos elementos do período e emite os relatórios
    for convenio in base_de_dados.periodos[chave]['convenios']:

        # Chama função que insere o convênio no filtro
        selecionar_convenio(convenio)


        # Realiza a impressão do relatório
        impressao_relatorio()
        






