import sys
import csv
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

print("Choose a movie \n 1-Avengers Infinity war \n 2-Deadpool 2 \n 3-Jurassic park Fallen Kingdom")
x=int(input("Input : "))
print("Here are the reviews of this movie : ")

print("\nAnalyzing the given reviews...\n")

def entity_sentiment_text(text):
    """Detects entity sentiment in the provided text."""
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))


with open('reviews-input.csv', newline='') as f:
    reader=csv.DictReader(f)
    data=[r for r in reader]
    review=data[x-1]['Reviews']
    print(review)

if x==1:
    entity_sentiment_text(review)
elif x==2:
    entity_sentiment_text(review)
elif x==3:
    entity_sentiment_text(review)













