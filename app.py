from flask import Flask, request, render_template, jsonify
import json
from JianYuMaker import jianyu

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/get_result", methods=["POST"] )
def get_result():
    if request.method == "POST":
        user_input = request.form["user_input"]
        resultSTR = jianyu(user_input)
    return jsonify(f"Here's your jianyu result: {resultSTR}")    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
