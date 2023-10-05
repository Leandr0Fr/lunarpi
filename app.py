from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify(message='API on!'), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))