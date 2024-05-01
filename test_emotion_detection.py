import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def text_emotion_detector(self):
        resultJoy = emotion_detector('I am glad this happened')
        self.assertEqual(resultJoy['dominant_emotion'], 'joy')
        
        resultAnger = emotion_detector('I am really mad about this')
        self.assertEqual(resultAnger['dominant_emotion'], 'anger')
        
        resultDisgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(resultDisgust['dominant_emotion'], 'disgust')
        
        resultSadness = emotion_detector('I am so sad about this')
        self.assertEqual(resultSadness['dominant_emotion'], 'sadness')
        
        resultFear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(resultFear['dominant_emotion'], 'fear')

unittest.main()