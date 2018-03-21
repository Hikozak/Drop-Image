from flask import Flask, request, send_from_directory, render_template
app = Flask(__name__, static_folder='', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def home():
    return render_template('about.html')

@app.route('/upload.php')
def upload():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.run(debug=True)