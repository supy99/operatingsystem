from apikeys import google, cx
from requests import get
import json

def search(term):
	r = get('https://www.googleapis.com/customsearch/v1', params={'key': google, 'cx': cx, 'q': term})
	data = json.loads(r.text)
	url = data['items'][0]['link']
	return url

print(search('Apple'))
