from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

from bson import ObjectId


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/flaskusers'
mongo = PyMongo(app)

# Settings
CORS(app)

db_operations = mongo.db.flaskusers


@app.route('/users', methods=['POST'])
def createUser():
    print(request.json)
    id = db_operations.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id)))


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db_operations.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)


@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = db_operations.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']
    })


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    print(request.json)
    db_operations.update_one({'_id': ObjectId(id)}, {"$set": {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    }})
    return jsonify({'message': 'User Updated'})


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db_operations.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User Deleted'})


if __name__ == "__main__":
    app.run(debug=True)
