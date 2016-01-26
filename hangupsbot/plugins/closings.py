import plugins
import json
from requests import get
from control import *
import asyncio

def _initialise():
    plugins.register_user_command(['fcps'])
    plugins.register_handler(_fcps, type="message")
    plugins.register_handler(_lcps, type="message")


def checklcps():    
    page = get('http://wogloms.com/closings/status.php')
    data = json.loads(page.text)
    status = data['Loudoun']
    return status
    

def checkfcps():
    page = get('http://wogloms.com/closings/status.php')
    data = json.loads(page.text)
    status = data['Fairfax']
    return status

def fcps(bot, event, *args):
    '''This command checks for closings in the Fairfax County Public Schools Area. Data taken from TJHSST.'''
    try:
        page = get('https://ion.tjhsst.edu/api/emerg?format=json')
        data = json.loads(page.text)
        status = data['status']
        if status:
            message = data['message']
            message = message.replace('<p>', '')
            message = message.replace('</p>', '')
            msg = _(message)
        else:
            msg = _('FCPS is open')
        yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, msg)

@asyncio.coroutine
def _fcps(bot, event, command):
    try:
        tbc = ['fcps', 'fairfax', 'ffx']
        if any(term in event.text.lower() for term in tbc):
            check = checkfcps()
            msg = _('FCPS Is Currently <b>{}<b>').format(check.upper())
            yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)    
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, message)

@asyncio.coroutine
def _lcps(bot, event, command):
    try:
        tbc = ['lcps', 'loudoun']
        if any(term in event.text.lower() for term in tbc):
            check = checklcps()
            msg = _('LCPS Is Currently <b>{}<b>').format(check.upper())
            yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)    
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, message)