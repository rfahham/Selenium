# Selenium

https://www.selenium.dev/

Selenium automatiza navegadores. É isso!
O que você faz com esse poder depende inteiramente de você.

## Use Selenium WebDriver se você:

- Precisa suportar vários navegadores, incluindo Chrome, Firefox, Safari, Internet Explorer e Microsoft Edge, Opera.
- Está trabalhando em um ambiente de desenvolvimento que usa várias linguagens de programação.
- Precisa executar testes em ambientes diferentes, como dispositivos móveis e navegadores diferentes.
- Tem mais experiência em automação de testes e deseja mais flexibilidade e controle sobre sua automação de testes.

## Requisitos:

- python 3.10
- Visual Studio Code
- Extensão do Jupiter Notebook
- Selenium
- webdriver-manager
- Google-Chrome

## Preparando ambiente virtual

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Instalando o Selenium

```bash
pip install selenium
```

## Instalando o webdriver-manager 

```bash
pip install webdriver-manager 
```

## Instalando o Google-Chrome

Baixe o pacote `.deb` do Google Chrome:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Instale o pacote `.deb`:

```bash
sudo apt install ./google-chrome-stable_current_amd64.deb
```

Verifique a instalação:

Após a instalação, você pode verificar se o Google Chrome está disponível executando:

```bash
google-chrome --version

Google Chrome 126.0.6478.126
```

## Executando

```bash
python main.py
```