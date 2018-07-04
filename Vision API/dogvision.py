import io
import os
from google.cloud import vision
from google.cloud.vision import types
import requests
import json

n=int(input("Input the number of dog images you want: "))
print("the number of dog images you want is: ", n)
url="https://dog.ceo/api/breeds/image/random"
print("Here are the urls for", n, "dog images.")
    
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with open(path,'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
        
for y in range(n):
    urlresp = requests.get(url).text
    imageurl = json.loads(urlresp)
    print(imageurl['message'])
    r=requests.get(imageurl['message'])
    file="dog"+str(y)+".jpg"
    with open(file,"wb") as img:
        img.write(r.content)    
    detect_labels("dog"+str(y)+".jpg")

