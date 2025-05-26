from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    benutzername = request.form["username"]
    passwort = request.form["password"]
    print(f"Benutzername: {benutzername}")
    print(f"Passwort: {passwort}")
    return f"Login empfangen für Benutzer: {benutzername}"

@app.route("/roll", methods=["GET"])
def roll():
    würfel1 = random.randint(1, 6)
    würfel2 = random.randint(1, 6)
    summe = würfel1 + würfel2
    doppel = würfel1 == würfel2
    return f"{würfel1},{würfel2},{summe},{doppel}"

if __name__ == "__main__":
    app.run(debug=True)
