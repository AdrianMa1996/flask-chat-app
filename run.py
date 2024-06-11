from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# Man kann glaub kein env im OneDrive erstellen...

if __name__ == "__main__":
    app.run(debug=True)