from requests import get
import plugins

def _initialise():
    plugins.register_user_command(['wtf'])

def wtf(bot, event, *args):
    wtftext = ' '.join(args)
    try:
        text = get('http://abbreviations.yourdictionary.com/articles/list-of-commonly-used-abbreviations.html').text
        first = text.split('Abbreviations</a>')[1]
        second = text.split('<div class="twelve')[0]
        wtf = second.split('<li>')
        for i in range(len(wtf)):
            if wtftext in wtf[i]:
                item = wtf[i]
        item = item.replace('&ndash;','-')
        msg = _('{}').format(item[:-5])
    except:
        msg = _("Not Found")
    yield from bot.coro_send_message(event.conv, msg)


        
