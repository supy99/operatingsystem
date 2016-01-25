import os
import sys
import plugins
from control import *

def _initialise():
    plugins.register_admin_command(['restart'])

def restart(bot, event, *args):
    os.execl(sys.executable, sys.executable, *sys.argv)
    msg = _('Bot has been restarted')
    yield from bot.coro_send_message(CONTROL, msg)
