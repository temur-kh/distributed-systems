from flask import Flask, request, render_template
from pymongo import MongoClient
app = Flask(__name__)
list = [{"message": "nameA: messageA"},
        {"message": "nameB: messageB"},
        {"message": "nameC: messageC"}]
client = MongoClient("server-1", replicaset='rs0', username='mongo-admin',password='password')
db = client['messenger']
col = db['messages']
col.insert_many(list)


@app.route('/')
def index():
    messages = []
    for msg in col.find({}):
        messages.append(msg['message'])
        print(msg)
    return render_template('index.html', messages=messages)


@app.route('/add_msg/', methods=['POST'])
def doit():
    msg = request.form['message']
    name = request.form['name']
    str = name + ': ' + msg
    col.insert_one({"message": str})
    messages = []
    for msg in col.find({}):
        messages.append(msg['message'])
        print(msg)
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

