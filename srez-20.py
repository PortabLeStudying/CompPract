from flask import Flask, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/image')
def get_image():
    img = Image.new('RGB', (300, 100), color='white')
    
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')