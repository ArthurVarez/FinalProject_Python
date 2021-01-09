from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def hi():
    return "<h1>Hello you<h1>"

if __name__=="__main__":
    app.run(port=5050, debug=True)