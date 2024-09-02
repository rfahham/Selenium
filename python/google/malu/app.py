from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://ri.magazineluiza.com.br/')

navegador.find_element('xpath', '//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a').click()

# navegador.find_element_by_xpath('//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a').click()

