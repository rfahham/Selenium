# sudo !pip install selenium
# sudo pip install pandas
# sudo pip install webdriver-manager

import pandas as pd
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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

    time.sleep(5)

finally:
    # Fechar o navegador
    driver.quit()