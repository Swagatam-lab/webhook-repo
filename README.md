Project: webhook-repo
markdown
Copy
Edit
# GitHub Webhook Event Tracker 🚀

This project is a real-time webhook listener and dashboard that receives `push` and `pull_request` events from a GitHub repository, stores them in MongoDB, and displays them on a webpage using Flask.

---

## 📌 Features

- 🔁 Listens for GitHub webhook events (push and pull request)
- 🧠 Stores data in MongoDB Atlas
- 🌐 Displays events on a webpage that updates every 15 seconds
- 🔧 Built with Flask, MongoDB, HTML, and JavaScript
- 🧪 Uses ngrok for public webhook testing

---

## 📂 Project Structure

webhook-repo/
├── app.py # Flask server
├── requirements.txt # Dependencies
├── templates/
│ └── index.html # Frontend HTML

yaml
Copy
Edit

---

## ⚙️ Tech Stack

- **Python 3.11+**
- **Flask**
- **MongoDB Atlas**
- **pymongo**
- **HTML + JS**
- **ngrok**

---

## 🚀 How It Works

1. GitHub sends a webhook to `/webhook` when someone pushes or opens a PR.
2. The Flask app extracts the relevant data and saves it to MongoDB.
3. The frontend (`index.html`) polls the `/events` endpoint every 15 seconds.
4. The latest GitHub events are shown in human-readable format.

---

## 🧪 Testing It Yourself

### 1. Clone and install

```bash
git clone https://github.com/Swagatam-lab/webhook-repo.git
cd webhook-repo
pip install -r requirements.txt
2. Set up MongoDB
Create a MongoDB Atlas cluster

Add IP and database user

Create database: github_webhooks

Create collection: events

Paste your connection string in app.py:

python
Copy
Edit
MONGO_URI = "mongodb+srv://<user>:<password>@cluster.mongodb.net/github_webhooks?retryWrites=true&w=majority"
3. Run the Flask app
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

4. Start ngrok (in a new terminal)
bash
Copy
Edit
ngrok http 5000
Copy the public HTTPS URL.

5. Add GitHub Webhook
Go to any test repo (like action-repo)

Go to Settings → Webhooks → Add Webhook

Payload URL: https://<ngrok-id>.ngrok-free.app/webhook

Content type: application/json

Events: push and pull_request

6. Trigger Events
bash
Copy
Edit
# Simulate a push
echo "test" > test.txt
git add .
git commit -m "Trigger push event"
git push

# Simulate a PR
git checkout -b pr-test
echo "PR" > pr.txt
git add .
git commit -m "PR event"
git push --set-upstream origin pr-test
Open a Pull Request on GitHub.

✅ Your webpage should show new messages like:

vbnet
Copy
Edit
Swagatam pushed to main on Sat, 6 Jul 2025 10:30 AM UTC
Swagatam submitted a pull request from pr-test to main on Sat, 6 Jul 2025 10:31 AM UTC
📸 Demo Screenshot
(Add a screenshot here of the webpage showing events)

📬 Credits
Made with 💻 by Swagatam — learning one webhook at a time!
