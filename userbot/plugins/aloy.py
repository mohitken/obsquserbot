"""Check if userbot alive. If you change these, bot may not work.consult bot creator @obsquriel"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.aloy$")
@borg.on(admin_cmd(pattern=r"aloy"))
async def amireallyalive(aloy):
    """ For .aloy command, check if the bot is running.  """
    await aloy.edit("` ░█─░█ █▀▀ █── █── █▀▀█ `"
"                     `░█▀▀█ █▀▀ █── █── █──█ `"
"                     `░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ `\n\nnjn oru paavam malayali aane..ivda ethelum mallu indele dm cheyy`⋙⋙Telethon version:6.9.0`\n`⋙⋙Python version:3.7.1`\n`⋙⋙Bot version:1.1.2`\n\n"
                     f"▓▓`My owner`: {DEFAULTUSER}\n▒▒`channel`:@crackedapps_obsq\n"
                     "░░`Bot name:obsqofficial_bot`\n\n`➳➳fork by:`@obsquriel\n\n"
                     "➳➳`Database Status: Database ellam error aane..lockdown aayond ellarum net ill aa athond server hang!\n`\n"
                     "[Ivde amarthi ee botina deploy cheyy](https://github.com/obsq/obsquserbot.git)")
                     
