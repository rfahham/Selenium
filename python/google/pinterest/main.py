from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar o WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Abrir a página inicial
    driver.get("https://br.pinterest.com/ideas/")
    time.sleep(10)

    # Verificar o título da página
    assert "Explore the best of Pinterest" in driver.title

    # Encontrar um elemento e interagir com ele
    elemento = driver.find_element(By.XPATH, "//*[@id='mweb-unauth-container']/div/div/div/div/section[2]/div[2]/div[1]/div/a/div/div[2]")
    elemento.click()

    # Esperar para ver o resultado
    time.sleep(10)


finally:
    # Fechar o navegador
    driver.quit()