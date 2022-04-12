import json
from flask import Flask, jsonify, request, Response

def verifyPitchRequest(request: dict) -> bool:
    if not request:
        return False

    if len(request) != 5:
        return False

    if "entrepreneur" not in request:
        return False
    elif not request["entrepreneur"].strip() or type(request["entrepreneur"]) is not str:
        return False

    if "pitchTitle" not in request:
        return False
    elif not request["pitchTitle"].strip() or type(request["pitchTitle"]) is not str:
        return False
    
    if "pitchIdea" not in request:
        return False
    elif not request["pitchIdea"].strip() or type(request["pitchIdea"]) is not str:
        return False

    if "askAmount" not in request:
        return False
    elif type(request["askAmount"]) is not float or request["askAmount"] < 0:
        return False

    if "equity" not in request:
        return False
    elif type(request["equity"]) is not float or request["equity"] > 100 or request["equity"] < 0:
        return False

    return True

def verifyOfferRequest(request: dict) -> bool:
    if not request:
        return False
    
    if len(request) != 4:
        return False
    
    if "investor" not in request:
        return False
    elif not request["investor"].strip() or type(request["investor"]) is not str:
        return False
    
    if "amount" not in request:
        return False
    elif type(request["amount"]) is not float:
        return False

    if "equity" not in request:
        return False
    elif type(request["equity"]) is not float or request["equity"] < 0 or request["equity"] > 100:
        return False
    
    if "comment" not in request:
        return False
    elif not request["comment"].strip() or type(request["comment"]) is not str:
        return False
    
    return True