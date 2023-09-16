from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
from flask_cors import CORS

import openai
import os

API_KEY = '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'

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
        response_text = generate_response(ocr_text, 'text_files/examples.txt', 'text_files/text_guidelines.txt')
        print(response_text)
        return jsonify({'text': response_text})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

def generate_response(test_message, examples, guidelines):
    openai.api_key = API_KEY

    model = 'text-davinci-003'
    print("TESTTTTT")
    print(os.getcwd())
    test_message_output = test_message
    with open(examples) as f:
        examples_output = f.read()
    f.close()
    with open(guidelines) as f:
        guidelines_output = f.read()
    f.close()
     
    print(test_message_output)
    
    response_prompt = '''
        An image of a medical pill bottle and prescription was fed through an OCR package and produces the text on the label. 
        Based on these snippets of text, output a simple, straightforward description of the medicine and it's uses. 
        DO NOT include the prescription number, quantity of pills inside the bottle, etc. 
        This is an example of what the output should look like:
        
    ''' + examples_output + "\n\nUse these guidelines to create the text response: \n" + guidelines_output + "\n\nFind a response for this conversation: \n" + test_message_output
    
    response = openai.Completion.create(
        prompt=response_prompt,
        model=model,
        max_tokens=2000,
        temperature=0.95,
        n=1,
    )

    result_array = []
    for result in response.choices:
        result_array.append(result.text)

    formatted_str = ""
    for r in result_array:
        formatted_str += r
    print(formatted_str)
    return formatted_str


if __name__ == '__main__':
    app.run(debug=True)
