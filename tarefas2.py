from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
from dotenv import load_dotenv
import os



#22/04/2024
data_init = '22/04/2024'
EM2C = 'tbody tr:nth-child(1) input[type="radio"]'
EM2B = 'tbody tr:nth-child(2) input[type="radio"]'
EM2A = 'tbody tr:nth-child(3) input[type="radio"]'
EM1B = 'tbody tr:nth-child(4) input[type="radio"]'
EM1C = 'tbody tr:nth-child(5) input[type="radio"]'
sala = '1C'
class TarefaScraper:
    def __init__(self):
        self.navegador = opcoesSelenium.Chrome()
        self.id_atividade = []
        self.dados_alunos = []

    def clicar_radio(self):
        radio1 = self.navegador.find_element(By.CSS_SELECTOR, EM1C)
        radio1.click()

    def clicar_botao_txt(self, texto_link):
        botao = self.navegador.find_element(By.XPATH, f'//button[text()="{texto_link}"]')
        botao.click()

    def puxar_tabela(self):
        table = self.navegador.find_element(By.CLASS_NAME, 'MuiTable-root')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        data_limite = datetime.strptime(data_init, '%d/%m/%Y')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if not cells:
                cells = row.find_elements(By.TAG_NAME, 'th')
            if cells and cells[0].text != 'Id':
                cell_id = cells[8].get_attribute('id')
                cell_data_text = cells[6].text         
                try:
                    cell_data_convert = datetime.strptime(cell_data_text, '%d/%m/%Y')
                    if cell_data_convert >= data_limite:
                        if cell_id:
                            self.id_atividade.append(cell_id)
                except ValueError:
                    pass

    def puxar_tabela_alunos(self):          
        table = self.navegador.find_element(By.CLASS_NAME, 'MuiTable-root')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if not cells:
                cells = row.find_elements(By.TAG_NAME, 'th')
            if cells and cells[0].text != 'Id':
                self.dados_alunos.append([cell.text for cell in cells])

    def salvar_dados_excel(self, caminho_arquivo):
        df = pd.DataFrame(self.dados_alunos, columns=['Id', 'Aluno', 'Turma', 'Entregue em', 'Duração', 'Status', 'Nota', 'Observação'])
        df.to_excel(caminho_arquivo, index=False, sheet_name='Dados Alunos')

        # Consolidar dados por aluno
        df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
        media_notas = df.groupby('Aluno')['Nota'].mean().reset_index()
        media_notas.columns = ['Aluno', 'Média Nota']
        
        with pd.ExcelWriter(caminho_arquivo, engine='openpyxl', mode='a') as writer:
            media_notas.to_excel(writer, index=False, sheet_name='Média Notas')

    def executar(self):
        # Carregar variáveis de ambiente do arquivo .env
        load_dotenv()

        # Obter os valores das variáveis de ambiente
        password = os.getenv('PASSWORD')
        documento = os.getenv('DOCUMENTO')        
        self.navegador.get('https://cmsp-tms.ip.tv')
        time.sleep(5)
        self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
        time.sleep(2)
        self.navegador.find_element(By.ID, 'document').send_keys(documento)
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[3]/form/div/div[1]/div/div/div').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id=":r4:"]/li[1]').click()
        time.sleep(2)
        self.navegador.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/form/div/div[5]/button').send_keys(Keys.ENTER)
        time.sleep(2)

        #Home
        prof = self.navegador.find_element(By.CLASS_NAME, 'MuiTypography-h5').text.split()[2]
        time.sleep(1)

        #Atividades
        self.navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/button/div').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id="1"]/ul/li/div/div/div/ul/li[2]/a/div').click()
        time.sleep(2)
        checkbox = self.navegador.find_element(By.ID, "filter-by-publication-target")
        if not checkbox.is_selected():
            checkbox.click()
        else:
            print("Checkbox já está marcado")
        time.sleep(2)

        self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/button').click()
        time.sleep(2)
        self.clicar_radio()
        time.sleep(2)
        self.clicar_botao_txt('Adicionar')
        time.sleep(2)

        self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[3]/div/form/div/div[1]/div[1]/div/div/div').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id=":r10:"]/li[1]').click()
        time.sleep(2)
        self.navegador.find_element(By.ID, ':r11:').send_keys(prof)
        time.sleep(2)
        self.clicar_botao_txt('Procurar')
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id=":r12:"]').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id=":r14:"]/li[2]').click()
        time.sleep(2)

        self.puxar_tabela()
        time.sleep(2)
        for id in self.id_atividade:
            self.navegador.find_element(By.XPATH, f'//*[@id="{id}"]/div/button').click()
            time.sleep(2)
            self.navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[1]/div[2]/span').click()
            time.sleep(2)
            self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div').click()   
            time.sleep(2)
            self.navegador.find_element(By.XPATH,'/html/body/div[5]/div[3]/ul/li[2]').click()   
            time.sleep(2)
            self.puxar_tabela_alunos()
            time.sleep(2)
            self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/nav/ol/li[3]').click()
            time.sleep(2)
            self.navegador.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]').click()
            time.sleep(2)
            self.navegador.find_element(By.XPATH, '/html/body/div[5]/div[3]/ul/li[2]').click()
            time.sleep(2)

        self.salvar_dados_excel('dados_alunos_consolidado_'+sala+'.xlsx')
        print("Dados consolidados")

# Execução
scraper = TarefaScraper()
scraper.executar()




