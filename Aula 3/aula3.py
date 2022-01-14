# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# ### Selenium permite controlar tudo do seu navegador.
# 
# Quando usar Selenium, XPATH sempre em aspas simples.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as By
from IPython.display import display
import pandas as pd

# Abrir navegador

navegador = webdriver.Chrome()

# Cotação Dólar

navegador.get('https://google.com.br')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('cotação dolar')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Cotação Euro

navegador.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/input').clear()
navegador.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Cotação Ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_dolar)
print(cotacao_euro)
print(cotacao_ouro)
navegador.quit()

# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

tabela = pd.read_excel('Produtos.xlsx')

# - Atualizando os preços e o cálculo do Preço Final

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']
display(tabela)

# ### Agora vamos exportar a nova base de preços atualizada

tabela.to_excel('Produtos Novo.xlsx', index=False)
