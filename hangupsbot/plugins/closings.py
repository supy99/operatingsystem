import plugins
import json
from requests import get
from control import *
from bs4 import BeautifulSoup
import asyncio

def _initialise():
    plugins.register_user_command(['fcps', 'lcps'])
    plugins.register_handler(_fcps, type="message")
    plugins.register_handler(_lcps, type="message")


def checklcps():    
    try:
        r = get('http://www.nbcwashington.com/weather/school-closings/')
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        schools = []
        for school in soup.find_all('p'):
            schools.append(school.text)

        for i in range(len(schools)):
            if 'Loudoun County' in schools[i]:
                check = str(schools[i])
        status = check.replace('Loudoun County Schools', '')
        msg = _('LCPS is {}').format(status)
        return {'message': msg,
                'simple': ''}
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)
        return {'message': msg,
                'simple': simple}
    

def checkfcps():
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
        return {'message':msg,
                'simple': ''}
    except BaseException as e:
        simple = _('An Error Occurred')
        msg = _('{} -- {}').format(str(e), event.text)
        return {'message':msg,
                'simple': simple}
@asyncio.coroutine
def _fcps(bot, event, command):
    tbc = ['fcps', 'fairfax', 'ffx']
    if any(term in event.text.lower() for term in tbc):
        check = checkfcps()
        if check['simple'] == '':
            yield from bot.coro_send_message(event.conv, check['message'])
        else:
            yield from bot.coro_send_message(event.conv, check['simple'])
            yield from bot.coro_send_message(CONTROL, check['message'])

@asyncio.coroutine
def _lcps(bot, event, command):
    tbc = ['lcps', 'loudoun']
    if any(term in event.text.lower() for term in tbc):
        check = checklcps()
        if check['simple'] == '':
            yield from bot.coro_send_message(event.conv, check['message'])
        else:
            yield from bot.coro_send_message(event.conv, check['simple'])
            yield from bot.coro_send_message(CONTROL, check['message'])

def fcps(bot, event, *args):
    '''This command checks for school closings in the Loudon County Public Schools area. Data taken from NBC.'''
    check = checkfcps()
    if check['simple'] == '':
        yield from bot.coro_send_message(event.conv, check['message'])
    else:
        yield from bot.coro_send_message(event.conv, check['simple'])
        yield from bot.coro_send_message(CONTROL, check['message'])

def fcps(bot, event, *args):
    '''This command checks for closings in the Fairfax County Public Schools Area. Data taken from TJHSST.'''
    check = checklcps()
    if check['simple'] == '':
        yield from bot.coro_send_message(event.conv, check['message'])
    else:
        yield from bot.coro_send_message(event.conv, check['simple'])
        yield from bot.coro_send_message(CONTROL, check['message'])