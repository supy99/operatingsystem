import plugins, re
from control import *
from requests import get
from bs4 import BeautifulSoup
from apikeys import lyricsnmusic as key

def _initialise():
    plugins.register_user_command(["lyrics"])

def lyrics(bot, event, *args):
        payload = {'apikey': key, 'q': str(args)}
        r = get('http://api.lyricsnmusic.com/songs', params=payload)
        url = r.json()[0]['url']
        lyrics = BeautifulSoup(get(url).text, 'html.parser')
        msg = _(lyrics.pre.string)
        yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        simple = _("Lyrics not found")
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL,msg)


    
