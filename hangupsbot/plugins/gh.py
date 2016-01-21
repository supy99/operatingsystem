import plugins

from links import *

def _initialise():
    plugins.register_user_command(['gh' , 'source'])

def gh(bot, event, *args):
    url = 'https://github.com/2019okulkarn/sodabot'
    short = shorten(url)
    title = get_title(url)
    msg = _('** {} ** - {}').format(title, short)
    yield from bot.coro_send_message(event.conv, msg)

def source(bot, event, *args):
    url = 'https://github.com/2019okulkarn/sodabot'
    short = shorten(url)
    title = get_title(url)
    msg = _('** {} ** - {}').format(title, short)
    yield from bot.coro_send_message(event.conv, msg)
