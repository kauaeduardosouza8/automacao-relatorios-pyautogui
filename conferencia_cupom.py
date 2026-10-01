# Automação para impressão do relatório de conferência de vendas por cupom
# Desenvolvido para uso no Sistema ERP Linx Big Farma
# Automação deve ser iniciada com o Sistema aberto previamente

import pyautogui
from time import sleep
from datetime import date
import base_de_dados_nomes_reais
hoje = date.today()
ano_atual = hoje.year
mes_atual = 9
pyautogui.PAUSE = 0.8

empresa = 'contmax'

# Solicita do usuário o fechamento buscado
fechamento = int(input("Qual período de fechamento gostaria de imprimir? [1](01-31) [2](20-19) "))
if fechamento == 1:
    chave = '01_31'
if fechamento == 2:
    chave = '20_19'
sleep(5)


# Utiliza a função para determinar data de ínicio e fim do período
dia_inicio = base_de_dados_nomes_reais.periodos[chave]['dia_inicio']
dia_fim = base_de_dados_nomes_reais.periodos[chave]['dia_fim']


inicio, fim = base_de_dados_nomes_reais.criar_periodo(
    ano_atual,
    mes_atual,
    dia_inicio,
    dia_fim
    )


pyautogui.PAUSE = 0.5


# Abre a interface de emissão do relatório


# Clica na aba de relatórios
pyautogui.click(x=33, y=393)

# Clica no sub-aba de vendas
pyautogui.click(x=168, y=244)

# Clica na função de confêrencia de venda por cupom
pyautogui.click(x=241, y=290)


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


for empresa in base_de_dados_nomes_reais.periodos[chave]["empresas"]:
    # Define o filtro da empresa (Posteriormente inserir no loop)

    # Clica no filtro de empresa
    pyautogui.click(x=558, y=498)
    # Limpa seleção
    pyautogui.press('f7')
    # Pesquisa a empresa pelo nome
    pyautogui.write(empresa)
    # Marca a seleção
    pyautogui.press('f5')
    pyautogui.press('enter')
    # Visualiza o relatório
    pyautogui.press('f3')

    
    sleep(1.5)
    # Envia o relatório para impressão
    #pyautogui.click(x=101, y=60)
    #pyautogui.press('enter')
    
    # Fecha o relatório
    pyautogui.click(x=756, y=59)








