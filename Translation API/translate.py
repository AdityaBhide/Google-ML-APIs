#this is the example of translation api as well as it uses the speech to text api
#The transcribed text from the speech is translated into the 4 languages 
#the 4 languages are -- [french, spanish, russian, hindi]
#if you want you can even change the target languages below


import os
import io
# Imports the Google Cloud client library
from google.cloud import translate

def translate_into(input_text, language):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = input_text
    # The target language
    target = language

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Translation: {}'.format(translation['translatedText']))

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
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
        print(u'Transcript: {}'.format(result.alternatives[0].transcript), '\n')

    re = response.results[0].alternatives[0].transcript
    #You can change the languages here.
    languages = ['fr', 'es', 'ru', 'hi']

    for language in languages:
        translate_into(re, language)

transcribe_file('chicago.flac')




