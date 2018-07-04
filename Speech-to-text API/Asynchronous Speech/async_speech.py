import io
import os
# [START def_transcribe_file]
def transcribe_file(speech_file):

    """Transcribe the given audio file asynchronously."""

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    client = speech.SpeechClient()
    # [START migration_async_request]

    with io.open(speech_file ,'rb') as audio_file:
        content = audio_file.read()
        print(audio_file)
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')
    
    # [START migration_async_response]
    operation = client.long_running_recognize(config, audio)

    # [END migration_async_request]
    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript:{}'.format(result.alternatives[0].transcript))
        print('Confidence:{}'.format(result.alternatives[0].confidence))

    # [END migration_async_response]

    # [END def_transcribe_file]


transcribe_file('speech.flac')

