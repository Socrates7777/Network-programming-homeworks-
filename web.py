from flask import Flask , render_template
web = Flask(__name__)

@web.route("/")
def home():
    return render_template("home.html")

@web.route("/home.html")
def Home_H():
    return render_template("home.html")

@web.route("/contact.html")
def Sho():
    return render_template("contact.html")

@web.route("/info.html")
def Cont():
    return render_template("info.html")


if __name__ == "__main__" :
    web.run(debug=True)


