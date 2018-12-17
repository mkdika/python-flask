from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        msg = ""
        username = request.form["username"]
        passwd = request.form["password"]

        # static useless validation
        if username == 'admin' and passwd == 'admin':
            msg = 'Username and password are correct'
        else:
            msg = 'Username or password are incorrect'
        return render_template('homepage.html', message=msg)


# Main function
if __name__ == '__main__':

    # Enable debug mode for development
    app.run(debug=True)
