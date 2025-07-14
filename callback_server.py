from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/indodax/callback", methods=["POST"])
def indodax_callback():
    data = request.get_json()
    print("📥 Callback diterima dari Indodax:")
    print(data)

    # Nanti bisa validasi signature di sini (opsional)
    
    return jsonify({"status": "received"}), 200

@app.route("/", methods=["GET"])
def home():
    return "✅ Indodax Callback Server Aktif!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

