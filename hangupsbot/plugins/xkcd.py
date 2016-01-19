"""
Identify images, upload them to google plus, post in hangouts
"""

import aiohttp, asyncio, io, logging, os, re

import plugins

from links import *

from random import choice as choose

import pykcd

logger = logging.getLogger(__name__)


def _initialise():
    plugins.register_user_command(["xkcd"])


def xkcd(bot, event, *args):
    # Don't handle events caused by the bot himself
    numlist =  list(range(1, 1631))
    if args:
        msg = _("Please don't enter any arguments")
        yield from bot.coro_send_message(event.conv, msg)
    else:
        chosencomic = choose(numlist)
        chosennum = int(chosencomic)
        link_image = str(pykcd.XKCDStrip(chosennum).image_link)

        logger.info("getting {}".format(link_image))
        filename = os.path.basename(link_image)
        r = yield from aiohttp.request('get', link_image)
        raw = yield from r.read()
        image_data = io.BytesIO(raw)
        link = shorten(link_image)
        image_id = yield from bot._client.upload_image(image_data, filename=filename)
        yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
        yield from bot.coro_send_message(event.conv, _('{}').format(link))
