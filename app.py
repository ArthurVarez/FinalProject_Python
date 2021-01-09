from flask import Flask

app = Flask(__name__)

@app.route("/")

def Home():
    return "<h1>Drug prediction using personnality score<h1>"

if __name__=="__main__":
    app.run(port=5050, debug=True)