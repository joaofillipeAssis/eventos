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