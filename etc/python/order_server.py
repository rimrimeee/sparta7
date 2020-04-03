from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta.order



def run_server():
    server = Flask('주문서버')
    @server.route('/', methods=['GET'])
    def home():
        return render_template('homework4.html')

    @server.route('/order', methods=['GET'])
    def read_order():
       orders = list(db.find({},{'_id':0}))
       return jsonify({'result': 'success', 'orders': orders})

    @server.route('/order', methods=['POST'])
    def add_order():
        name = request.form['name']
        count = request.form['count']
        email = request.form['email']
        phone = request.form['phone']

        order = {'name': name, 'count': count, 'email': email, 'phone':phone}
        db.insert_one(order)
        result = {'result':'success','message':'good'}
        return jsonify(result)




    server.run('0.0.0.0', port=5000, debug=True)
run_server()














