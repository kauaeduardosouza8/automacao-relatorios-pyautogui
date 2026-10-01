# Automação com foco em emissão de relatórios para fechamento de convênios
# Desenvolvido para uso no Sistema ERP Linx Big Farma


import pyautogui
from time import sleep
from datetime import date
import base_de_dados
hoje = date.today()
ano_atual = hoje.year
mes_atual = hoje.month

# Função que seleciona uma empresa no visualizador de relatórios
def selecionar_convenio(convenio):
    pyautogui.doubleClick(x=468, y=170) # clica no filtro de empresa
    sleep(1)
    pyautogui.press('f7') # limpa o campo de seleção
    pyautogui.click(x=504, y=257) # clica na caixa de texto do filtro
    pyautogui.write(convenio) # informa o nome do convênio
    pyautogui.press('f5')
    pyautogui.press('f3')


pyautogui.PAUSE = 0.5

fechamento = int(input("Qual período de fechamento gostaria de imprimir? [1](01-31) [2](20-19) "))
if fechamento == 1:
    chave = '01_31'
if fechamento == 2:
    chave = '20_19'
sleep(5)

# Clica na aba financeiro
pyautogui.click(x=33, y=290) 


# Rola a tela para encontrar a aba de relatório
pyautogui.moveTo(x=242, y=297)
pyautogui.scroll(-10)
pyautogui.scroll(-10)
pyautogui.scroll(-10)
pyautogui.scroll(-10)
pyautogui.scroll(-10)

# clica na aba de relatório contas a receber
pyautogui.click(x=243, y=628) 
# clica na aba de convênio sintético por funcionário
pyautogui.click(x=249, y=299) 
pyautogui.press('enter')


# Dá um intervalo de tempo para que o sistema de relatórios abra
sleep(10)


# Inicio do loop de impressão dos relatórios


dia_inicio = base_de_dados.periodos[chave]['dia_inicio']
dia_fim = base_de_dados.periodos[chave]['dia_fim']


inicio, fim = base_de_dados.criar_periodo(
    ano_atual,
    mes_atual,
    dia_inicio,
    dia_fim
    )

# Insere a data de ínicio e dim no filtro


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

sleep(5)


# Passa por todos elementos do período e emite os relatórios
for convenio in base_de_dados.periodos[chave]["empresas"]:

    #c Chama função que insere o convênio no filtro
    selecionar_convenio(convenio)
    

    # confirma seleção
    pyautogui.press('f3') 


    # Envia o documento para impressão


    pyautogui.doubleClick(x=1271, y=345) # Clica em imprimir / exportar


    # Intervalo para que o sistema de impressão carregue
    sleep(3)


    # Ajusta a orientação do relatório
    pyautogui.click(x=496, y=72) # Clica em orientation
    pyautogui.click(x=512, y=129) # seleciona portrait


    # Envia o documento para impressão
    pyautogui.click(x=158, y=63) # Clica em quick print

    # Fecha o documento da impressão
    sleep(2)
    pyautogui.click(x=1325, y=61)


print("Finalizando automação!")


