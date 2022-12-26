import json
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def index():
    return jsonify(data)


@app.route('/data', methods=['POST'])
def add_user():
    #for num in range(len(data)):
    #    if request.get_json()['id'] == data[num]['id']:
    #        print("ID number is busy")
    #    else:
    data.append(request.get_json())
    return jsonify(data)


@app.route('/data', methods=['PUT'])
def update_user():
    data[request.get_json()['id']] = request.get_json()
    return jsonify(data)


@app.route('/data', methods=['DELETE'])
def del_user():
    data.pop(request.get_json()['id'])
    # data.append({'name': 'Matt'})
    # return jsonify(data)
    pass


if __name__ == '__main__':
    app.run(debug=True)


