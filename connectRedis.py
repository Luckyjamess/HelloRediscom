import os
import redis
import json
from flask import Flask,request,jsonify

app = Flask(__name__)
db=redis.StrictRedis(
        host='node9162-advweb-25.app.ruk-com.cloud',
        port=11156,
        password='LZDovo88328',
        decode_responses=True)

@app.route('/',methods=['GET']) 
def Show_keys():     
    name=db.keys() 
    name.sort()     
    req = []     
    for i in name :         
        req.append(db.hgetall(i))     
    return jsonify(req)

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run()

