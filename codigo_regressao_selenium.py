from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do Chrome para rodar sem erro no Linux
options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("file:///home/bia/Documentos/teste_de_regressao/index.html")
driver.maximize_window()

# TESTE DE REGRESSÃO
print("Iniciando teste de regressão do botão de contato...\n")

try:
    botao_contato = driver.find_element("class name", "contact-btn")
    botao_contato.click()
    print("TESTE PASSOU!")

except Exception as e:
    print("TESTE FALHOU")
    print("Detalhes do erro:", e)


time.sleep(10)
driver.quit()
