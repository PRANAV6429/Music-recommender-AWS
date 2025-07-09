from log_to_dynamodb import log_mood_to_dynamodb
from mood_detect import detect_mood
from flask import Flask, render_template, request
from recommender import recommend_song

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    mood_used = None
    if request.method == "POST":
        user_message = request.form.get("user_message")  # Changed input name
        song_title = request.form.get("song_title") or None

        # If user gives message input → detect mood using AWS Comprehend
        if user_message:
            mood_used, _ = detect_mood(user_message)
            log_mood_to_dynamodb(user_message, mood_used)
        else:
            mood_used = request.form.get("mood")  # Fallback to manual mood (if any)

        recommendations = recommend_song(song_title=song_title, mood=mood_used)

    return render_template("index.html", recommendations=recommendations, mood=mood_used)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
