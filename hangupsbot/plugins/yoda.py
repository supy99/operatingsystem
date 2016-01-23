from urllib.request import Request, urlopen
from urllib.parse import quote_plus
import plugins

def _initialise():
    plugins.register_user_command(["yoda"])

def yoda(bot, event, *args):
    if args:
        tbc = ' '.join(args)
        converted = convert(tbc)
        msg = _("{}").format(converted)
    else:
        msg = _("What should yoda say?")
    yield from bot.coro_send_message(event.conv, msg)

def convert(input):
    sentence = quote_plus(input)
    q = Request('https://yoda.p.mashape.com/yoda?sentence=' + sentence)
    q.add_header('X-Mashape-Key', 'bpQPLI22xemshjIJyMtbRDcO40Fvp1WHIK5jsn5XpZPqPaASfk')
    q.add_header('Accept', 'text/plain')
    a = urlopen(q).read()
    b = list(a)
    b = [chr(x) for x in b]
    a = ''.join(b)
    return a
