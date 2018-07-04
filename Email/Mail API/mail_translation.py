import os
import io
# Imports the Google Cloud client library
from google.cloud import translate
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def translate_into(input_text):
    # Instantiates a client
    translate_client = translate.Client()
    email=input("input your Email id : ")
    password=input("Enter your password : ")

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.connect("smtp.gmail.com", 465)
    server.login(email, password)

    fromaddr = email
    toaddr = str(input("Enter the target Email address : "))
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = str(input("Subject : "))

    body = str(input("Input the message : "))
    msg.attach(MIMEText(body, 'plain'))   

    # The text to translate
    text = input_text
    # The target language
    languages = ['fr', 'es', 'ru', 'hi']
    for language in languages:
        target = language

        # Translates some text into language given
        translation = translate_client.translate(
            text,
            target_language=target)
        trans = translation['translatedText']

        filename1 = language+".txt"     
        attachment1 = open(filename1, 'wb')

        attachment1.write(trans.encode('utf-8'))
        attachment1.close()
        
        filename = filename1
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        

    text=msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()                       

    
def transcribe_file(speech_file):
    """Transcribe the  audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file , 'rb') as audio_file:
        content = audio_file.read()
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
    translate_into(re)


transcribe_file('chicago.flac')
