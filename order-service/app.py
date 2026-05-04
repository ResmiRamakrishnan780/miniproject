from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    return jsonify([
        {"order_id": 101, "status": "PLACED"},
        {"order_id": 102, "status": "DELIVERED"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)