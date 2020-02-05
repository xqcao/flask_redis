from flask import Flask, render_template, request, redirect, url_for
from redis import Redis
import json

db = Redis(host='myredis', port=6379)
app = Flask(__name__)


@app.route('/')
def hello():
    count = db.incr('count')

    return 'Hello World! Count is {}'.format(count)


@app.route("/home")
def home_page():
    data = db.hgetall('nameVsemail')
    print(data)
    # dd = json.dumps(data)
    return render_template("index.html", msg="hello home", dd=data)


@app.route('/addnew', methods=["POST"])
def add_one():
    uname = request.form['username']
    uemail = request.form['email']
    db.hset("nameVsemail", uname, uemail)
    print(uname, uemail)
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(port="5001", host="0.0.0.0", debug=True)
