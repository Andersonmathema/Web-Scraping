from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoDeEspera
import pandas as pd


#pip install virtualenv
#python -m venv venv 
#pip install -r requirements.txt

# Aguarda o carregamento da página
tempoDeEspera.sleep(5)

# Inicia o navegador
navegador = opcoesSelenium.Chrome()

# Acessa a página
navegador.get('https://rpachallengeocr.azurewebsites.net/')

# Lista para armazenar os dados
listaDataFrame = []

# Itera para capturar dados das tabelas
for i in range(3):  # Captura de 3 páginas
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    tempoDeEspera.sleep(1)
    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    
    for linhaAtual in linhas[1:]:  # Ignora o cabeçalho
        dadosLinha = linhaAtual.find_elements(By.TAG_NAME, 'td')
        print(f"Linhas encontradas: {len(dadosLinha)} colunas")  # Mensagem de depuração
        if len(dadosLinha) == 5:  # Verifica se a linha tem 5 colunas
            linhaTexto = [dado.text for dado in dadosLinha]
            listaDataFrame.append(linhaTexto)
        else:
            print(f"Erro: Linha com número incorreto de colunas: {len(dadosLinha)}")  # Mensagem de depuração
    
    # Aguarda e clica no botão 'Next' para a próxima página
    tempoDeEspera.sleep(2)
    try:
        next_button = navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]')
        next_button.click()
    except Exception as e:
        print(f"Erro ao clicar no botão 'Next': {e}")  # Mensagem de depuração
        break
    tempoDeEspera.sleep(2)

# Fecha o navegador
navegador.quit()

# Converte a lista de dados em DataFrame
colunas = ['ID', 'Due Date', 'Task Description', 'Priority', 'Status']
if listaDataFrame:
    dataFrame = pd.DataFrame(listaDataFrame, columns=colunas)

    # Prepara o arquivo excel usando o xlsxwriter como mecanismo
    with pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter') as arquivoExcel:
        dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

    print('Dados extraídos com sucesso e salvos em "dadosAbasSite.xlsx"!')
else:
    print('Nenhum dado foi extraído.')

