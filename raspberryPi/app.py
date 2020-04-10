from flask import *

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/image', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save("received.png")
        return render_template("success.html", name=f.filename)


if __name__ == '__main__':
    app.run(host = "192.168.1.100", debug=True, port=5000)