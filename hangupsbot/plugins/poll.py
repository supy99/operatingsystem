import plugins
from control import *

def _initialize():
    plugins.register_admin_command(["poll"])
    plugins.register_user_command(["vote", "results"])

def poll(bot, event, *args):
    '''Creates a poll. Format is /bot poll <name>'''
    try:
        if not bot.memory.exists(['polls']):
                bot.memory.set_by_path(['polls'], {})
        if args:
            name = ' '.join(args)
            bot.memory.set_by_path(['polls', name], {})
            bot.memory.save()
            msg = _("Poll '{}' created").format(name)
        else:
            msg = _("What is this poll called?")
        yield from bot.coro_send_message(event.conv, msg)
        bot.memory.save()
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, msg)

def vote(bot, event, *args):
    '''Retrieves quote from bot's memory. Format is /bot quote <person>'''
    try:
        spl = ' '.join(args).split(' - ')
        if len(spl) == 2:  
            vote = spl[0]
            poll = spl[1]
            path = bot.memory.get_by_path(['polls', poll])
            path[event.user.first_name] = vote
            bot.memory.set_by_path(['polls', poll], path)
            bot.memory.save()
            msg = _('Your vote for {} has been recorded as {}').format(poll, vote)
        else:
            msg = _("The correct format is /bot vote <vote> - <poll>")
        yield from bot.coro_send_message(event.conv, msg)
    except:
        simple = _('An Error Occurred')
        msg = _("{} -- {}").format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, msg)

def results(bot, event, *args):
    '''    try:'''
    poll = ' '.join(args)
    votes = []
    names = []
    msg = []
    path = bot.memory.get_by_path(["polls", poll])
    for person in path:
        spl = person.split(':')
        name = spl[0]
        vote = spl[1]
        names.append(name)
        votes.append(vote)
    [str(name) for name in names]
    [str(vote) for vote in votes]
    for i in range(len(names)):
        result = '{} voted {}<br>'.format(names[i], votes[i])
        msg.append(result)
    final = ''.join(msg)
    yield from bot.coro_send_message(event.conv, final)
    '''    except BaseException as e:
        simple = _('Either an error occurred or there is no poll by that name')
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, msg)'''






