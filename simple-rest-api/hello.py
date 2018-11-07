from flask import Flask
app = Flask(__name__)


# default method is GET
@app.route("/")
def hello():
    return "Hello World!"


# path variable
# explicit HTTP method
@app.route("/echo/<message>", methods=["GET"])
def echo(message):
    return message

# POST demo
# @app.route("/insert", methods=["POST"])
# def insert():
#     return "test"


if __name__ == '__main__':
    app.run(debug=True)
