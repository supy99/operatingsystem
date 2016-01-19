from urllib.request import urlopen

import plugins

def _initialise():
    plugins.register_user_command(['joke'])
def escape(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
            ('"', ' \\xe2\\x80\\x9c'),
            ('"', '\\xe2\\x80\\x9d'),
            ("'", '\\xe2\\x80\\x99')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def joke(bot, event, *args):
    if not args:
        request = urlopen('http://www.ajokeaday.com/jokes/random')
        html = request.read()
        html = str(html)
        jokesplit = html.split('<p style="margin-bottom:20px;">')
        jokehalf = jokesplit[1]
        joke1 = jokehalf.split('</p>')
        joke = joke1[0]
        joke = joke.strip('\\r\\n')
        joke = joke.strip(' ')
        joke = escape(joke)
        jokelist = list(joke)
        for i in range(len(jokelist)):
            if jokelist[i] == '\\' and (jokelist[i+1] == 'r' or jokelist[i+1] == 'n'):
                jokelist[i] = ''
                jokelist[i+1] = ''
        jokelist[-1] = ''
        jokelist[-2] = ''
        jokelist[-3] = ''
        jokelist[-4] = ''
        joke = ''.join(jokelist)
        joke = bytes(joke, 'utf8')
        joke = joke.decode('utf8')
        msg = _('{}').format(joke)
    else:
        msg = _('<i>Too many parameters.</i>')
    yield from bot.coro_send_message(event.conv, msg)

