from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    r=request.get_json()
    a=int(r["first"])
    b=int(r["second"])
    c=a+b
    data={
        "result":c
    }
    return jsonify(data),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    r=request.get_json()
    a=int(r["first"])
    b=int(r["second"])
    c=a-b
    data={
        "result":c
    }
    return jsonify(data),200


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
