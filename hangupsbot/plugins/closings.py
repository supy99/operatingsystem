import plugins
import json
from requests import get
from control import *
import asyncio

def _initialise():
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