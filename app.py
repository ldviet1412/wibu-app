#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)

wibus = [
    {
        'id': 1,
        'name': 'wibu1',
        'gender': 'male', 
    },
    {
        'id': 2,
        'name': 'wibu2',
        'gender': 'male', 
    },
]

@app.route('/hello', methods=['GET'])
def hello():

    return jsonify({'result': "Hello"})

@app.route('/add', methods=['GET'])
def add():
    data = request.json
    a = data["a"]
    b = data["b"]
    return jsonify({'sum': a+b})


@app.route('/wibu', methods=['GET'])
def get_wibus():
    return jsonify({'wibu': wibus})


@app.route('/wibu/<int:wibu_id>', methods=['GET'])
def get_wibu(wibu_id):
    wibu = [wibu for wibu in wibus if wibu['id'] == wibu_id]
    if len(wibu) == 0:
        abort(404)
    return jsonify({'wibu': wibu[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/wibu', methods=['POST'])
def create_wibu():
    print("dfsfgdjgfdjgfdjgfdj")
    print(request.json)
    if not request.json or not 'name' in request.json:
        abort(400)
    wibu = {
        'id': wibus[-1]['id'] + 1,
        'name': request.json['name'],
        'gender': request.json.get('gender', ""),
    }
    wibus.append(wibu)
    return jsonify({'wibu': wibu}), 201


@app.route('/wibu/<int:wibu_id>', methods=['DELETE'])
def delete_wibu(wibu_id):
    wibu = [wibu for wibu in wibus if wibu['id'] == wibu_id]
    if len(wibu) == 0:
        abort(404)
    wibus.remove(wibu[0])
    return jsonify({'result': True})


@app.route('/wibu/<int:wibu_id>', methods=['PUT'])
def update_wibu(wibu_id):

    wibu = [wibu for wibu in wibus if wibu['id'] == wibu_id]
    print(wibu)
    if len(wibu) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json:
        abort(400)
    if 'gender' in request.json:
        abort(400)

    wibu[0]['name'] = request.json.get('name', wibu[0]['name'])
    wibu[0]['gender'] = request.json.get('gender', wibu[0]['gender'])
    return jsonify({'wibu': wibus[0]})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
