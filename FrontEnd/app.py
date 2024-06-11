import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

from flask import Flask, request, render_template, redirect, url_for, jsonify
from Backend.Connection.connection import getConnection
from Backend.Queries.query import selectSingle
from Backend.Queries.query import selectAll
from Backend.Queries.update import update
from Backend.Queries.delete import delete
from Backend.Queries.create import create

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
    update(neighborhood, block, lot, model, elevation, color,conn)
    print(selectSingle(neighborhood=neighborhood,block=block,lot=lot,connection=conn))
    return redirect(url_for('home'))


@app.route('/delete/<string:neighborhood>/<int:block>/<int:lot>', methods=['GET'])
def delete_house(neighborhood,block,lot):
    house = selectSingle(neighborhood,block,lot,conn)
    if house:
        delete(neighborhood,block,lot,conn)
    return jsonify({'message': 'House deleted successfully'}), 200


@app.route('/house', methods = ['GET','POST'])
def houses():
    print(request.method)
    if (request.method == 'GET'):
        result = selectAll()
        return jsonify(result)
    elif (request.method == 'POST'):
        neighborhood = request.form['neighborhood']
        block = request.form['block']
        lot = request.form['lot']
        message = create(neighborhood,block,lot,conn)
        return f"House with id: {message} was created!"
    



@app.route('/house/<string:neighborhood>/<int:block>/<int:lot>', methods=['GET','PUT','DELETE'])
def singleHouse():
    print("stub")

if __name__ == '__main__':
    app.run(debug=True)