from final_project.EmotionDetection import get_dominant_emotion, emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_get_dominant_emotion_joy(self):
        emotions_joy = emotion_detector("I am glad this happened")
        dominant_emotion_joy = get_dominant_emotion(emotions_joy)
        self.assertEqual(dominant_emotion_joy, "joy")
        
    def test_get_dominant_emotion_anger(self):
        emotions_anger = emotion_detector("I am really mad about this")
        dominant_emotion_anger = get_dominant_emotion(emotions_anger)
        self.assertEqual(dominant_emotion_anger, "anger")
        
    def test_get_dominant_emotion_disgust(self):
        emotions_disgust = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion_disgust = get_dominant_emotion(emotions_disgust)
        self.assertEqual(dominant_emotion_disgust, "disgust")
        
    def test_get_dominant_emotion_sadness(self):
        emotions_sadness = emotion_detector("I am so sad about this")
        dominant_emotion_sadness = get_dominant_emotion(emotions_sadness)
        self.assertEqual(dominant_emotion_sadness, "sadness")
        
    def test_get_dominant_emotion_fear(self):
        emotions_fear = emotion_detector("I am really afraid that this will happen")
        dominant_emotion_fear = get_dominant_emotion(emotions_fear)
        self.assertEqual(dominant_emotion_fear, "fear")

if __name__ == '__main__':
    unittest.main()