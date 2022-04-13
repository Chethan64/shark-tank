# Flask application that contains the REST API endpoint routines

# Importing the required libraries
import json
from flask import Flask, jsonify, request, Response
from database.db import client, database, collection
from validate.validreq import verifyOfferRequest, verifyPitchRequest

app = Flask(__name__)

# Endpoint to post a pitch to the backend
@app.route('/pitches', methods=['POST'])
def post_pitch():
    body = request.get_json()
    document = dict()

    # Check if the request body is valid
    if not verifyPitchRequest(body):
        return Response(status=400)

    # Getting the id for the pitch from the number of documents in the collection
    # and inserting into the collection
    id_ = collection.count_documents({}) + 1
    document["id"] = str(id_)
    body["offers"] = list()
    document.update(body)
    collection.insert_one(document)

    # Successful response output
    response = {"id": str(id_)}
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=201)

# Endpoint to fetch all the pitches in the reverse chronological order from the backend
@app.route('/pitches', methods=['GET'])
def get_pitches():
    response = []  

    # Iterating through the collection and setting _id field as 0  
    for document in collection.find({}, {'_id': 0}):
        response.insert(0, document)
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=200)

# Endpoint to make a counter offer for a pitch
@app.route('/pitches/<int:id>/makeOffer', methods=['POST'])
def make_offer(id):
    # Checking if the id is present in the collection
    if not collection.count_documents({'id': str(id)}):
        return Response(status=404)

    # Checking if the request body is valid
    body = request.get_json()
    if not verifyOfferRequest(body):
        return Response(status=400)

    # Appending the offer to the list of the specified document
    document = collection.find_one({'id': str(id)})
    offer_id = len(document['offers']) + 1
    offer = dict()
    offer["id"] = str(offer_id)
    offer.update(body)
    collection.update_one({'id': str(id)}, {'$push': {'offers': offer}})

    # Successful response output
    response = json.dumps({'id': str(offer_id)}, indent=4)
    return Response(response=response, mimetype='application/json', status=201)

# Endpoint to specify a particular id to fetch a single pitch
@app.route('/pitches/<int:id>', methods=['GET'])
def get_pitch(id):
    # Check if the id is valid
    if not collection.count_documents({'id': str(id)}):
        return Response(status=404)
    
    # Return the response 
    response = collection.find_one({"id": str(id)}, {'_id': 0})
    response = json.dumps(response, indent=4)
    return Response(response=response, mimetype='application/json', status=200)

if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=True)