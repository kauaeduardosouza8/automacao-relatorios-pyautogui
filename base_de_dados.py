from datetime import date, timedelta
import calendar


# Define data atual / Poderá ser substituido por data necessária para emissão do relatório
hoje = date.today()
ano_atual =  hoje.year
mes_atual = hoje.month

# Define os períodos de venda e os convênios pertencentes a cada um


periodos  = {
    '01_31' : {
        "dia_inicio" : 1,
        "dia_fim" : 31,
        "convenios" : [
            'convenio1',
            'convenio2',
            'convenio3',
        ]
    },
    '20_19' : {
        'dia_inicio' : 20,
        'dia_fim' : 19,
        'convenios' : [
            'convenio4',
            'convenio5',
            'convenio6',
        ]
    }
}


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


# Função que determina ínicio e fim com base na chave informada pelo usuário
def definir_datas_inicio_fim(chave):
    
    
    dia_inicio = periodos[chave]['dia_inicio']
    dia_fim = periodos[chave]['dia_fim']


    inicio, fim = criar_periodo(
        ano_atual,
        mes_atual,
        dia_inicio,
        dia_fim
        )

    return inicio, fim










