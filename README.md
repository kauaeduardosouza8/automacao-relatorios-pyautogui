\# Automação de Relatórios — Linx Big Farma



Projeto em \*\*Python\*\* desenvolvido para automatizar etapas repetitivas da emissão de relatórios utilizados no fechamento de convênios no sistema \*\*ERP Linx Big Farma\*\*.



A aplicação utiliza \*\*PyAutoGUI\*\* para interagir com a interface do ERP e \*\*Tkinter\*\* para disponibilizar uma interface gráfica simples ao operador.



> \*\*Status do projeto:\*\* em desenvolvimento.



\---



\## Objetivo



Automatizar o fluxo de emissão dos relatórios necessários para o fechamento de convênios, reduzindo tarefas manuais como:



\- seleção do período de fechamento;

\- cálculo das datas inicial e final;

\- abertura das telas de relatórios;

\- preenchimento automático dos filtros;

\- seleção dos convênios cadastrados;

\- geração sequencial dos relatórios;

\- preparação dos documentos para impressão.



Atualmente o projeto trabalha com dois tipos principais de relatório:



1\. \*\*Conferência de venda por cupom\*\*;

2\. \*\*Convênio sintético por funcionário\*\*.



\---



\## Tecnologias utilizadas



\- \*\*Python\*\*

\- \*\*PyAutoGUI\*\*

\- \*\*Tkinter\*\*

\- \*\*ttk\*\*

\- \*\*datetime\*\*

\- \*\*calendar\*\*

\- \*\*time\*\*



\---



\## Estrutura do projeto



```text

projeto/

│

├── interface.py

├── main.py

├── base\_de\_dados.py

├── conferencia\_cupom.py

├── relatorio\_convenios.py

└── README.md

```



\### `interface.py`



Responsável pela interface gráfica utilizada pelo operador.



A interface permite:



\- visualizar o título da aplicação;

\- selecionar o período de fechamento;

\- escolher entre os períodos `01\_31` e `20\_19`;

\- iniciar a automação através de um botão.



Ao clicar em \*\*Iniciar automação\*\*, a chave do período selecionado é enviada para:



```python

main.main(chave)

```



Dessa forma, a interface fica responsável apenas pela interação com o usuário, enquanto a execução da automação permanece centralizada no `main.py`.



\---



\### `main.py`



É o arquivo responsável por \*\*orquestrar o fluxo geral da aplicação\*\*.



A função principal recebe a chave selecionada pelo usuário:



```python

def main(chave):

```



A partir dela, o programa:



1\. consulta as datas correspondentes ao período;

2\. executa a emissão do relatório de conferência de vendas por cupom;

3\. executa a emissão do relatório de convênio sintético por funcionário.



Fluxo simplificado:



```text

Interface

&#x20;  │

&#x20;  ▼

main(chave)

&#x20;  │

&#x20;  ├── definir datas

&#x20;  │

&#x20;  ├── relatório de conferência por cupom

&#x20;  │

&#x20;  └── relatório de convênio sintético

```



As principais funções presentes neste arquivo são:



\#### `imprimir\_conferencia\_cupom(chave, inicio, fim)`



Controla o processo do relatório de conferência de vendas por cupom.



Ela:



\- abre o relatório;

\- preenche o período;

\- percorre os convênios cadastrados;

\- aplica cada convênio como filtro;

\- gera o relatório;

\- fecha o relatório antes de continuar para o próximo convênio.



\#### `imprimir\_relatorio\_convenio\_sintetico(chave, inicio, fim)`



Controla o relatório de convênio sintético por funcionário.



Ela:



\- abre a área de relatórios financeiros;

\- aguarda o carregamento;

\- insere as datas inicial e final;

\- chama o loop responsável por percorrer os convênios;

\- prepara cada relatório para impressão.



\#### `main(chave)`



Função central da aplicação.



Responsável por conectar os módulos e executar as automações na ordem definida.



\---



\### `base\_de\_dados.py`



Centraliza as configurações utilizadas pelos demais módulos.



Atualmente contém:



\- períodos disponíveis;

\- dias inicial e final de cada período;

\- convênios pertencentes a cada período;

\- obtenção do ano e mês atuais;

\- geração das datas utilizadas nos relatórios.



Exemplo simplificado:



```python

periodos = {

&#x20;   "01\_31": {

&#x20;       "dia\_inicio": 1,

&#x20;       "dia\_fim": 31,

&#x20;       "convenios": \[

&#x20;           "convenio1",

&#x20;           "convenio2",

&#x20;           "convenio3"

&#x20;       ]

&#x20;   },



&#x20;   "20\_19": {

&#x20;       "dia\_inicio": 20,

&#x20;       "dia\_fim": 19,

&#x20;       "convenios": \[

&#x20;           "convenio4",

&#x20;           "convenio5",

&#x20;           "convenio6"

&#x20;       ]

&#x20;   }

}

```



