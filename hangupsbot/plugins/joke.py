from requests import get
import plugins

#def _initialize():
    #plugins.register_user_command(['joke'])

def joke(bot, event, *args):
    x = get('http://tambal.azurewebsites.net/joke/random').json()
    joke = x["joke"]
    if len(args) == 0:
        msg = _('{}').format(joke)
    else:
        msg = _('<i>Too many parameters')
    yield from bot.coro_send_message(event.conv, msg)

