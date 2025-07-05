# app.py

from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from datetime import datetime, timezone

# Create a Flask app
app = Flask(__name__)

# Connect to MongoDB
MONGO_URI = "mongodb+srv://swagatam:Swagatam%402025@cluster0.vqlborh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["github_webhooks"]
collection = db["events"]

# Route for homepage - shows webpage
@app.route('/')
def home():
    return render_template("index.html")

# Route to return event data to frontend
@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))  # latest 10
    for event in events:
        event["_id"] = str(event["_id"])  # convert Mongo ID to string
    return jsonify(events)

# Route for GitHub webhook (only POST)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    # Handle push events
    if event_type == "push":
        event = {
            "author": data["pusher"]["name"],
            "type": "push",
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": datetime.now(timezone.utc)
        }

    # Handle pull request events
    elif event_type == "pull_request":
        pr = data["pull_request"]
        event = {
            "author": pr["user"]["login"],
            "type": "pull_request",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": datetime.now(timezone.utc)
        }

    else:
        return "Event type not supported", 200

    # Save event to MongoDB
    collection.insert_one(event)
    return "Event received!", 200

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
