from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

navegador = opcoesSelenium.Chrome()

def login():
    # Obter os valores das variáveis de ambiente
    password = os.getenv('PASSWORD')
    documento = os.getenv('DOCUMENTO')
    navegador.get('https://sed.educacao.sp.gov.br/')
    time.sleep(5)
    navegador.find_element(By.ID, 'name').send_keys('rg' + documento + 'sp')
    time.sleep(2)
    navegador.find_element(By.ID, 'senha').send_keys(password)
    time.sleep(2)
    try:
        navegador.find_element(By.ID, 'botaoEntrar').click()
    except Exception(e):
        print(e)
    time.sleep(40)


def mapao():
    navegador.find_element(By.ID, 'decorMenuFilterTxt').send_keys('mapão nominal',Keys.ENTER)
    time.sleep(5)

    # Tipo de ensino
    navegador.find_element(By.ID, 'filt-grupotipoEnsino').click()
    time.sleep(2)
    navegador.find_element(By.ID, 'bs-select-6-6').click()
    time.sleep(2)

    # Turma - def por fora para escolha, ou loop
    navegador.find_element(By.ID, '').click()
    time.sleep(2)
    navegador.find_element(By.ID, '').click()
    time.sleep(2)
    
    # Tipo de fechamento
    navegador.find_element(By.ID, '').click()
    time.sleep(2)
    navegador.find_element(By.ID, '').click()
    time.sleep(2)
    

    
if __name__ == "__main__":
    login()
    mapao()




