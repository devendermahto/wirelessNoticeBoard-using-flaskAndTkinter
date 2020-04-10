from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import cv2


app = Flask(__name__)


@app.route('/maskImage', methods=['POST'])
def mask_image():
    file = request.files['image'].read()
    print(file)
    nparr = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("received.png", img)
    return jsonify({'status': "received"})


if __name__ == '__main__':
	app.run(host="192.168.1.100", port= 5000)