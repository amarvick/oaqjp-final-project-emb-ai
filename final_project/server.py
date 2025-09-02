""" Main server file """
import requests
from flask import Flask
from final_project.EmotionDetection import get_dominant_emotion, emotion_detector


app = Flask(__name__)

@app.route('/emotionDetector/', defaults={'statement': None})
def get_emotions_str(statement):
    """ Server call to get emotion score """
    if not statement or not isinstance(statement, str):
        return "<b>Invalid text! Please try again!</b>"

    try:
        emotions = emotion_detector(statement)
        dominant_emotion = get_dominant_emotion(emotions)

        if dominant_emotion is None:
            return "<b>Invalid text! Please try again!</b>"

    except requests.exceptions.RequestException as e:
        return f"<b>Failed to analyze emotions/dominant emotion: {e}</b>"

    emotions_str = 'For the given statement, the system response is '
    for emotion, score in emotions.items():
        emotions_str += f" '{emotion}': {score},"
    emotions_str += f'. The dominant emotion is <b>{dominant_emotion}</b>'

    return emotions_str

if __name__ == "__main__":
    app.run(debug=True)
