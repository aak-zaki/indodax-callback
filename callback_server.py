from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/indodax/callback", methods=["POST"])
def indodax_callback():
    data = request.get_json()
    print("📥 Callback dari Indodax:")
    print(data)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Port bebas di lokal, Render akan override
