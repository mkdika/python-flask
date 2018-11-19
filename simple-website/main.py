from flask import Flask, render_template

app = Flask(__name__)


# use external template response renderer
@app.route("/")
@app.route("/index")
def hello():
    return render_template("hello.html")


# Main function
if __name__ == '__main__':

    # Enable debug mode for development
    app.run(debug=True)
