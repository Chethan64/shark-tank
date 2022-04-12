import json
from flask import Flask, jsonify, request, Response
from database.db import client
from validate.validreq import verifyOfferRequest, verifyPitchRequest

app = Flask(__name__)
database = client.xharktank
collection = database.pitches

@app.route('/pitches', methods=['POST'])
def post_pitch():
    body = request.get_json()
    document = dict()

    if not verifyPitchRequest(body):
        return Response(status=400)

    id_ = collection.count_documents({}) + 1
    document["id"] = id_
    body["offers"] = list()
    document.update(body)
    collection.insert_one(document)

    response = {"id": id_}
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches', methods=['GET'])
def get_pitches():
    response = []    
    for document in collection.find({}, {'_id': 0}):
        response.insert(0, document)
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=200)

@app.route('/pitches/<int:id>/makeOffer', methods=['POST'])
def make_offer(id):
    if not collection.count_documents({'id': id}):
        return Response(status=404)

    body = request.get_json()
    if not verifyOfferRequest(body):
        return Response(status=400)

    document = collection.find_one({"id": id})
    offer_id = len(document['offers']) + 1
    offer = dict()
    offer["id"] = offer_id
    offer.update(body)
    collection.update_one({'id': id}, {'$push': {'offers': offer}})

    response = json.dumps({'id': offer_id}, indent=4)
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches/<int:id>', methods=['GET'])
def get_pitch(id):
    if not collection.count_documents({'id': id}):
        return Response(status=404)
    
    response = collection.find_one({"id": id}, {'_id': 0})
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=200)

app.run(host="localhost", port=8081, debug=True)