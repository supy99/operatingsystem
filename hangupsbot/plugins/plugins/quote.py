import asyncio, logging, re

from random import choice

import plugins

logger = logging.getLogger(__name__)

def _initialize():
    plugins.register_admin_command(["addquote"])
    plugins.register_user_command(["quote"])

def addquote(bot, event, *args):
    if args:
        quote = ' '.join(args).split(' - ')
        user = quote[1]
        if not bot.memory.exists([user]):
            bot.memory.set_by_path([user], {})
        quotetoadd = quote[0]
        bot.memory.set_by_path([user], quotetoadd)
        msg = _("User memory created and quote for {} added").format(user)   
        quotetoadd = quote[0]
        bot.memory.set_by_path([user], quotetoadd)
        bot.memory.save()
        msg = _("New quote for {}").format(user)
    else:
        msg = _("Please give me a quote to add")
    yield from bot.coro_send_message(event.conv, msg)
    bot.memory.save()

def quote(bot, event, *args):
    if args:
        user = ' '.join(args)
        listofquotes = bot.memory.get_by_path([user])
        msg = _("\"{}\" - {}").format(listofquotes, user)
    else:
        msg = _("Incorrect number of arguments")
    yield from bot.coro_send_message(event.conv, msg)


