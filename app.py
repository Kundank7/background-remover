from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded!', 400

    file = request.files['image']
    img = Image.open(file.stream)
    output = remove(img)

    img_byte_arr = io.BytesIO()
    output.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/png')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render-assigned port
    app.run(host='0.0.0.0', port=port)
