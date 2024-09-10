from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

try:
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.alura.com.br")

    elemento = driver.find_element(By.XPATH, "/html/body/main/section[1]/div[2]/div[2]/nav/div/div[1]/div")
    elemento = driver.find_element(By.XPATH, "/html/body/main/section[1]/div[2]/div[2]/nav/div/div[1]/div")
    print(elemento.text)
    
    time.sleep(5)

    elemento.click()

    time.sleep(5)

finally:
    # Fechar o navegador
    driver.quit()