from flask import Flask , render_template
app = Flask(__name__)

@app.route('/login')
def hello_world():
    return render_template("login.html")

@app.route('/register')
def nice():
    return render_template("register.html")
@app.route('/')
def main():
    return render_template("main page.html")
if __name__ == "__main__":
    app.run(debug = True)