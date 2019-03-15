from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/poultry/')
def poultry():
    return render_template('poultry.html')

@app.route('/dairy/')
def dairy():
    return render_template('dairy.html')


if __name__=="__main__":
    app.run(debug=True)
