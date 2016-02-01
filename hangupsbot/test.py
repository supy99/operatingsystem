from apikeys import image, gapi
from requests import get
import json
def imagesearch(term):
    r = get('https://www.googleapis.com/customsearch/v1', params={'key': gapi, 'cx': image, 'q': term, 'defaultToImageSearch': 'True'})
    data = json.loads(r.text)
    if 'items' not in data:
        return 'No Images Found'
    else:
        link = data['items'][0]['pagemap']['cse_image'][0]['src']
        return link
print(imagesearch('atari'))

