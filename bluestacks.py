# Adicionar ao final do arquivo do ambiente (Activate.ps1) o path do adb no sdk android
#$env:PATH += ";C:\Users\anddr\AppData\Local\Android\Sdk\platform-tools" 

import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho absoluto do adb
adb_path = r'C:\\Users\\anddr\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe'  # Altere para o caminho correto do adb

# Conectar ao BlueStacks
subprocess.run([adb_path, 'connect', '127.0.0.1:5555'])

# Verificar dispositivos conectados
result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)
print(result.stdout)

# Listar pacotes instalados
result = subprocess.run([adb_path, 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
print(result.stdout)

# Desconectar do BlueStacks
#subprocess.run([adb_path, 'disconnect', '127.0.0.1:5555'])

# Configurar o WebDriver
driver = webdriver.Chrome()

# Conectar ao BlueStacks
driver.get('http://127.0.0.1:5555')

# Exemplos de comandos Selenium
# Aguardar a presença de um elemento e interagir com ele
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))
element.click()

# Fechar o WebDriver
driver.quit()



