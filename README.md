# PCA Coin label

* [Preparando o ambiente de trabalho](#preparando-o-ambiente-de-trabalho)
    + [Ubuntu 19.10+ / Debian (sid)](#ubuntu-1910----debian--sid-)
    + [Windows e outras distribuições de Linux](#windows-e-outras-distribui--es-de-linux)
    + [MacOs](#macos)


## Preparando o ambiente de trabalho
### Ubuntu 19.10+ / Debian (sid)
Nas distribuições mais novas do Ubuntu e no Debian (sid),
o programa pode ser facilmente instalado com o comando abaixo:
```
sudo apt-get install labelme
```
### Windows e outras distribuições de Linux
Para instalar o programa nesses sistemas é necessário instalar o **Anaconda**, o Anaconda é uma distribuição de Python que facilita a instalação de programas e bibliotecas.

[Tutorial de Instalação no Windows e Ubuntu](https://minerandodados.com.br/instalar-python-anaconda/).

Após instalar o Anaconda, basta executar o comando abaixo:
```
conda install labelme -c conda-forge
```
### MacOs
```
brew install pyqt  # maybe pyqt5
pip install labelme
```
