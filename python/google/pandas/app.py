import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    # A clsse Service é usada para iniciar uma instância do Chrome WEbdriver
    service = Service(ChromeDriverManager().install())

    # webdriver.ChromeOptions é usado para definir a prefer~encia para o browser do chrome
    options = webdriver.ChromeOptions()

    # Inicia-se a instância do Chrome webdriver com as definidas "options" e "service"
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://books.toscrape.com/"

    driver.get(url)

    sleep(5)

    driver.find_elements(By.TAG_NAME, 'a')[54].text

    

finally:
    # Fechar o navegador
    driver.quit()



