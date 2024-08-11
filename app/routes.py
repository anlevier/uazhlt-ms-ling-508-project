from flask import Flask, jsonify, request
from flask_cors import CORS
import praw
import re
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

@app.route('/get_comments', methods=['POST'])
def get_comments():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    try:
        match = re.search(r'/comments/([a-zA-Z0-9_]+)/', url)
        if match:
            submission_id = match.group(1)
        else:
            return jsonify({"error": "Invalid URL format"}), 400

        submission = reddit.submission(id=submission_id)
        top_level_comments = [comment.body for comment in submission.comments if not isinstance(comment, praw.models.MoreComments)]

        return jsonify(top_level_comments)

    except (praw.exceptions.RedditAPIException, Exception) as e:
        print(f"Error retrieving comments: {str(e)}")
        return jsonify({"error": f"Error retrieving comments: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)