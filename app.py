from flask import Flask, request, jsonify, render_template
from predict import predict_imgURL
from array_to_img import transfer_nparray_to_img
from divide_img import divide_img
from save_train_data import save_train_data
from retrieve_train_data import retrieve_train_data
from clear_train_data import clear_train_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def predict():
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
    
    if scenario == "SAVE":
        train_data = {
            "imgURL": img_url,
            "label": req['prediction']
        }

        save_train_data(train_data)

        return "Successfully saved to MongoDB"

@app.route("/trainset")
def display_train_set():
    train_set = retrieve_train_data()
    print(type(train_set))
    return render_template("dataset.html", data=train_set)

@app.route("/trainset", methods=["POST"])
def clear_train_set():
    req = request.get_json()
    print(req["id"])
    clear_train_data(req["id"])
    return "yes"

@app.route("/api/trainset")
def train_set():
    train_set = retrieve_train_data()
    dicts = []
    for row in list(train_set):
        dictionary ={}
        dictionary["imgURL"] = row["imgURL"]
        dictionary["label"] = row["label"]
        dicts.append(dictionary)

    return jsonify(data=dicts)

if __name__ == "__main__":
    app.run(debug=True)
 