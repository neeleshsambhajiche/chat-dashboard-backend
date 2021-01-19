from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
from PIL import Image


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

breachList = []
dict1 = {"email": "123@gmail.com", "time": "5.00 pm 12th July 2020",
         "type": "Sleeping", "ImageName": "titan-graph3.JPG"}
breachList.append(dict1)
breachList.append({"email": "123@gmail.com", "time": "5.00 pm 12th July 2020",
                   "type": "Mobile", "ImageName": "titan-graph3.JPG"})


@app.route("/send_image", methods=["POST"])
def save_image():
    file = request.files['image']
    img = Image.open(file.stream)
    img.save('new.png')
    return 'success'


@app.route("/get_image", methods=["GET"])
def get_image():
    return send_file('titan-graph3.JPG', mimetype='image/jpeg')


@app.route("/breaches", methods=["GET"])
def get_breaches():
    return jsonify(breachList)


if __name__ == "__main__":
    app.run(debug=True)
