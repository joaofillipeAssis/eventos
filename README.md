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

O gerenciador do Django cria o projeto. A pasta **core** sera criada e o arquivo **manage.py**.

``` bash
django-admin startproject core .

```
**.** indica que será criado na mesma pasta





