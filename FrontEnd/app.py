import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

from flask import Flask, request, render_template, redirect, url_for
from Backend.Connection.connection import getConnection
from Backend.Queries.query import selectSingle
from Backend.Queries.update import update

app = Flask(__name__)
conn = getConnection()

@app.route('/')
def home():
    return render_template('index.html', message="Hello, Flask!")

@app.route('/update/<string:neighborhood>/<int:block>/<int:lot>', methods=['GET'])
def show_update_form(neighborhood, block, lot):
    house = selectSingle(neighborhood,block,lot,conn)
    if house:
        return render_template('update.html', neighborhood=neighborhood, block=block, lot=lot, house=house)
    else:
        return "House not found", 404

# Route to handle the form submission
@app.route('/update/<string:neighborhood>/<int:block>/<int:lot>', methods=['POST'])
def handle_update_form(neighborhood, block, lot):
    model = request.form['model']
    elevation = request.form['elevation']
    color = request.form['color']
    print(neighborhood)
    print(block)
    print(lot)
    print(model)
    print(elevation)
    print(color)
    update(neighborhood, block, lot, model, elevation, color)
    print(selectSingle(neighborhood,block,lot,conn))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)