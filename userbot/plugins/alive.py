"""Check if userbot alive. If you change these, bot may not work.consult bot creator @obsquriel"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import KYNE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(KYNE_NAME) if KYNE_NAME else "obsq"

#@command(outgoing=True, pattern="^!kyne$")
@borg.on(admin_cmd(pattern=r"!kyne"))
async def amireallyalive(alive):
    """ For !kyne command, check if the bot is running.  """
    await alive.edit("kyne mode on!!\n\n`⋙⋙kyne version:1.1.2`\n"
                     f"`⋙⋙My owner`: {DEFAULTUSER}\n"
                     "➳➳`Database Status: Databases functioning normally!`\n\n"
                     "[Made with love❤️](https://t.me/obsquriel)")
                     
