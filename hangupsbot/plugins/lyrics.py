import plugins, re

from urllib.request import urlopen

def _initialise():
    plugins.register_user_command(["lyrics"])

def lyrics(bot, event, *args):
    info = ' '.join(args).split(' by ')
    if len(info) == 2:
        songname  = str(info[0]).lower().split()
        songs = ''.join(songname)
        namelist = list(songs)
        for i in range(len(namelist)):
            if namelist[i] == "'":
                namelist[i] = ''
            else:
                namelist[i] = namelist[i]
        song = ''.join(namelist)
        artistname = str(info[1]).lower().split()
        artist = ''.join(e for e in artistname if e.isalnum())
        response = urlopen('http://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html')
        html = str(response.read())
        list1 = re.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', html)
        lyr = str(list1[1])
        lyr = re.split('</div>', lyr)
        lyrics1 = lyr[0]
        charlist1 = list(lyrics1)
        for i in range(len(charlist1)):
            if charlist1[i] == '\\':
                charlist1[i] = ''
            else:
                charlist1[i] = charlist1[i]
        lyrics2 = ''.join(charlist1)
        charlist2 = list(lyrics2)
        for i in range(len(charlist2)):
            if charlist2[i] == 'r' and charlist2[i+1] == 'n':
                charlist2[i] = ''
                charlist2[i+1] = ''
            elif charlist2[i] == '>' and charlist2[i+1] == 'n':
                charlist2[i] = '>'
                charlist2[i+1] = ''
            else:
                charlist2[i] = charlist2[i]
        charlist2[-1] = ''
        lyricstoshow = ''.join(charlist2)
        msg = _('{}').format(lyricstoshow)
    else:
        msg = _('The correct format for this command is ! lyrics <song name> by <artist>')
    yield from bot.coro_send_message(event.conv, msg)


    
