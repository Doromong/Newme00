from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.planme


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

#
#
# UserName(POST) API
@app.route('/events', methods=['POST'])
def save_event():
    eventname_receive = request.form['eventname_give']
    doc = {
        'eventname': eventname_receive,
    }
    db.allevents.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '이벤트 생성 완료!'})


#*여기위로 살리기

# API 역할을 하는 부분
@app.route('/users', methods=['POST'])
def add_user():
    user_receive = request.form['user_give']
    doc = {
        'names':user_receive,
    }
    db.allevents.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문 완료!'})


@app.route('/users', methods=['GET'])
def show_users():
    allusers = list(db.allevents.find({}, {'_id': False}))
    return jsonify({'result':'success','all_users': allusers})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)