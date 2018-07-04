#In this program you have to input an audio speech file and the api will transcribe the speech to text 
#The output will be printed in text
#IMPORTANT : You will have to convert your .p3 file into .flac 
#You can use this link for conversion of .mp3 to .flac --- "ttps://audio.online-convert.com/convert-to-flac"

import os
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    client = speech.SpeechClient()

    with io.open(speech_file , 'rb') as audio_file:
        content = audio_file.read()
        print(audio_file)
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

    re=response.results[0].alternatives[0].transcript
    print(re)
    

#here you put the audio file with extension .flac
transcribe_file('filename.flac')
