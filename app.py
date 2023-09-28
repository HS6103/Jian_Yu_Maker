from flask import Flask, request, render_template
from JianYuMaker import jianyu

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        # You can process the user input here using your Python program.
        # For demonstration, we'll just return it.
        return f"You entered: {user_input}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
