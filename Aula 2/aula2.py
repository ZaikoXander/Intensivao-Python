# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# Importar a Base de Dados

import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

# Visualizar Base de Dados
tabela = tabela.drop('Unnamed: 0', axis=1)
display(tabela)

# Tratamento de Dados

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)

print(tabela.info())
display(tabela)

# Análise Inicial

display(tabela['Churn'].value_counts())
display(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # Para colocar formatação de porcentagem

# Análise mais completa

import plotly.express as px

for coluna in tabela.columns:
    if coluna != "IDCliente":
        grafico = px.histogram(tabela, x=coluna, color="Churn")
        grafico.show()
        display(tabela.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente'])

# ### Conclusões e Ações

# Escreva aqui suas conclusões:

# Análise de Dados chega em você como um desafio.
# A base de dados muitas vezes vai vir com problemas. E você terá que corrigir esses erros.
# Você tem que confirmar as hipoteses(problemas relatados pela empresa).
# E terá que analisar a causa do problema caso as hipoteses sejam verdadeiras.
# 
# Base de Dados? pandas SEMPRE
# 
# Churn é quando alguém cancela a assinatura.
# * Tratamento de Dados
#     * Informação que não te ajuda, te atrapalha.
#         * Coluna inútil
#             * 0 => linha
#             * 1 => coluna
#         * Valores reconhecidos de forma errada
#             * Sempre depois de tirar valores inúteis, o seguinte é identificar valores reconhecidos de forma errada.
#             * object => texto
#             * int => número inteiro
#             * float => número com casa decimal
#         * Valores vazios(NaN)
#             * Excluir colunas vazias
#             * Excluir linhas vazias
#     * Ver se seu chefe ta errado kkk
#         * 26% -- 2,6%
#     * No final de tudo o que você quer é encontrar um padrão(causa).
#         * Encontrar algo que salta os olhos
#             * Pessoas com famílias menores tem mais chance de cancelar
#                 * Podemos criar um plano família para diminuir a taxa de cancelamento
#             * Estamos perdendo muitos clientes nos primeiros meses
#                 * Tem alguma ação promocional que tá trazendo muito cliente desqualificado
#                 * Podemos pensar em dar bônus pro cliente nos primeiros meses
#                 * A 1ª experiência do cliente pode estar sendo muito ruim
#             * Estamos com um problema na Fibra
#                 * Podemos arruma sadisgraça
#             * Quanto mais serviços o cliente tem menor a chance dele cancelar
#                 * Podemos fazer promoções com mais serviços pro cliente
#             * Forma de pagamento
#                 * Evitar boleto eletronico, vamos dar desconto nas outras opções


