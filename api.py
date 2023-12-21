import random
import string
from flask import Flask, jsonify, request, url_for
from PIL import Image
import os

app = Flask(__name__)

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# info API
@app.route('/info', methods=['GET'])
def info():
    data = {
        "name": "Convertal API",
        "author": "Fabricio Amorim",
        "version": "1.0.0",
        "description": "API Beta for Convertal, a free online image converter.",
        "formats": [
            "png",
            "jpg",
            "gif",
            "bmp",
            "tiff",
            "ico",
            "webp"
        ]
    }
    return jsonify(data)

# Route to convert images to PNG 
@app.route('/convert/png', methods=['POST'])
def convert_to_png():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.png'
        new_filepath = os.path.join('static', 'png', new_filename)

        # Create the static/png folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('png', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to PNG successfully', 'urls': urls})

# Route to convert images to JPG
@app.route('/convert/jpg', methods=['POST'])
def convert_to_jpg():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.jpg'
        new_filepath = os.path.join('static', 'jpg', new_filename)

        # Create the static/jpg folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('jpg', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to JPG successfully', 'urls': urls})

# Route to convert images to GIF
@app.route('/convert/gif', methods=['POST'])
def convert_to_gif():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.gif'
        new_filepath = os.path.join('static', 'gif', new_filename)

        # Create the static/gif folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('gif', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to GIF successfully', 'urls': urls})

# Route to convert images to BMP
@app.route('/convert/bmp', methods=['POST'])
def convert_to_bmp():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.bmp'
        new_filepath = os.path.join('static', 'bmp', new_filename)

        # Create the static/bmp folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('bmp', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to BMP successfully', 'urls': urls})

# Route to convert images to TIFF
@app.route('/convert/tiff', methods=['POST'])
def convert_to_tiff():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.tiff'
        new_filepath = os.path.join('static', 'tiff', new_filename)

        # Create the static/tiff folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('tiff', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to TIFF successfully', 'urls': urls})

# Route to convert images to ICO
@app.route('/convert/ico', methods=['POST'])
def convert_to_ico():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.ico'
        new_filepath = os.path.join('static', 'ico', new_filename)

        # Create the static/ico folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('ico', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to ICO successfully', 'urls': urls})

# Route to convert images to WEBP
@app.route('/convert/webp', methods=['POST'])
def convert_to_webp():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.webp'
        new_filepath = os.path.join('static', 'webp', new_filename)

        # Create the static/webp folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('webp', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to WEBP successfully', 'urls': urls})

# Route to convert images to PDF
@app.route('/convert/pdf', methods=['POST'])
def convert_to_pdf():
    files = request.files.getlist('file')
    urls = []
    for file in files:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        random_string = generate_random_string()
        new_filename = 'Convertal_' + random_string + '_' + os.path.splitext(file.filename)[0] + '.pdf'
        new_filepath = os.path.join('static', 'pdf', new_filename)

        # Create the static/pdf folder if it doesn't exist
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

        rgb_im.save(new_filepath)
        # Replace backslashes with slashes in the file path
        filename = os.path.join('pdf', new_filename).replace('\\', '/')
        image_url = url_for('static', filename=filename)
        urls.append(image_url)

    return jsonify({'message': 'Images converted to PDF successfully', 'urls': urls})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)