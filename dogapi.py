n=int(input("Input the number of dog images you want: "))
print("the number of dog images you want is: ", n)
import requests
import json
url="https://dog.ceo/api/breeds/image/random"
print("Here are the urls for", n, "dog images.")
for y in range(n):
    urlresp = requests.get(url).text
    imageurl = json.loads(urlresp)
    print(imageurl['message'])
    r=requests.get(imageurl['message'])
    file="dog"+str(y)+".jpg"
    with open(file,"wb") as img:
        img.write(r.content)
        
        

       
    
    
    
    
    


    

