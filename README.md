#Eventex

Sistema de eventos para o curso Welcome to the Django

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
source .wttd\Scripts\activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
