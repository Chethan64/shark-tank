import json
from flask import Flask, jsonify, request, Response

# Function to check if the pitch request is valid
def verifyPitchRequest(request) -> bool:
    # Empty body
    if not request:
        return False

    # Extra or less arguments
    if len(request) != 5:
        return False

    # Checking every key-value pair according to the constraints
    if "entrepreneur" not in request:
        return False
    elif not request["entrepreneur"] or type(request["entrepreneur"]) is not str:
        return False

    if "pitchTitle" not in request:
        return False
    elif not request["pitchTitle"] or type(request["pitchTitle"]) is not str:
        return False
    
    if "pitchIdea" not in request:
        return False
    elif not request["pitchIdea"] or type(request["pitchIdea"]) is not str:
        return False

    if "askAmount" not in request:
        return False
    elif request["askAmount"] < 0:
        return False

    if "equity" not in request:
        return False
    elif request["equity"] > 100 or request["equity"] < 0:
        return False

    return True

# Function to verify offer request
def verifyOfferRequest(request) -> bool:
    # Empty request body
    if not request:
        return False
    
    # Extra or less pairs
    if len(request) != 4:
        return False
    
    # Checking every key-value pair according to the constraints
    if "investor" not in request:
        return False
    elif not request["investor"] or type(request["investor"]) is not str:
        return False
    
    if "amount" not in request:
        return False
    elif request["amount"] < 0:
        return False

    if "equity" not in request:
        return False
    elif request["equity"] < 0 or request["equity"] > 100:
        return False
    
    if "comment" not in request:
        return False
    elif not request["comment"] or type(request["comment"]) is not str:
        return False
    
    return True