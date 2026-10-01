\# Automação de Relatórios com Python e PyAutoGUI



Projeto desenvolvido para automatizar a emissão de relatórios

em uma aplicação desktop utilizando Python e PyAutoGUI.



\## Objetivo



Automatizar tarefas repetitivas relacionadas à emissão de relatórios,

incluindo:



\- seleção do período;

\- preenchimento automático das datas;

\- seleção de empresas;

\- geração dos relatórios;

\- envio automático para impressão.



\## Tecnologias utilizadas



\- Python

\- PyAutoGUI

\- datetime

\- calendar



\## Estrutura



\### relatorio\_convenios.py



Responsável pela automação da interface gráfica.



\### base\_de\_dados.py



Responsável pela configuração das empresas, períodos e cálculo

das datas utilizadas nos relatórios.



\## Funcionamento



O usuário seleciona um período de fechamento.



O programa então:



1\. acessa o módulo de relatórios;

2\. calcula as datas correspondentes;

3\. preenche os filtros;

4\. percorre as empresas cadastradas;

5\. gera o relatório;

6\. envia o relatório para impressão.



\## Observações



A automação utiliza coordenadas de tela através do PyAutoGUI.



Por esse motivo, pode ser necessário ajustar as coordenadas para

diferentes resoluções de tela, configurações de escala ou versões

da aplicação utilizada.



Os nomes utilizados neste repositório são fictícios e não

representam os dados utilizados no ambiente original.

