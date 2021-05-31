from flask import Flask, request, jsonify, render_template, redirect, url_for
from predict import predict_imgURL
from array_to_img import transfer_nparray_to_img
from divide_img import divide_img
import time

applicaiton = app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# def landing_page():
#     TEST = ""
#     if request.method == 'POST':
#         req = request.get_json()
#         print(req['imgURL'])
#         TEST = "RESULT"
#         return render_template("result.html", result=TEST)
#     else:
#         return render_template("index.html", result=TEST)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def predict():
    global result
    req = request.get_json()
    # print(req)
    img_url = req['imgURL']
    scenario = req['scenario']

    if scenario == "A":
        prediction, img_np_arr = predict_imgURL(img_url)
        img_URL = transfer_nparray_to_img(img_np_arr)
        return jsonify((str(prediction), img_URL))

    if scenario == "B":
        imgA_url, imgB_url = divide_img(img_url)
        prediction_A, _ = predict_imgURL(imgA_url)
        prediction_B, _ = predict_imgURL(imgB_url)
        return jsonify((str(prediction_A), str(prediction_B), imgA_url, imgB_url))

# @app.route("/result")
# def result():
#     print(request.query_string)
#     model_output = request.args.get('model_output')
#     return render_template("result.html", result=model_output)


if __name__ == "__main__":
    app.run(debug=True)
 