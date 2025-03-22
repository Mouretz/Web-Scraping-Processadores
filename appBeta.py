from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math
import re
import pandas as pd


# Iniciando sessao do Navegador -  Selenium WebDriver(JS BOT)
session_options = Options() 

# Passando argumentos de inicialicaczao
arguments = [
    '--lang=pt-BR', '--disable-notifications', "--headless"
    ]

for arg in arguments:
    session_options.add_argument(arg)

# Carregar o Navegador e opcoes
navigator = webdriver.Chrome( options=session_options)

# Correcao
errors = [NoSuchElementException, ElementNotInteractableException,ElementNotVisibleException]
wait = WebDriverWait(navigator, timeout=2, poll_frequency=2, ignored_exceptions=errors)

# URL
url = "https://www.kabum.com.br/hardware/processadores/processador-intel"
navigator.get(url)


qtd_products = wait.until(expected_conditions.element_to_be_clickable((By.ID, "listingCount")))
qtd_products = qtd_products.text
numbers = re.findall(r'\d',qtd_products)
qtd = int(''.join(numbers))
last_page = math.ceil(qtd/20)


dict_produtos = {"Descricao":[], "Preco":[]}


for i in range(1,last_page+1):
    url_pag = f"https://www.kabum.com.br/hardware/processadores/processador-intel?page_number={i}"
    navigator.get(url_pag)
   
    products = wait.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,"productCard")))
    
    

    for product in products:
        navigator.execute_script("arguments[0].scrollIntoView();", product) 
        product_name = product.find_element(By.CLASS_NAME, "nameCard").text
        product_price = product.find_element(By.CLASS_NAME, "priceCard").text
        
        dict_produtos["Descricao"].append(product_name)
        dict_produtos["Preco"].append(product_price)

df = pd.DataFrame(dict_produtos)
df.to_csv("Processadores_Intel.csv", encoding="utf-8", sep=";")

print("Fim! Arquivo criado com sucesso.")
        