# Instalação

## Verificar a versção do Chrome

Digitar: chrome://version/ na barra de endereços do seu navegador.

126.0.6478.127 (Versão oficial) 64 bits (cohort: Stable) 

chromedriver-linux64

```bash
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip

chmod +x chromedriver
```

Verificar local de instalação do windows

```bash
which python3

/usr/bin/python3
```

Copiar o `geckodriver` para a mesma pasta do python

```bash
sudo cp chromedriver /usr/bin/

/usr/local/bin/
```

Se o local do seu driver ainda não estiver em um diretório listado, você pode adicionar um novo diretório ao PATH:

```bash
echo 'export PATH=$PATH:/usr/bin/chromedriver' >> ~/.zshenv

source ~/.zshenv
```


Você pode testar se ele foi adicionado corretamente verificando a versão do driver:

```bash
chromedriver --version
```