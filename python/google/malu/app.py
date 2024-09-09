from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://ri.magazineluiza.com.br')

# Encontre o elemento que deseja clicar
elemento = driver.find_element(By.XPATH, "//*[contains(text(), 'Informações Financeiras')]")
elemento.click
time.sleep(5)

elemento2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Planilha de Resultado')]")
elemento2.click
time.sleep(5)

driver.get('https://ri.magazineluiza.com.br/ShowCanal/Planilha-de-Resultado?=CHN0/Z4bUSgrS8IkQeL+Wg==&linguagem=pt')

elemento3 = driver.find_element(By.XPATH, "//*[contains(text(), 'Planilha de Resultados Trimestrais')]")
elemento3.click()
time.sleep(5)

# O arquivo é enviado para a pasta Downloads

# Feche o navegador
driver.quit()