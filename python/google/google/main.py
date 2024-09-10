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
    driver.get("https://www.google.com")

    # Verificar o título da página
    assert "Google" in driver.title

    # Encontrar um elemento e interagir com ele
    elemento = driver.find_element(By.NAME, "q")  # Substitua pelo seletor apropriado
    elemento.clear()
    elemento.send_keys("selenium")
    elemento.send_keys(Keys.RETURN)

    # Esperar para ver o resultado
    time.sleep(10)

    elemento2 = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
    print(elemento2.text)
    elemento2.click()
    time.sleep(10)

finally:
    # Fechar o navegador
    driver.quit()