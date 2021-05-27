from flask import Flask, request, jsonify, render_template, redirect, url_for
from predict import predict_imgURL
import time

app = Flask(__name__)


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
    return render_template("index.html", result="TEST")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    global result
    req = request.get_json()
    # print(req)
    result = req['imgURL']
    
    result = predict_imgURL(req['imgURL'])
    print(result)
#     print(request.method)

    # return redirect(url_for('result'))#/result{result}")
    # return redirect('http://127.0.0.1:5000')
    time.sleep(2)
    return redirect(f'/result/{str(result)}')
    # return jsonify(str(result))

    # return f"<img src={result} />"

@app.route("/result/<result>")
def result(result):
    print(result)
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
 