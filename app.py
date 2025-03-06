from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route("/")
def home():
    return "API is running!"

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    return jsonify({"success": True, "download_link": "https://example.com/video.mp4"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
