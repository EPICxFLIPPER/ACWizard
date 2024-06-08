from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Hello, Flask!")

if __name__ == '__main__':
    app.run(debug=True)