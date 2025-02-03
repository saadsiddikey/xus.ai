from flask import Flask, render_template, request
from chat_ai import chat_with_ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = chat_with_ai(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
