from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

## LOGIN
## Usando Live Server
sleep(10)
navegador.get('http://localhost:5500/python/google/login/login.html')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[1]').send_keys('rfahham@hotmail.com')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[2]').send_keys('1q2w3e4r')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/a/button').click()
sleep(5)

# CADASTRO
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[1]').send_keys('Ricardo Fahham')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[2]').send_keys('Petrópolis')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[3]').send_keys('Rio de Janeiro')
sleep(1)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[4]').send_keys('Brasil')
sleep(1)

# DOWNLOAD
navegador.find_element('xpath', '//*[@id="download"]').click()

sleep(10)