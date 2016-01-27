from urllib.request import urlopen as get
from bs4 import BeautifulSoup as soup
import plugins
from control import *

def getlyrics(title, artist):
        joinedartist = ''.join(artist.split())
        url = 'http://www.azlyrics.com/lyrics/' + joinedartist + '/' + title + '.html'
        r = get(url)
        html = r.read()
        nice = soup(html, 'html.parser')
        text = nice.get_text()
        lyr = text.split(artist.upper() + ' LYRICS')[2]
        lyrics = lyr.split('Submit Corrections')[0]
        return lyrics.strip()

def _initialise():
	plugins.register_user_command(['lyrics'])

def lyrics(bot, event, *args):
	try:
		message = ' '.join(args)
		title = message.split(' by ')[0]
		title = ''.join(title.split())
		artist = message.split(' by ')[1]
		g = getlyrics(title, artist)
		msg = _(g)
		yield from bot.coro_send_message(event.conv, msg)
	except BaseException as e:
		simple = _('The correct format is /bot lyrics <title> by <artist>')
		msg = _('{} -- {}').format(str(e), event.text)
		yield from bot.coro_send_message(event.conv, simple)
		yield from bot.coro_send_message(CONTROL, msg)
