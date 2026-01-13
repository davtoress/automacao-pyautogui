import pyautogui
import time
import pandas

pyautogui.PAUSE = 2

#Abrir o navegador:
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#Inserir o link do site:

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

#Cadrastar o email e depois a senha:

pyautogui.click(x=754, y=404)
pyautogui.write("davitorres@gmail.com")
pyautogui.press("tab")
pyautogui.write("algumasenha")
pyautogui.press("tab")
pyautogui.press("enter")

#Ler a planinha do sistema:

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=804, y=283)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Só escreve a observação se ela existir:
    if not pandas.isna(tabela.loc[linha, "obs"]):
     pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")