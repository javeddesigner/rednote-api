import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "RedNote API is running!"

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")  # Get the URL from the query parameter
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    # Simulate downloading process (you should add actual logic here)
    return jsonify({"message": "Download started", "url": url})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's default port
    app.run(host="0.0.0.0", port=port)
