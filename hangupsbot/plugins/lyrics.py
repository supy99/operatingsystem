import plugins, re
from control import *
from requests import get
from bs4 import BeautifulSoup
from apikeys import lyricsnmusic as key

def _initialise():
    plugins.register_user_command(["lyrics"])

def lyrics(bot, event, *args):
    '''get lyrics from lyricsnmusic.com. THIS IS NOT PERFECT EVERY TIME. Format is /bot lyrics <song>'''
    try:
        payload = {'apikey': key, 'q': str(args)}
        r = get('http://api.lyricsnmusic.com/songs', params=payload)
        info = r.json()[0]
        lyrics = BeautifulSoup(get(info['url']).text, 'html.parser')
        msg[0] = _('<b>Title: </b>{}, <b>Artist: </b>{}').format(
            info['title'], info['artist']['name'])
        msg[1] = _(lyrics.pre.string)
        yield from bot.coro_send_message(event.conv, msg[0])
        yield from bot.coro_send_message(event.conv, msg[1])
    except BaseException as e:
        simple = _("Lyrics not found")
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL,msg)
