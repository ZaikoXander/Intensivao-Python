# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# 
# - Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# ### Passo a Passo de um Projeto de Ciência de Dados
# 
# - Passo 1: Entendimento do Desafio
# - Passo 2: Entendimento da Área/Empresa
# - Passo 3: Extração/Obtenção de Dados
# - Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# - Passo 5: Análise Exploratória
# - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# - Passo 7: Interpretação de Resultados

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# - TV, Jornal e Rádio estão em milhares de reais
# - Vendas estão em milhões

# #### Importar a Base de dados

from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

df = pd.read_csv('advertising.csv')
display(df)

# Limpeza de Dados

display(df.info())

# #### Análise Exploratória
# - Vamos tentar visualizar como as informações de cada item estão distribuídas
# - Vamos ver a correlação entre cada um dos itens


sns.pairplot(df)
plt.show()

# Este gráfico não me pareceu muito esclarecedor. Vamos a outro exemplo.

sns.heatmap(df.corr(), cmap='Wistia', annot=True)
plt.show()

# ##### Conclusão:
# Os melhores investimentos são TV e Rádio, mas apenas TV(que está acima de 0.5 == 50%) tem equação matemática positiva.
# 
# Parece-me que a quantidade de investimento em TV está diretamente relacionada a quantidade de Milhões em Vendas.

# #### Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# 
# - Separando em dados de treino e dados de teste


# X é o valor que você irá usar para fazer a previsão
# Y é o valor que você quer prever

x = df[['TV', 'Radio', 'Jornal']] # df.drop('Vendas', axis=1)
y = df['Vendas']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # random_State=1 => Valor seed do aleatório

# #### Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# 
# - Regressão Linear
# - RandomForest (Árvore de Decisão)


# Criação da IA
lin_reg = LinearRegression()
rf_reg = RandomForestRegressor()

# Treino da IA
lin_reg.fit(x_train, y_train)
rf_reg.fit(x_train, y_train)

# #### Teste da AI e Avaliação do Melhor Modelo
# 
# - Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

# Identificando a IA com melhores resultados
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
r2_rf = metrics.r2_score(y_test, test_pred_rf)

print(f'R² da Regressão Linear: {r2_lin}')
print(f'R² da Random Forest: {r2_rf}')

# #### Visualização Gráfica das Previsões

# O melhor modelo é o RandomForest
df_resultado = pd.DataFrame()

df_resultado['y_teste'] = y_test
df_resultado['y_previsao_lin'] = test_pred_lin
df_resultado['y_previsao_rf'] = test_pred_rf

plt.figure(figsize=(15, 6))
sns.lineplot(data=df_resultado)
plt.show()

# #### Como fazer uma nova previsão?

# importar nova tabela com as informações de propaganda em TV, Radio e Jornal
# passa a nova tabela para o predict do seu modelo

new_df = pd.read_csv('novos.csv')
display(new_df)
previsao = rf_reg.predict(new_df).round(1) # Apenas uma casa decimal
print(previsao)
new_df['Previsao Vendas'] = previsao
display(new_df)
new_df.to_csv('novos previsao.csv', index=False)

importancia_features = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
plt.figure(figsize=(5, 5))
sns.barplot(x=importancia_features.index, y=importancia_features[0])
plt.show()
