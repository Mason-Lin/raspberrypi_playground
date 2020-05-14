from flask import Flask, make_response
app = Flask(__name__)
app.debug = True

@app.route("/")
def show_icon():
    return make_response("""\
<!DOCTYPE html>
<meta charset="utf-8">
<title>Flask is fun</title>
<img src="static/flask.png" alt="Flask">""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8001")
