from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

#pip install virtualenv
#python -m venv venv 
#pip install -r requirements.txt

def clicar_radio1():
    # Encontra o primeiro input do tipo rádio na tabela e clica nele
    radio1 = navegador.find_element(By.CSS_SELECTOR, 'tbody tr:first-child input[type="radio"]')
    radio1.click()


def clicar_botao_txt(texto_link):
    botao = navegador.find_element(By.XPATH, f'//button[text()="{texto_link}"]')
    botao.click()


def puxar_tabela():
    table = navegador.find_element(By.CLASS_NAME, 'MuiTable-root')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    
    data_limite = datetime.strptime('22/04/2024', '%d/%m/%Y')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if not cells:  # Caso seja uma linha de cabeçalho
            cells = row.find_elements(By.TAG_NAME, 'th')
        if cells:  # Apenas continue se houver células na linha
            # Supondo que o ID está na primeira célula de cada linha
            cell_id = cells[8].get_attribute('id')
            cell_data = cells[6].get_attribute('Publicação')
            cell_data_text = cells[6].text         
            try:
                cell_data_convert = datetime.strptime(cell_data_text, '%d/%m/%Y')
                if cell_data_convert >= data_limite:
                    if cell_id:
                        id_atividade.append(cell_id)
            except ValueError:                
                pass
            # Fazer um if pela data get_attribute('Publicação')               
    #print(id_atividade)


def puxar_tabela_alunos():
    table = navegador.find_element(By.CLASS_NAME, 'MuiTable-root')
    rows = table.find_elements(By.TAG_NAME, 'tr')    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if not cells:  # Caso seja uma linha de cabeçalho
            cells = row.find_elements(By.TAG_NAME, 'th')        
        for cell in cells:
            print(cell.text, end=' | ')
        print()

# Exemplo de uso da função
# Suponha que 'navegador' já esteja inicializado e apontando para a página correta



# Inicia o navegador
navegador = opcoesSelenium.Chrome()
id_atividade = []
# Login
navegador.get('https://cmsp-tms.ip.tv')
time.sleep(5)
navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
time.sleep(2)
navegador.find_element(By.ID, 'document').send_keys('466709742')
time.sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[3]/form/div/div[1]/div/div/div').click()
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id=":r4:"]/li[1]').click()
time.sleep(2)
navegador.find_element(By.ID, 'password').send_keys('@Antero89')
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/form/div/div[5]/button').send_keys(Keys.ENTER)
time.sleep(2)


#Home

# Identificador do prof
prof = navegador.find_element(By.CLASS_NAME, 'MuiTypography-h5 ').text.split()[2]
print(prof)
time.sleep(1)

#Atividades
navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/button/div').click()
time.sleep(2)
#Atividades/Atividades
navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/div/div/div/ul/li[2]/a/div').click()
time.sleep(2)
checkbox = navegador.find_element(By.ID, "filter-by-publication-target")
if not checkbox.is_selected():
    checkbox.click()
else:
    print("Checkbox já está marcado")
time.sleep(2)
#Clicar para selecionar turma
navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/button').click()
time.sleep(2)
# Encontra o primeiro input do tipo rádio na tabela e clica nele
clicar_radio1()
time.sleep(2)
clicar_botao_txt('Adicionar')
time.sleep(2)
# Muda o filtro de Título para Publicador
navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[1]/div[1]/div/div/div').click()
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id=":r10:"]/li[1]').click()
time.sleep(2)
# Insere o professor e busca
navegador.find_element(By.ID, ':r11:').send_keys(prof)
time.sleep(2)
clicar_botao_txt('Procurar')
time.sleep(2)
# Muda filtro para visualização em 50 linhas
navegador.find_element(By.XPATH, '//*[@id=":r12:"]').click()
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id=":r14:"]/li[2]').click()
time.sleep(2)
# Acessar página da atividade 1
#
#time.sleep(2)
puxar_tabela()
time.sleep(2)
for id in id_atividade:
    navegador.find_element(By.XPATH, f'//*[@id="{id}"]/div/button').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[1]/div[2]/span').click()
    time.sleep(2)
    puxar_tabela_alunos()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/nav/ol/li[3]').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[2]').click()
    time.sleep(2)











