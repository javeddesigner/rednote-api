import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RedNote API is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's default port
    app.run(host="0.0.0.0", port=port)
