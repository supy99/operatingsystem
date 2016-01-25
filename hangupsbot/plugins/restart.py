import os
import sys
import plugins

def _initialise():
    plugins.register_admin_command(['restart'])

def restart(bot, event, *args):
    os.execl(sys.executable, sys.executable, *sys.argv)
