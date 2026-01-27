from flask import Flask, request
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


app = Flask(__name__)
CORS(app)

# Load model once at startup
model_name = 'facebook/bart-large-cnn'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    try:
        video_id = url.split('=')[1]
    except IndexError:
        return 'Invalid YouTube URL', 400
    try:
        transcript = get_transcript(video_id)
    except Exception as e:
        return f'Could not get transcript: {str(e)}', 400
    try:
        summary = get_summary(transcript)
        return summary, 200
    except Exception as e:
        return f'Could not generate summary: {str(e)}', 500



def get_transcript(video_id):
    api = YouTubeTranscriptApi()
    transcript_data = api.fetch(video_id)
    transcript = ' '.join([snippet.text for snippet in transcript_data.snippets])
    return transcript



def get_summary(transcript):
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        chunk = transcript[i*1000:(i+1)*1000]
        if not chunk.strip():
            continue
        inputs = tokenizer(chunk, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=10)
        summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summary += summary_text + ' '
    return summary

if __name__ == '__main__':
    app.run()

