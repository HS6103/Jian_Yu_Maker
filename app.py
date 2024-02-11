from flask import Flask, request, render_template, jsonify
from JianYuMaker import jianyu

app = Flask(__name__)

def jian_string(inputSTR):
    return jianyu(inputSTR)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            result = jian_string(user_input)
            return jsonify(result=result)
        else:
            return jsonify(result='Input needed')        
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
