import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    emotion_index = 0

    analyzed_emotions = {
        'anger': formatted_response['emotionPredictions'][emotion_index]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][emotion_index]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][emotion_index]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][emotion_index]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][emotion_index]['emotion']['sadness'],
        'dominant_emotion': max(formatted_response['emotionPredictions'][emotion_index]['emotion'], key=formatted_response['emotionPredictions'][emotion_index]['emotion'].get),
    }

    print(json.dumps(analyzed_emotions, indent = 4))
    return(analyzed_emotions)