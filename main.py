from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    #planet_data = next(item for item in data if item["name"] == name)
    #planet_data = next(item for item data if item["names"] == name)
    #planet_data = next(item for item in data if item["names"] == name)
    #planet_data = next(item for item in data if item["names"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

#if __name__ == "__main__":
#if __main__ == "__main__":
#if __name__ == "__name__":
#if __main__ == "__name__":
    app.run()