from urllib.request import urlopen as get
from bs4 import BeautifulSoup as soup
import plugins
from control import *

def getlyrics(title, artist):
	url = 'http://www.azlyrics.com/lyrics/' + artist + '/' + title + '.html'
	r = get(url)
	html = r.read()
	nice = soup(html, 'html.parser')
	text = nice.get_text()
	newartist = artist.upper()
	tosplit = newartist + " LYRICS"
	lyr = text.split(tosplit)
	lyrics = lyr[2]
	lyrics_ = lyrics.split('Submit Corrections')
	final = lyrics_[0]
	return final

def _initialise():
	plugins.register_admin_command(['testlyrics'])

def testlyrics(bot, event, *args):
	message = ' '.join(args)
	title = message.split(' by ')[0]
	artist = message.split(' by ')[1]
	g = getlyrics(title, artist)
	msg = _(g)
	yield from bot.coro_send_message(CONTROL, msg)
