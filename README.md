### VENV - Ambiente Virtual do Python

Ajuda a manter as dependências do projeto separadas das dependências globais do sistema.

###### Criar

``` bash
python -m venv venv
```

###### Ativar


``` bash
venv\Scripts\Activate
```

(venv) indica que está ativado:
```bash
(venv) PS C:\
```

### INSTALAÇÃO DE BIBLIOTECAS

###### DJANGO


``` bash
pip install django  
```

###### PILLOW
Usado para imagens no projeto.

``` bash
pip install pillow
```

### CRIANDO PROJETO

O gerenciador do Django cria o projeto. A pasta **core** é criada e o arquivo **manage.py**.

``` bash
django-admin startproject core .
```
**.** indica que será criado na mesma pasta

### RODANDO PROJETO

``` bash
python manage.py runserver
```

**Ctrl + C** pausa o servidor.

### CRIANDO apps

``` bash
python manage.py startapp evento
```
- cria app com nome **evento**.
-  **'evento'** é adicionado no bloco **INSTALLED APPS** do arquivo **settings** na pasta **core** para ser reconhecido coomo app.

### MIGRAÇÕES

``` bash
python manage.py makemigrations
```
- Informa ao Django como as migrações devem ser executadas conforme arquivo **models.py** 

- Arquivo **0001_initial.py** criado na pasta **migrations**.

##### Salvar no Banco de Dados

``` bash
python manage.py migrate
```

