import json
from flask import Flask, jsonify, request, Response
from database.db import client

app = Flask(__name__)
database = client.xharktank
collection = database.pitches

@app.route('/')
def root():
    return {
        "Welcome to Sharktank": "Pitch your ideas in!"
    }

@app.route('/pitches', methods=['POST'])
def post_pitch():
    body = request.get_json()
    
    id_ = collection.count_documents({}) + 1
    body["offers"] = list()
    body["id"] = id_
    collection.insert_one(body)

    response = {"id": id_}
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches', methods=['GET'])
def get_pitches():
    response = []    
    for document in collection.find({}, {'_id': 0}):
        response.insert(0, document)
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=200)

@app.route('/pitches/<int:id>/makeOffer', methods=['POST'])
def make_offer(id):
    if(id > collection.count_documents({})):
        return Response(status=404)
        
    body = request.get_json()
    document = collection.find_one({"id": id})
    offer_id = len(document['offers']) + 1
    body["id"] = offer_id
    collection.update_one({'id': id}, {'$push': {'offers': body}})
    response = json.dumps({'id': offer_id})
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches/<int:id>', methods=['GET'])
def get_pitch(id):
    if(id > collection.count_documents({})):
        return Response(status=404)
    
    response = collection.find_one({"id": id}, {'_id': 0})
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=200)

app.run(host="localhost", port=8081, debug=True)