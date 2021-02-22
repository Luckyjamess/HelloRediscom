import os
import redis
import json
from flask import Flask,request,jsonify

#connectRedis
app = Flask(__name__)
db=redis.StrictRedis(
        #host='node9162-advweb-25.app.ruk-com.cloud',
        host='10.100.2.140',
        #port=11156,
        port=6379,
        password='LZDovo88328',
        decode_responses=True)

#แสดงข้อมูลที่มีทั้งหมดของตาราง
@app.route('/',methods=['GET']) 
def Show_fruits():     
    name=db.keys() 
    name.sort()
    req = []     
    for i in name :         
        req.append(db.hgetall(i))     
    return jsonify(req)

#แสดงข้อมูล1อย่างในตาราง
@app.route('/<Key>', methods=['GET'])
def Show_fruit(Key):
    name = db.hgetall(Key)  
    #print (name)
    return jsonify(name)

#ใส่ข้อมูลเพิ่มในตาราง
@app.route('/Key', methods=['POST'])
def add_fruit():
    id = request.json['id']
    name = request.json['name']
    price = request.json['price']
    #print (id)
    #print (name)
    #print (price)
    user = {"id":id, "name":name, "price":price}
    db.hmset(name,user)
    return 'insert data success!!!'

#อัพเดทข้อมูลในตาราง
@app.route('/<Key>', methods=['PUT'])
def update_fruit(Key):
    id = request.json['id']
    name = request.json['name']
    price = request.json['price']
    print (id)
    print (name)
    print (price)
    user = {"id":id, "name":name, "price":price}
    db.hmset(name,user)
    return 'Update data success!!!'

#ลบข้อมูล
@app.route('/<Key>', methods=['DELETE'])
def delete_staff(Key):
    db.delete(Key)
    return 'Delete data success!!!'

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

