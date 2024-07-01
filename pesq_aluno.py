from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os valores das variáveis de ambiente
password = os.getenv('PASSWORD')
documento = os.getenv('DOCUMENTO')

navegador = opcoesSelenium.Chrome()


def login(): # Login
    navegador.get('https://cmsp-tms.ip.tv')
    time.sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
    time.sleep(2)
    navegador.find_element(By.ID, 'document').send_keys(documento)
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[3]/form/div/div[1]/div/div/div').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id=":r4:"]/li[1]').click()
    time.sleep(2)
    navegador.find_element(By.ID, 'password').send_keys(password)
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/form/div/div[5]/button').send_keys(Keys.ENTER)
    time.sleep(2)


def capturar_nome_prof():
    prof = navegador.find_element(By.CLASS_NAME, 'MuiTypography-h5').text.split()[2]
    time.sleep(1)
    #return print(prof)


def clicar_botao_txt(texto_link):
        botao = navegador.find_element(By.XPATH, f'//button[text()="{texto_link}"]')
        botao.click()      


def exibir_menu():
    print("Escolha a sala: ")
    print("1. 1B")
    print("2. 1C")
    print("3. 2A")  
    print("4. 2B")  
    print("5. 2C")  
    
def lista_alunos():
    while True:
        try:
            opc = int(input("Sua escolha: "))
            if opc == 1:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/1B.csv"
            elif opc == 2:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/1C.csv"
            elif opc == 3:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2A.csv"
            elif opc == 4:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2B.csv"
            elif opc == 5:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2C.csv"
            else:
                print("Opção inválida. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")
    
    df_excel = pd.read_csv(file_path, sep=';')
    return df_excel


def alunos():
    df_alunos = lista_alunos()
    dados = df_alunos[['Nome', 'ID_Aluno']].values.tolist()

    # Exibir a lista de alunos com seus índices
    for i, (nome, id_aluno) in enumerate(dados):
        print(f"{i}: {nome}")

    while True:
        try:
            opc = int(input("Escolha o número do aluno: "))
            if 0 <= opc < len(dados):
                id_aluno = dados[opc][1]
                return id_aluno
            else:
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")    


if __name__ == '__main__':
    exibir_menu()
    print(lista_alunos())
    id = alunos()

    login()
    capturar_nome_prof()
    navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/button/div').click() #Aba Atividades
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/div/div/div/ul/li[3]/a/div').click() # Respostas
    time.sleep(2)
    navegador.find_element(By.ID, ':rv:').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id=":r10:"]/li[4]').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id=":r11:"]').send_keys(id)
    time.sleep(2)
    clicar_botao_txt('Procurar')
    time.sleep(900)

    navegador.close()




    
