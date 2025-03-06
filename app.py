from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

# Root route to check if API is running
@app.route("/")
def home():
    return "API is running!", 200

# Example API route
@app.route("/download", methods=["GET"])
def download_file():
    file_path = "example.txt"  # Change this to your actual file path
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404

# Run the app (only needed for local testing)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
