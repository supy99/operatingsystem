from bs4 import BeautifulSoup as BS

from urllib.request import urlopen

def shorten(url):
    try:
        response = urlopen('http://tinyurl.com/api-create.php?url=' + url)
        html = response.read()
        soup = BS(html, 'html.parser')
        return soup.get_text()
    except:
        error = "Could not create shortened link"
        return error

def get_title(url):
    try:
        response = urlopen(url)
        html = response.read()
        soup = BS(html, 'html.parser')
        return soup.title.string
    except:
        error = "Unable to open url :("
        return error
