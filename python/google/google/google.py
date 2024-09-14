from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--headless") # Executa o navegador em modo headless (sem interface gráfica)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Caminho para o ChromeDriver
service = Service('caminho/para/chromedriver') # Atualize com o caminho real do ChromeDriver

# Inicializa o driver do Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abre a página do Google
    driver.get("https://www.google.com")

    # Encontra o campo de pesquisa
    search_box = driver.find_element(By.NAME, "q")

    # Envia uma consulta de pesquisa
    search_box.send_keys("Automação de Testes com Selenium")
    search_box.send_keys(Keys.RETURN)

    # Espera um pouco para os resultados carregarem
    driver.implicitly_wait(10) # Espera até 10 segundos

    # Verifica se os resultados estão presentes
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, "Nenhum resultado encontrado."

    # Exibe o título da primeira página de resultados
    print("Título da primeira página de resultados:")
    print(results[0].text)

finally:
# Fecha o navegador
driver.quit()


# tente abrir a página do Google..
# mas acho que poderia ter usado em um outro contexto.. por exemplo, 
# nesse caso dessa página simples do Google, ter encontrado o campo de pesquisa, 
# ter feito a pesquisa, e aí fazer um try com o resultado esperado.. 
# talvez fosse melhor exemplificado..