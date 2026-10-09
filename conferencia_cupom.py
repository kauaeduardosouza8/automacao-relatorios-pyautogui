# Automação para impressão do relatório de conferência de vendas por cupom
# Desenvolvido para uso no Sistema ERP Linx Big Farma


import pyautogui
from time import sleep
import base_de_dados
import pygetwindow as gw


# Define a pausa do pyautogui
pyautogui.PAUSE = 0.5


# Funções do sistema


# Função que abre o relatório de vendas por cupom
def abrir_relatorio_vendas_por_cupom():
    # Abre a interface de emissão do relatório


    # Clica na aba de relatórios
    pyautogui.click(x=33, y=393)

    # Clica no sub-aba de vendas
    pyautogui.click(x=168, y=244)

    # Clica na função de confêrencia de venda por cupom
    pyautogui.click(x=241, y=290)


# Função ajusta a formatação e preenche o período do relatório
def preencher_periodo_vendas_cupom(inicio, fim):
    # Marca a ordenação por cliente
    pyautogui.click(x=640, y=230)

    # Clica no campo de período
    pyautogui.click(x=543, y=395)

    # Define a data inicial
    pyautogui.write(inicio)
    pyautogui.press('enter')
    pyautogui.press('enter')


    # Define a data final
    pyautogui.write(fim)


# Clica no filtro de convenio
def selecionar_convenio(convenio):    
    pyautogui.click(x=558, y=498)
    # Limpa seleção
    pyautogui.press('f7')
    # Pesquisa a convenio pelo nome
    pyautogui.write(convenio)
    # Marca a seleção
    pyautogui.press('f5')
    pyautogui.press('enter')
    # Visualiza o relatório
    pyautogui.press('f3')


def imprimir_conferencia_cupom(chave, inicio, fim):
# Impressão do relatório de conferência de venda por cupom


    abrir_relatorio_vendas_por_cupom()


    janela = gw.getWindowsWithTitle('Conferência de Venda por Cupom')


    while janela:


        preencher_periodo_vendas_cupom(inicio, fim)


        for convenio in base_de_dados.periodos[chave]['convenios']: 
            
            
            # Define o filtro da convenio
            selecionar_convenio(convenio)

            
            sleep(1.5)

            
            # Envia o relatório para impressão
            #pyautogui.click(x=101, y=60)
            #pyautogui.press('enter')
            
            # Fecha o relatório
            pyautogui.click(x=756, y=59)


        # Fecha a tela de conferência de venda por cupom
        pyautogui.press('esc')


        janela = gw.getWindowsWithTitle('Conferência de Venda por Cupom')


        print('=' * 60)
        print('Finalizando impressão relatório de vendas por cupom')
        print('=' * 60)











