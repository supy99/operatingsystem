import plugins

def _initialise():
    plugins.register_admin_command(["spam"])

def spam(bot, event, *args):
    if args:
        message = ' '.join(args)
        msg = _("{}").format(message)
    else:
        msg = _("spam")
    for i in range(50):
        yield from bot.coro_send_message(event.conv, msg)

