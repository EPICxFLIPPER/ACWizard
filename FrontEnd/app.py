import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

from flask import Flask, request, render_template, redirect, url_for, jsonify
from Backend.Connection.connection import getConnection
from Backend.Queries.read import selectSingle
from Backend.Queries.read import selectAll
from Backend.Queries.update import update
from Backend.Queries.delete import delete
from Backend.Queries.create import create

app = Flask(__name__)
conn = getConnection()

@app.route('/')
def home():
    return render_template('index.html', message="Hello, Flask!")


@app.route('/house', methods = ['GET','POST'])
def houses():
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
def singleHouse(neighborhood,block,lot):
    if (request.method == 'GET'):
        result = selectSingle(neighborhood,block,lot,conn)
        return jsonify(result)
    elif (request.method == 'PUT'):
        model = request.form['model']
        elevation = request.form['elevation']
        colour = request.form['colour']

        house = selectSingle(neighborhood,block,lot,conn)[0]
        if (model is None or model == ""):
            model = house[5]
        if (elevation is None or elevation == ""):
            elevation = house[6]
        if (colour is None or colour == ""):
            colour = house[7]
        
        update(neighborhood,block,lot,model,elevation,colour,conn)
        return f"House updated"
    
    elif (request.method == 'DELETE'):
        delete(neighborhood,block,lot,conn)
        return jsonify({'message': 'House deleted successfully'}), 200
    

if __name__ == '__main__':
    app.run(debug=True)