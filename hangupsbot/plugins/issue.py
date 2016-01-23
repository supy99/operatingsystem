import json
import requests
import plugins
from ghinfo import *
from links import *
from control import *

def _initialise():
    plugins.register_admin_command(['issue', 'commit'])

def commit(bot, event, *args):
    '''Get the latest commit'''
    try:
        url = 'https://api.github.com/repos/{}/{}/git/refs/heads/master'.format(REPO_OWNER, REPO_NAME)
        get = requests.get(url)
        data = json.loads(get.text)
        commiturl = data[u'object'][u'url']
        getcommit = requests.get(commiturl)
        commitdata = json.loads(getcommit.text)
        link = shorten(str(commitdata[u'html_url']))
        committer = str(commitdata[u'committer'][u'name'])
        date = str(commitdata[u'committer'][u'date'])
        message = str(commitdata[u'message'])
        msg = _('The last commit was {} by {} at {}<br>{}').format(message, committer, date, link)
        yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        msg = _('{} -- {}').format(e, event.text)
        simple = _('An Error Occurred. Please Try Again Later')
        yield from bot.coro_send_message(event.conv, simple)
        yield from bot.coro_send_message(CONTROL, msg)

def issue(bot, event, *args):
    '''Create an issue on github.com using the given parameters.'''
    try:
        if args:
            url = 'https://api.github.com/repos/{}/{}/issues'.format(REPO_OWNER, REPO_NAME)
            
            if str(args[0]).isdigit():
                try:
                    get = requests.get(url)
                    data = json.loads(get.text)
                    num = int(args[0]) * -1
                    link = shorten(str(data[num][u'html_url']))
                    title = str(data[num][u'title'])
                    msg = _('{} -- {}').format(title, link)
                except:
                    msg = _('Invalid Issue Number')
            else:
                session = requests.Session()
                session.auth=(USERNAME, PASSWORD)
                # Create our issue
                issue = {'title': ' '.join(args),
                         'body': 'Issue created by {}'.format(event.user.full_name)}
                # Add the issue to our repository
                get = requests.get(url)
                data = json.loads(get.text)
                r = session.post(url, json.dumps(issue))
                link = shorten(str(data[0][u'html_url']))
                if r.status_code == 201:
                    msg = _('Successfully created issue: {}').format(link)
                else:
                    msg = _('Could not create issue.<br>Response: {}').format(r.content)

        else:
            msg = _('No issue given.')
        yield from bot.coro_send_message(event.conv, msg)
    except BaseException as e:
        msg = _('{} -- {}').format(str(e), event.text)
        yield from bot.coro_send_message(CONTROL, msg)