\#### `criar\_periodo(ano, mes, dia\_inicio, dia\_fim)`



Calcula as datas inicial e final do fechamento e retorna os valores no formato:



```text

DDMMAAAA

```



A função também trata situações como:



\- meses com menos de 31 dias;

\- períodos que terminam no mês seguinte;

\- mudança de dezembro para janeiro do próximo ano.



\#### `definir\_datas\_inicio\_fim(chave)`



Recebe a chave do período, consulta sua configuração no dicionário `periodos` e retorna:



```python

inicio, fim

```



\---



\### `conferencia\_cupom.py`



Contém as funções responsáveis pela automação do relatório de \*\*conferência de vendas por cupom\*\*.



\#### `abrir\_relatorio\_vendas\_por\_cupom()`



Navega pela interface do Linx Big Farma até a opção correspondente ao relatório.



\#### `preencher\_periodo\_vendas\_cupom(inicio, fim)`



Configura o relatório e preenche:



\- data inicial;

\- data final;

\- ordenação utilizada no relatório.



\#### `selecionar\_convenio(convenio)`



Seleciona um convênio no filtro do relatório utilizando o nome recebido como argumento.



\---



\### `relatorio\_convenios.py`



Responsável pela automação do relatório de \*\*convênio sintético por funcionário\*\*.



\#### `abrir\_aba\_relatorio()`



Navega pelo sistema até a tela de relatórios de contas a receber e abre o relatório de convênio sintético.



\#### `inserir\_data\_inicio\_fim(inicio, fim)`



Preenche os campos de data inicial e final.



Também ajusta a estrutura utilizada pelo relatório.



\#### `selecionar\_convenio(convenio)`



Pesquisa e seleciona o convênio informado.



\#### `impressao\_relatorio()`



Abre a tela de impressão/exportação, ajusta a orientação do documento e executa as etapas relacionadas à impressão.



\#### `loop\_impressao\_relatorios(chave)`



Percorre automaticamente todos os convênios cadastrados para o período escolhido:



```python

for convenio in base\_de\_dados.periodos\[chave]\["convenios"]:

```



Para cada convênio, o programa:



1\. seleciona o convênio;

2\. gera o relatório;

3\. executa a rotina de impressão;

4\. continua para o próximo item.



\---



\## Períodos de fechamento



A aplicação possui atualmente dois períodos configurados.



\### `01\_31`



Representa fechamentos realizados dentro do próprio mês.



Exemplo:



```text

01/10/2026 até 31/10/2026

```



Caso o mês possua menos de 31 dias, o programa utiliza automaticamente o último dia válido.



Exemplo:



```text

01/02/2026 até 28/02/2026

```



\### `20\_19`



Representa fechamentos que começam no mês atual e terminam no mês seguinte.



Exemplo:



```text

20/10/2026 até 19/11/2026

```



Na virada do ano, o cálculo também é ajustado automaticamente.



Exemplo:



```text

20/12/2026 até 19/01/2027

```



\---



\## Fluxo de execução



O fluxo atual da aplicação é:



```text

1\. Operador executa interface.py

&#x20;               │

&#x20;               ▼

2\. Interface gráfica é aberta

&#x20;               │

&#x20;               ▼

3\. Operador seleciona o período

&#x20;     ┌─────────┴─────────┐

&#x20;     │                   │

&#x20;   01\_31               20\_19

&#x20;     │                   │

&#x20;     └─────────┬─────────┘

&#x20;               ▼

4\. interface.py chama main.main(chave)

&#x20;               │

&#x20;               ▼

5\. base\_de\_dados.py calcula início e fim

&#x20;               │

&#x20;               ▼

6\. Relatório de conferência por cupom

&#x20;               │

&#x20;               ▼

7\. Convênios do período são percorridos

&#x20;               │

&#x20;               ▼

8\. Relatório sintético por funcionário

&#x20;               │

&#x20;               ▼

9\. Convênios do período são percorridos

&#x20;               │

&#x20;               ▼

10\. Automação é finalizada

```



\---



\## Como executar



\### 1. Requisitos



É necessário possuir uma instalação compatível do Python.



Instale o PyAutoGUI:



```bash

pip install pyautogui

```



O \*\*Tkinter\*\* normalmente já acompanha as instalações padrão do Python para Windows.



\---



\### 2. Abra previamente o Linx Big Farma



A automação pressupõe que o ERP esteja:



\- aberto;

\- com o usuário autenticado;

\- na interface esperada pelo programa;

\- utilizando resolução e escala compatíveis com as coordenadas configuradas.



\---



\### 3. Execute a interface



Utilize:



