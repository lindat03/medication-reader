from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

cors = CORS(app, resources={r"/upload": {"origins": ["http://localhost:3000"]}})

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        print("here!")
        image = request.files['image']
        img = Image.open(image)
        ocr_text = pytesseract.image_to_string(img)
        print(ocr_text)
        return jsonify({'text': ocr_text})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
