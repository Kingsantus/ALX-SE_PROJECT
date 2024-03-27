from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': "Williams Joe",
        'title': "Washburn Elegante S24S Bella Tono Studio",
        'category': "Acostic",
        'price': 5000,
        'location': "Enugu, Nigeria",
        'discount': 0.05,
        'discription': "Good Sound and electrical",
        'date_posted': "March 27, 2024"
    },
    {
        'author': "Kelvin Finder",
        'title': "Medeli Electronics AKX10 Arranger Pro Digital Workstation",
        'category': "Keyboard",
        'price': 10000,
        'location': "Anambra, Nigeria",
        'discount': 0.03,
        'discription': "Good Sound and electrical",
        'date_posted': "March 25, 2024"
    }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('base.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)