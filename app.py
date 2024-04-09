from flask import Flask, render_template, request
from flask_cors import CORS
from PIL import Image
import io
import os
app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Ayesha' and password == 'password':
            return "success"
        else:
            return "failure"


@app.route('/fileupload', methods=['POST'])
def file_upload():
    files = request.files.getlist("file")
    for file in files:
        if file.content_type == 'text/plain':
            return file.read().decode()
        # Check if the uploaded file is an image
        elif file.content_type.startswith('image/'):
            # Read the image file
            image_bytes = file.read()
            # Create an in-memory file-like object
            image_stream = io.BytesIO(image_bytes)
            # Open the image using PIL (Python Imaging Library)
            image = Image.open(image_stream)
            # Display the image (you may need to render it in a template or use another method depending on your application)
            image.show()
            try:
                os.mkdir('test/')
            except:
                pass
            image.save('test/'+file.filename)
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=8080)
