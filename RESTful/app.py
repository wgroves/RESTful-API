from flask import Flask
from flask import Response
from flask import json
from flask import request
from DBController import DBController
import sqlalchemy_declaration

app = Flask(__name__)
controller = DBController()

@app.route('/addParent', methods = ['POST'])
def api_addParent():

    if request.headers['Content-Type'] == 'application/json':
        args = request.json
        name = args["name"]
        controller.addParent(name)
        return "Success!"
    else:
        return "Unsupported Input: Please pass JSON data in form: {'name':name}"

@app.route('/addChild', methods = ['POST'])
def api_addChild():
    if request.headers['Content-Type'] == 'application/json':
        args = request.json
        child_name = args["name"]
        parent_id = args["p_id"]
        controller.addChild(child_name, parent_id)
        return "Success!"
    else:
        return "Unsupported Input: Please pass JSON data in form: {'name':name}"

@app.route('/parent/<int:parentid>')
def api_getParent(parentid):
    resultDict = controller.getParent(parentid)
    js = json.dumps(resultDict)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/child/<int:childid>')
def api_getChild(childid):
    resultDict = controller.getChild(childid)
    js = json.dumps(resultDict)
    resp = Response(js,status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()