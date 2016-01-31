import plugins
from apikeys import cx, google
from links import shorten
from control import *
import json
from requests import get
import traceback

from urllib.parse import quote
def _initialise():
    plugins.register_user_command(['lmgtfy', 'google', 'g'])

def search(term):
    r = get('https://www.googleapis.com/customsearch/v1', params={'key': google, 'cx': cx, 'q': term})
    data = json.loads(r.text)
    link = shorten(data['items'][0]['link'])
    return link

def google(bot, event, *args):
    try:
        if args:
            s = search(' '.join(args))
            msg = _('I searched Google and got {}').format(s)
        else:
            msg = _('What should I ask Google to answer?')
        yield from bot.coro_send_message(event.conv, msg)
    except:
        tb = traceback.format_exc()
        msg = _('{} -- {}').format(tb, event.text)
        yield from bot.coro_send_message(CONTROL, msg)
        yield from bot.coro_send_message(event.conv, _('An Error Occured'))


def g(bot, event, *args):
    try:
        if args:
            s = search(' '.join(args))
            msg = _('I searched Google and got {}').format(s)
        else:
            msg = _('What should I ask Google to answer?')
        yield from bot.coro_send_message(event.conv, msg)
    except:
        tb = traceback.format_exc()
        msg = _('{} -- {}').format(tb, event.text)
        yield from bot.coro_send_message(CONTROL, msg)
        yield from bot.coro_send_message(event.conv, _('An Error Occured'))

def lmgtfy(bot, event, *args):
    '''Returns an lmgtfy link from http://lmgtfy.com/ Format is /bot lmgtfy <what to google>'''
    try:
        if args:
            query = ' '.join(args)
            search = quote(query)
            url = 'http://lmgtfy.com/?q=' + search
            msg = _('{}').format(shorten(url))
        else:
            msg = _('{}').format(shorten('http://lmgtfy.com/?q=urbandictionary%20dolphin'))
        yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(CONTROL, msg)
