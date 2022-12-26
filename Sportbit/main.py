import json
from flask import Flask, jsonify, request, render_template
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="watch",
    user="postgres",
    password="*******",
    port=5434
)
cursor = conn.cursor()
success_message = {'success': True}



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def index():
    data_clients = []
    sql = 'SELECT * FROM owner'
    cursor.execute(sql)
    data = cursor.fetchall()
    for client in data:
        data_owners.append({'id': client[0],
                            'name': client[1],
                            'surname': client[2],
                            'phone number': client[3]})
    print(data_clients)
    print(request.url)
    return render_template('index1.html', clients=data_clients)



@app.route('/data', methods=['POST'])
def add_user():
    sql = 'INSERT INTO owner VALUES (%s, %s, %s, %s)'
    id = random.randint(1, 999999)
    name = request.get_json()['name']
    lastname = request.get_json()['lastname']
    email = request.get_json()['email']
    cursor.execute(sql, (id, name, lastname, email))
    conn.commit()
    return index(id)



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


