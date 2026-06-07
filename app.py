from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "hey! this is the output of the which is printed with flask application"

if __name__ == "__main__":
    app.run(debug=True)
