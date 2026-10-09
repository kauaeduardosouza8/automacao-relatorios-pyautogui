# Programa para automação total da rotina de emissão de relatórios para fechamento de convênio
# Desenvolvido para uso no sistema ERP Linx Big Farma
# Automação deve ser utilizada com sistema previamente aberto

from time import sleep
import base_de_dados
import interface
from relatorio_convenios import imprimir_relatorio_convenio_sintetico
from conferencia_cupom import imprimir_conferencia_cupom


def main():

    chave = interface.criar_interface()

    # Utiliza a base de dados para obter a data de inicio e fim formatada
    inicio, fim = base_de_dados.definir_datas_inicio_fim(chave)


    imprimir_conferencia_cupom(chave, inicio, fim)


    imprimir_relatorio_convenio_sintetico(chave, inicio, fim)


if __name__ == "__main__":
     main()