```bash

python interface.py

```



A janela da aplicação será aberta.



Selecione o período desejado e clique em:



```text

Iniciar automação

```



\---



\## Dependência das coordenadas da tela



O projeto utiliza coordenadas absolutas através de comandos como:



```python

pyautogui.click(x=33, y=393)

```



Isso significa que o funcionamento depende de fatores como:



\- resolução do monitor;

\- escala do Windows;

\- posição da janela do ERP;

\- versão da interface do Linx Big Farma;

\- tamanho e disposição dos elementos visuais.



Caso a aplicação seja utilizada em outro computador, algumas coordenadas provavelmente precisarão ser recalibradas.



\---



\## Segurança durante a execução



Como o PyAutoGUI controla diretamente mouse e teclado, não é recomendado utilizar o computador para outras tarefas durante a execução.



Uma alteração inesperada de janela ou posição pode fazer com que o programa envie comandos para o local incorreto.



Durante os testes, mantenha:



\- o ERP em primeiro plano;

\- a janela maximizada conforme o ambiente utilizado no desenvolvimento;

\- teclado e mouse sem interferência manual;

\- dados fictícios ou ambiente controlado sempre que possível.



\---



\## Estado atual da impressão



Alguns comandos responsáveis pelo envio definitivo à impressora ainda estão comentados no código durante a fase de testes.



Exemplo:



```python

\# pyautogui.click(...)

\# pyautogui.press("enter")

```



Portanto, antes de considerar a automação pronta para produção, é necessário revisar e validar as etapas finais de impressão nos dois relatórios.



Essa abordagem evita uma interessante experiência corporativa conhecida como \*\*imprimir dezenas de relatórios errados automaticamente\*\*.



\---



\## Limitações atuais



O projeto ainda possui algumas limitações:



\- dependência de coordenadas fixas;

\- ausência de detecção automática de telas;

\- ausência de validação visual do estado do ERP;

\- tratamento de erros ainda limitado;

\- ausência de logs estruturados;

\- automação executada de forma sequencial;

\- dependência da posição correta da aplicação;

\- impressão definitiva ainda em fase de teste.



\---



\## Melhorias planejadas



Algumas evoluções possíveis para as próximas versões:



\- \[ ] implementar tratamento de exceções;

\- \[ ] detectar erros durante a execução;

\- \[ ] validar se o Linx Big Farma está na tela correta;

\- \[ ] adicionar mensagens de status na interface gráfica;

\- \[ ] desabilitar o botão enquanto a automação estiver executando;

\- \[ ] adicionar barra de progresso;

\- \[ ] criar sistema de logs;

\- \[ ] registrar relatórios emitidos;

\- \[ ] permitir selecionar mês e ano manualmente;

\- \[ ] permitir escolher quais relatórios serão emitidos;

\- \[ ] adicionar confirmação antes de iniciar;

\- \[ ] substituir progressivamente coordenadas absolutas por métodos de detecção visual;

\- \[ ] criar arquivo externo de configuração;

\- \[ ] gerar uma versão executável da aplicação.



\---



\## Arquitetura atual



A separação dos arquivos segue uma divisão simples de responsabilidades:



```text

interface.py

&#x20;   │

&#x20;   │ interação com o usuário

&#x20;   ▼

main.py

&#x20;   │

&#x20;   │ controla o fluxo

&#x20;   ├───────────────┐

&#x20;   ▼               ▼

conferencia\_     relatorio\_

cupom.py         convenios.py

&#x20;   │               │

&#x20;   └───────┬───────┘

&#x20;           ▼

&#x20;    base\_de\_dados.py

```



Essa estrutura facilita a manutenção porque evita concentrar toda a automação em um único arquivo.



\---



\## Observação sobre execução direta do `main.py`



A função principal atualmente foi definida para receber uma chave:



```python

def main(chave):

```



Por isso, o fluxo recomendado é iniciar a aplicação através de:



```bash

python interface.py

```



A interface fornece a chave necessária antes de chamar `main()`.



Caso o `main.py` seja executado diretamente, a chamada presente no bloco:



```python

if \_\_name\_\_ == "\_\_main\_\_":

```



deve fornecer uma chave válida ou possuir uma rotina própria para solicitá-la.



\---



\## Dados do repositório



Os nomes de convênios apresentados na versão pública do projeto podem ser substituídos por valores fictícios para evitar a exposição de informações utilizadas no ambiente real.



\---



\## Finalidade



Este projeto foi desenvolvido principalmente para:



\- aprendizado de Python;

\- estudo de automação de tarefas;

\- aplicação prática de modularização;

\- integração entre interface gráfica e automação;

\- redução de tarefas repetitivas em ambiente administrativo.



O projeto continua sendo expandido conforme novas rotinas são automatizadas.



