from flask import Flask, request, jsonify
import requests
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

def extract_video_url(post_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(post_url, headers=headers)
        response.raise_for_status()
        
        video_url_match = re.search(r'"videoUrl":"(https:[^"]+)', response.text)
        
        if video_url_match:
            return video_url_match.group(1)
        else:
            return None
    except Exception as e:
        return None

@app.route('/')
def home():
    return 'RedNote Video Downloader API is running!'

@app.route('/download', methods=['GET'])
def download():
    post_url = request.args.get('url')
    if not post_url:
        return jsonify({"success": False, "error": "No URL provided"}), 400
    
    video_url = extract_video_url(post_url)
    if video_url:
        return jsonify({"success": True, "download_link": video_url})
    else:
        return jsonify({"success": False, "error": "Failed to extract video URL"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
