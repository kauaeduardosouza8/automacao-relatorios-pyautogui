from datetime import date, timedelta
import calendar


# Define data atual / Poderá ser substituido por data necessária para emissão do relatório
hoje = date.today()
ano_atual =  hoje.year
mes_atual = hoje.month


# Define a data de ínicio e fim do período de fechamento

def criar_periodo(ano, mes, dia_inicio, dia_fim):


    # Define o último dia do mês
    ultimo_dia = calendar.monthrange(ano, mes)[1]


    # Verifica se o mês possui menos de 31 dias
    data_inicio = (date(ano, mes, dia_inicio)).strftime('%d%m%Y')

    
    # Verifica o período do vencimento e ajusta o a data final para próximo mês e ano caso necessário
    if dia_fim == 19:
            mes_fim = mes + 1
            if mes_fim > 12:
                 mes_fim = 1
                 ano += 1
            data_final = date(ano, mes_fim, dia_fim).strftime('%d%m%Y')

    
    # Ajusta caso o último dia do mês seja menor do que o dia final
    elif dia_fim > ultimo_dia:
        dia_fim =  ultimo_dia
        data_final = date(ano, mes, dia_fim).strftime('%d%m%Y')
    else:
         data_final = date(ano, mes, dia_fim).strftime('%d%m%Y')

    return data_inicio, data_final


# Define o período de vencimento de cada convênio usando o nome como chave principal
def criar_periodo_convenio(nome_convenio, ano, mes):

    # Encontra o tipo do período no dicionário de convênios
    tipo_periodo = convenios[nome_convenio]

    # Armazena o dicionário com os períodos em uma variavel
    periodo = periodos[tipo_periodo]

    # Utiliza as chaves para acessar o contéudo do dicionário
    dia_inicio = periodo['dia_inicio']
    dia_fim = periodo['dia_fim']

    return criar_periodo(
         ano,
         mes,
         dia_inicio,
         dia_fim
    )



# Define os períodos de venda e os convênios pertencentes a cada um

periodos  = {
    '01_31' : {
        "dia_inicio" : 1,
        "dia_fim" : 31,
        "empresas" : [
            'empresa1',
            'empresa2',
            'empresa3',
        ]
    },
    '20_19' : {
        'dia_inicio' : 20,
        'dia_fim' : 19,
        'empresas' : [
            'empresa4',
            'empresa5',
            'empresa6',
        ]
    }
}


# Define os convênios

convenios = {
    'empresa1' : '01_31',
    'empresa2' : '01_31',
    'empresa3' : '01_31',   
    'empresa4' : '20_19',
    'empresa5' : '20_19',
    'empresa6' : '20_19',
}





