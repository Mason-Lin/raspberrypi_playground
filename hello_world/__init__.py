from flask import Flask, request
app = Flask(__name__)

@app.route("/")
@app.route("/hello1")
@app.route("/hello1-same")
def hello():
    return "<h1>Hello World!!</h1>"

# http://172.20.10.2:8000/hello2/mason/lin
# RESTful
@app.route("/hello2/<name>/<surname>")
def hello_restful(name, surname):
    return f"<h1>Hello, {name} {surname}</h1>"

# Query string
# http://172.20.10.2:8000/hello3?name=mason&surname=lin
@app.route("/hello3/")
def hello_query():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"<h1>Hello, {name} {surname}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
