import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

try:
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.pinterest.com/ideas/")

    # Esperar para ver o resultado
    time.sleep(10)

finally:
    # Fechar o navegador
    driver.quit()