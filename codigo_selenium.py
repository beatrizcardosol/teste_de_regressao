from selenium import webdriver # Importa o Selenium WebDriver para controle do navegador
from selenium.webdriver.chrome.service import Service # Importa o serviço do ChromeDriver
from selenium.webdriver.chrome.options import Options  # Importa as opções do Chrome
from webdriver_manager.chrome import ChromeDriverManager # Gerenciador automático do ChromeDriver
import time  # Importa o módulo time para pausas


#Configurações do Chrome pro linux rodar sem erro
options = Options()
options.binary_location = "/usr/bin/google-chrome"  # Caminho pro Chrome
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  #Inicia o ChromeDriver com as opções configuradas

driver.get("file:///home/bia/Documentos/teste_de_regressao/index.html") #Abre a página HTML local

#colocar o navegador em tela cheia
driver.maximize_window()

try:
    botao_contato = driver.find_element("class name", "contact-button") #o botão de contato antes de chamava "contact-btn"

    botao_contato.click()

except Exception as e:
    print(f"Ocorreu um erro: {e}")



time.sleep(50)
driver.quit()


#alterando o contact-btn para contact-button no html
#alterando o codigo_selenium.py para refletir essa mudança

