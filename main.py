# Programa para automação total da rotina de emissão de relatórios para fechamento de convênio
# Desenvolvido para uso no sistema ERP Linx Big Farma
# Automação deve ser utilizada com sistema previamente aberto

import pyautogui
from time import sleep
import base_de_dados
import relatorio_convenios
import conferencia_cupom



def imprimir_conferencia_cupom(chave, inicio, fim):
    # Impressão do relatório de conferência de venda por cupom


    conferencia_cupom.abrir_relatorio_vendas_por_cupom()


    conferencia_cupom.preencher_periodo_vendas_cupom(inicio, fim)


    for convenio in base_de_dados.periodos[chave]['convenios']: 
            
            
            # Define o filtro da convenio
            conferencia_cupom.selecionar_convenio(convenio)

            
            sleep(1.5)

            
            # Envia o relatório para impressão
            #pyautogui.click(x=101, y=60)
            #pyautogui.press('enter')
            
            # Fecha o relatório
            pyautogui.click(x=756, y=59)


    # Fecha a tela de conferência de venda por cupom
    pyautogui.press('esc')


    print('=' * 60)
    print('Finalizando impressão relatório de vendas por cupom')
    print('=' * 60)

    


# Impressão do relatório convênio sintetico por funcionário

def imprimir_relatorio_convenio_sintetico(chave, inicio, fim):
    # Chama a função que abre a aba de relatórios
    relatorio_convenios.abrir_aba_relatorio()


    # Dá um intervalo de tempo para que o sistema de relatórios abra
    sleep(10)


    # Insere no filtro as datas de ínicio e fim
    relatorio_convenios.inserir_data_inicio_fim(inicio, fim)


    sleep(5)


    # Realiza a impressão dos relatórios
    relatorio_convenios.loop_impressao_relatorios(chave)


    print('=' * 60)
    print('Finalizando impressão relatório convênio sintético por funcionário')
    print('=' * 60)


def main():


    # Programa solicita o período para o operador
    chave =  base_de_dados.definiçao_chave()


    # Utiliza a base de dados para obter a data de inicio e fim formatada
    inicio, fim = base_de_dados.definir_datas_inicio_fim(chave)


    imprimir_conferencia_cupom(chave, inicio, fim)


    imprimir_relatorio_convenio_sintetico(chave, inicio, fim)



if __name__ == "__main__":
     main()