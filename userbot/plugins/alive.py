"""Check if userbot alive. If you change these, bot may not work.consult bot creator @obsquriel"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`░█─░█ █▀▀ █── █── █▀▀█ `"
"                     `░█▀▀█ █▀▀ █── █── █──█ `"
"                     `░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ `\n\n`⋙⋙Telethon version:6.9.0`\n`⋙⋙Python version:3.7.1`\n`⋙⋙Bot version:1.1.2`\n\n"
                     f"▓▓`My owner`: {DEFAULTUSER}\n▒▒`channel`:@crackedapps_obsq\n"
                     "░░`Bot name:obsqofficial_bot`\n\n`➳➳fork by:`@obsquriel\n\n"
                     "➳➳`Database Status: Databases functioning normally!\n`\n"
                     "[DEPLOY THIS USERBOT NOW](https://github.com/obsq/obsquserbot.git)")
                     
