from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    images = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for('index'))
    return redirect(request.url)

@app.route('/delete/<filename>')
def delete_file(filename):
    os.remove(os.path.join(UPLOAD_FOLDER, filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
