import requests
import os

# fetch the html from a url
req = requests.get('https://clbokea.github.io/exam/assignment_2.html')
text = req.text

img_url_list = [] 

text_list = text.split('img')

def locate_image(e):
    i = e.find('"')

    # cut after  'src="' to end of the img_url  
    img_url = e.split('"')
    img_url = img_url[1]
    img_url_list.append(img_url)

for e in text_list:
    if 'src' in e:
        locate_image(e)

# print(img_url_list)

# Create a src directory for the images
os.mkdir('src')
os.chdir('src')

for i in img_url_list:
    # get the image
    req = requests.get(f'https://clbokea.github.io/exam/{i}', stream=True)

    # write image to file
    with open(i[4:], 'wb') as f:
        for chunk in req:
            f.write(chunk)

os.chdir('..')

with open('index.html', 'w') as f:
    f.write(text)

