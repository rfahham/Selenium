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
    elem = driver.find_element(By.NAME, "q")  # Substitua pelo seletor apropriado
    elem.clear()
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)

    # Esperar para ver o resultado
    time.sleep(5)

    # Verificar se os resultados são relevantes
    assert "No results found." not in driver.page_source
finally:
    # Fechar o navegador
    driver.quit()
