### Configuração de URL

#### Arquivo core/urls.py

Criação da url  **evento**.

``` bash
from django.urls import path, include

urlpatterns = [
    path('evento/', include('evento.urls')),
]
```
- **urlpatterns** lista onde as urls são mencionadas.

- **evento.urls** faz referência ao arquivo **urls** na pasta **evento**, onde as suburls são listadas. Criar arquivo caso não exista.

*O processo se repete para cada url criada na pasta core.*

### Configuração Templates

Arquivo **settings** pasta **core**

```bash
'DIRS': [BASE_DIR / 'templates'],
```

Pasta **templates** com arquivos específicos na raíz do projeto 

```bash
'APP_DIRS': True,
```

Pasta **templates** nas pastas dos apps.

### Configuração Static

Arquivo **settings** pasta **core**

```bash
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- Arquivos Estáticos adicionados por devs
- Arquivos de Mídia adicionados por usuários