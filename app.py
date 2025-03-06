import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    filename = url.split("/")[-1]  # Extract filename from URL
    filepath = os.path.join("downloads", filename)  # Save in 'downloads' folder

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        os.makedirs("downloads", exist_ok=True)  # Ensure folder exists

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        return jsonify({"message": "Download successful", "filepath": filepath})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
