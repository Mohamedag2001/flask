from flask import Flask , render_template

app = Flask(__name__)

@app.route("/accueil")
def index():
    return render_template("index.html", title="Accueil")

@app.route("/apropos")
def about():
    return render_template("about.html", title="À propos")


if __name__ == "__main__":
    app.run(debug=True)


    