import plugins

from links import shorten
from control import *

from urllib.parse import quote
def _initialise():
    plugins.register_user_command(['lmgtfy'])

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
