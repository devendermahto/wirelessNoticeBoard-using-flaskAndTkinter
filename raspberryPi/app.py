from flask import *
import cv2

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/image', methods=['POST'])
def success_image():
    if request.method == 'POST':
        f = request.files['file']
        f.save("received.png")
        return render_template("success.html", name=f.filename)


@app.route('/text', methods=['POST'])
def success_text():
    if request.method == 'POST':
        t = request.form.get('text')
        back = cv2.imread("back.png")
        cv2.putText(back, text=t, org=(int(back.shape[1]/4), int(back.shape[0]/2)), fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,color=(0,0,0),thickness=2)
        cv2.imwrite("received.png", back)
        return render_template("success.html", name="text")


if __name__ == '__main__':
    app.run(host = "192.168.1.100", debug=True, port=5000)