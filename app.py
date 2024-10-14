from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users_data = [
    {
        'username': 'jollyroger1',
        'password': 'Jolly1010##'
    },
        {
        'username': 'jollyroger2',
        'password': 'Jolly1010##'
    },
        {
        'username': 'jollyroger3',
        'password': 'Jolly1010##'
    },
        {
        'username': 'jollyroger4',
        'password': 'Jolly1010##'
    }
]


@app.route("/", methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            error = "Incomplete login info"
        else:
            for user_data in users_data:
                if username == user_data['username'] and password == user_data['password']:
                    return render_template("success.html", username=username)

            error = "invalid username / password"

    return render_template("login.html", error=error)




if __name__ == "__main__":
    app.run(debug=True)