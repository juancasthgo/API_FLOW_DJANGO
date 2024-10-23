# Implementación de Pasarela de Pagos para Comercio Electrónico con API Flow en Django

## Introducción

Implementacion de una pasarela de pagos utilizando la API de Flow en un proyecto Django. Los requerimientos previos son conocimientos básicos de Django y Python.
Flow.cl es una pasarela de pagos para comercio electrónico. Este cliente le permite integrar su ecommerce para recibir pagos online.

## Requerimientos Previos

- Python 3.x
- Django 3.x
- requests
- python-decouple

## Introducción

La documentación completa del API REST de Flow la encuentrá aquí:https://www.flow.cl/docs/api.html

## Instalación de Dependencias

Instala las dependencias necesarias:

```bash
pip install requests 
pip install python-decouple
```

## Configura tu archivo ENV

Cree un archivo `.env` en la raíz de tu proyecto, luego ocultar desde .gitignore.

```env
ENV=Valor # Agrega un valor a tu ENV
FLOW_API_KEY='FLOW_API_KEY'  # Sustituye por tu API key
FLOW_SECRET_KEY='SECRET_API_KEY'  # Sustituye por tu Secret key
```

## Configuración de settings.py

Configure las claves de la API de Flow en tu archivo `settings.py` utilizando `python-decouple` para manejar las variables de entorno de manera segura.

```python
from decouple import config

ENV = config('ENV', default='Valor')
FLOW_API_KEY = config('FLOW_API_KEY')
FLOW_SECRET_KEY = config('FLOW_SECRET_KEY')
```


