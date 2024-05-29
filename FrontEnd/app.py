from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/FrontEnd')
def home():
    return render_template('index.html', message="Hello, Flask!")

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Handling POST request'
    else:
        return 'Handling GET request'

if __name__ == '__main__':
    app.run(debug=True)