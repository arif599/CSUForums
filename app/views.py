from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["search"])
        return render_template("home.html")
    else:
        return render_template("home.html", home=True)