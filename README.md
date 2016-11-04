#Eventex

Sistema de eventos para o curso Welcome to the Django

[![Build Status](https://travis-ci.org/marcosvpj/Eventex.svg?branch=master)](https://travis-ci.org/marcosvpj/Eventex)
[![Code Health](https://landscape.io/github/marcosvpj/Eventex/master/landscape.svg?style=flat)](https://landscape.io/github/marcosvpj/Eventex/master)

##Como desenvolver?

1. Clonar o repo
2. Criar virtualenv com Python 3.5
3. Ativar o virtualenv
4. Instalar dependências
5. Configurar a instância com o .env
6. Executar os testes

```console
git clone https://github.com/marcosvpj/Eventex.git wttd
cd wttd
python -m venv .wttd
# Windows
.wttd\Scripts\activate.bat
# *nix
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```
