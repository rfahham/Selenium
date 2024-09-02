# Installing Webdrivers
 
Para usar o Firefox precisa instalar o GeckoDriver

Releases: https://github.com/mozilla/geckodriver/tags

O Selenium requer um driver para fazer interface com o navegador escolhido. O Firefox, por exemplo, requer o geckodriver, que precisa ser instalado antes que os exemplos abaixo possam ser executados. 
Certifique-se de que ele esteja no seu PATH, por exemplo, coloque-o em /usr/bin ou /usr/local/bin .

```bash 

wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz

tar -xvzf geckodriver*

chmod +x geckodriver
```

Verificar local de instalação do windows

```bash
which python3

/usr/bin/python3
```

Copiar o `geckodriver` para a mesma pasta do python

```bash
sudo cp geckodriver /usr/bin/

/usr/local/bin/
```


ERROR

DRIVER

Para ver quais diretórios já estão em PATH, abra um Terminal e execute:

```bash
echo $PATH
```

Se o local do seu driver ainda não estiver em um diretório listado, você pode adicionar um novo diretório ao PATH:

```bash
echo 'export PATH=$PATH:/usr/bin/geckodriver' >> ~/.zshenv

source ~/.zshenv
```
