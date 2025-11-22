import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 10000))
    debug = os.environ.get("DEBUG", "True").lower() == "true"
    
    app.run(host=host, port=port, debug=debug)
