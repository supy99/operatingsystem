import json
import requests
import plugins
from ghinfo import *

def _initialise():
    plugins.register_admin_command(['issue'])

def issue(bot, event, *args):
    '''Create an issue on github.com using the given parameters.'''
    if args: 
        # Our url to create issues via POST
        url = 'https://api.github.com/repos/{}/{}/issues'.format(REPO_OWNER, REPO_NAME)
        # Create an authenticated session to create the issue
        session = requests.Session()
        session.auth=(USERNAME, PASSWORD)
        # Create our issue
        issue = {'title': ' '.join(args),
                 'body': 'Issue created by {}'.format(event.user.full_name)}
        # Add the issue to our repository
        r = session.post(url, json.dumps(issue))
        if r.status_code == 201:
            msg = _('Successfully created issue')
        else:
            msg = _('Could not create issue.<br>Response: {}').format(r.content)
    else:
        msg = _('No issue given.')
    yield from bot.coro_send_message(event.conv, msg)
