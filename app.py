from flask import Flask, request, render_template, jsonify
from JianYuMaker import jianyu

app = Flask(__name__)

def jian_string(inputSTR):
    return jianyu(inputSTR)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/get_result', methods=['GET', 'POST'] )
def get_result():
    user_input = request.form["user_input"]
    result = jian_string(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)
