from flask import Flask, request, render_template, jsonify
from JianYuMaker import jianyu

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_result", methods=["POST"] )
def get_result():
    if request.method == "POST":
        user_input = request.form["user_input"]
        resultSTR = jianyu(user_input)
    return jsonify({'result': resultSTR})    
    

if __name__ == "__main__":
    app.run(debug=True)
