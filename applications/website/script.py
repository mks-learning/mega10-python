from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
# the route('/') is referring to the page within the website. So '/' means
# root. And '/about/' would be root/about
def home():
    return render_template('home.html')


@app.route('/about/')
# the route('/') is referring to the page within the website. So '/' means
# root. And '/about/' would be root/about
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
