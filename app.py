from flask import Flask, request, render_template
import json
from JianYuMaker import jianyu

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        resultSTR = jianyu(user_input)
        return f"Here's your jianyu result: {resultSTR}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
