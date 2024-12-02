from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = 'acc_5427df4384ca6b3'
API_SECRET = '76d6252b1a203185495e9bd09b7c6851'
IMAGGA_URL = 'https://api.imagga.com/v2/tags'

@app.route('/')
def index():
    # Lista de imágenes, deben estar en la carpeta static
    images = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg']
    return render_template('index.html', images=images)

@app.route('/analyze', methods=['POST'])
def analyze():
    image_urls = request.form.getlist('image_urls')

    results = []
    for url in image_urls:
        # Construir la ruta completa del archivo en la carpeta static
        image_path = os.path.join('static', url)
        
        try:
            with open(image_path, 'rb') as img_file:
                response = requests.post(
                    IMAGGA_URL,
                    auth=(API_KEY, API_SECRET),
                    files={'image': img_file})
            
            if response.status_code == 200:
                data = response.json()
                # Tomar los dos resultados más confiables
                tags = data['result']['tags'][:2]  # Tomar las dos primeras etiquetas más confiables
                results.append({'url': url, 'tags': tags})
            else:
                results.append({'url': url, 'error': 'No se pudo procesar la imagen'})
        except FileNotFoundError:
            results.append({'url': url, 'error': f'Imagen no encontrada: {url}'})

    return render_template('index.html', images=image_urls, results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
