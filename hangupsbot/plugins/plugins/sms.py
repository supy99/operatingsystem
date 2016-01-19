import plugins
from twilio.rest import TwilioRestClient
import re
from datetime import datetime
 # Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3bc352093340df8777d4f1557428f77a"
auth_token  = "c7e244d7d16d2e83c11ecfb757f7ddcf"
client = TwilioRestClient(account_sid, auth_token)

def _initialise():
    plugins.register_admin_command(['sms'])

def sms(bot, event, *args):
    argstr = ' '.join(args)
    listargs = argstr.split('to')
    num = listargs[1]
    num = re.findall('\d+', num)
    num = ''.join(num)
    bodytosend = listargs[0]
    message = client.messages.create(body= bodytosend,
        to= "+1" + num,    # Replace with your phone number
        from_="+12406075336") # Replace with your Twilio number
    msg = _("Message sent to {}").format(num)
    yield from bot.coro_send_message(event.conv, msg)
