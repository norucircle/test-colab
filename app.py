from flask import Flask, render_template, request

from main import iris_data_prediction

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def prediction():
    sepal_length = float(request.form["sl"])
    sepal_width = float(request.form["sw"])
    petal_length = float(request.form["pl"])
    petal_width = float(request.form["pw"])

    prediction_class = iris_data_prediction(sepal_length, sepal_width, petal_length, petal_width)
    
    return "<center><h1>ผลลัพธ์ของการพยากรณ์เป็นดอก {}</h1></center>".format(prediction_class)

if __name__ == "__main__":
    app.run(debug=True)