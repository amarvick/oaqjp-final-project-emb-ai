import requests
import json

def get_dominant_emotion(emotions_response):
    dominant_emotion = None
    dominant_emotion_score = 0

    for emotion, score in emotions_response.items():
        if (score > dominant_emotion_score):
            dominant_emotion = emotion
            dominant_emotion_score = score
    
    return dominant_emotion

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        print(get_dominant_emotion(emotions))
        return emotions
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")