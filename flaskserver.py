from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Verbindet HTML mit dieser Route

if __name__ == "__main__":
    app.run(debug=True)
