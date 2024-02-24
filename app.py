from flask import Flask ,jsonify
from pymongo import MongoClient
from flask_cors import CORS
import json
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


app = Flask(__name__)
CORS(app) 

client = MongoClient(MONGO_URI)
db = client["Database"]
collection = db["Data"]


@app.route("/", methods=['GET'])
def get_data():
    try:
        data_from_mongo = list(collection.find({}))
        for item in data_from_mongo:
            item['_id'] = str(item['_id'])
        json_data = jsonify({'data': data_from_mongo})
        return json_data, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
