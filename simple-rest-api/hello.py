from flask import Flask

app = Flask(__name__)


# default method is GET
# can be multiple routes mapped, in this case "/" and "/index"
@app.route("/")
@app.route("/index")
def index():
    return "Hello World XXX!"


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

    # Enable debug mode for development
    app.run(debug=True)
