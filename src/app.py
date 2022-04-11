import json
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

pitches = list()

@app.route('/')
def root():
    return {
        "Welcome to Sharktank": "Pitch your ideas in!"
    }

@app.route('/pitches', methods=['POST'])
def post_pitch():
    body = request.get_json()
    body["offers"] = list()
    pitches.append(body)
    response = {"id": len(pitches)}
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches', methods=['GET'])
def get_pitches():
    print(pitches)
    print(type(pitches))
    rev = pitches[::-1]
    response = json.dumps(rev)
    return Response(response=response, mimetype='application/json', status=200)

@app.route('/pitches/<int:id>/makeOffer', methods=['POST'])
def make_offer(id):
    if(id > len(pitches)):
        return Response(status=404)
        
    body = request.get_json()
    pitches[id-1]["offers"].append(body)
    response = {"id": len(pitches[id-1]["offers"])}
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=201)

@app.route('/pitches/<int:id>', methods=['GET'])
def get_pitch(id):
    if(id > len(pitches)):
        return Response(status=404)
    
    response = pitches[id-1]
    response = json.dumps(response)
    return Response(response=response, mimetype='application/json', status=200)

app.run(host="localhost", port=8081, debug=True)