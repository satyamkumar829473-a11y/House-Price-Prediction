from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])

    price = (area * 2500) + (bedrooms * 500000)

    return render_template(
        "index.html",
        prediction_text=f"Estimated House Price: ₹{price:,.0f}"
    )

if __name__ == "__main__":
    app.run(debug=True)