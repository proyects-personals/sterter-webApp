# WebApp Dockerizada que Consume SaaS (Imagga)

Este proyecto es una WebApp Dockerizada que consume el servicio de reconocimiento de imágenes de Imagga. El objetivo es analizar imágenes a través de la API de Imagga y mostrar los resultados de las etiquetas con la mayor confianza.

## Requisitos

- Docker
- Python 3.x
- Flask (Framework web)
- Imagga API Key y API Secret (obtenidos al registrarse en Imagga)

## Estructura del Proyecto

```bash
webapp-dockerizada/
│
├── app/
│   ├── templates/
│   │   └── index.html            # Plantilla HTML para mostrar las imágenes y resultados
│   ├── static/
│   │   └── images/               # Carpeta con imágenes (o URLs de imágenes públicas)
│   ├── app.py                    # Archivo principal con la lógica de la WebApp
│   ├── Dockerfile                # Dockerfile para dockerizar la aplicación
│   └── requirements.txt          # Dependencias de la aplicación
│
├── README.md                    
```

# Instalación

## 1. Clonar el repositorio
Clona el repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd webapp-dockerizada
```

# 2. Configurar las claves de Imagga
Para consumir la API de Imagga, necesitarás una clave de API y un secreto de API. Puedes obtenerlas registrándote en Imagga.

Copia tu API_KEY y API_SECRET después de registrarte.
Una vez que tengas tus credenciales, abre el archivo app.py y reemplaza <API_KEY> y <API_SECRET> por tus claves de Imagga en la siguiente parte del código:

```bash
IMAGGA_API_KEY = "<API_KEY>"
IMAGGA_API_SECRET = "<API_SECRET>"
```

# 3. Instalar dependencias
Si prefieres ejecutar el proyecto localmente fuera de Docker, instala las dependencias de Python necesarias:

```bash
pip install -r requirements.txt
```

# 4. Construir la imagen Docker
Si deseas ejecutar el proyecto dentro de un contenedor Docker, primero necesitas construir la imagen de Docker. Ejecuta el siguiente comando dentro del directorio raíz del proyecto:

```bash
docker build -t starter-webapp  .
```

Este comando construirá la imagen Docker basada en el Dockerfile.

# 5. Ejecutar la aplicación con Docker
Una vez que la imagen de Docker esté construida, puedes ejecutar la aplicación con el siguiente comando:

```bash
docker run -p 5000:5000 starter-webapp 
```
Esto iniciará el contenedor y expondrá la aplicación en el puerto 5000. La WebApp será accesible en tu navegador.