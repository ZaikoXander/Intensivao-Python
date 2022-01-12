# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

import pyautogui
import pyperclip
from time import sleep

pyautogui.PAUSE = 1

pyautogui.alert('Vai começar, aperte OK e não mexa em nada')
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')
site = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing'
pyperclip.copy(site)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(313, 297, clicks=2)
sleep(5)
pyautogui.click()
pyautogui.click(1713, 181)
pyautogui.click(1454, 584)
caminho = 'D:\Programação\ArquivosGerais\IntensivãoPython\Aula 1'
pyperclip.copy(caminho)
sleep(5)
pyautogui.click(1177, 219)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.click(1328, 709)

# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

import pandas as pd
from IPython.display import display

caminho = r'D:/Programação/ArquivosGerais/IntensivãoPython/Aula 1/Vendas - Dez.xlsx'
df = pd.read_excel(caminho)
display(df)

faturamento = df['Valor Final'].sum()
quantidade = df['Quantidade'].sum()

# ### Vamos agora enviar um e-mail pelo gmail

pyautogui.hotkey('ctrl', 't')
gmail = 'https://mail.google.com'
pyperclip.copy(gmail)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)

pyautogui.click(65, 234)
pyautogui.write('pythonimpressionador+diretoria@gmail.com')
pyautogui.press('tab', presses=2)
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f"""

Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
ZaikoXander"""
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

# #### Use esse código para descobrir qual a posição de um item que queira clicar
# 
# - Lembre-se: a posição na sua tela é diferente da posição na minha tela

"""
sleep(5)
print(pyautogui.position())
"""

