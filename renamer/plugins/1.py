import logging
logger = logging.getLogger(__name__)

import datetime
from ..config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied


@Client.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    if Config.FORCE_SUB:
        try:
            chat = await c.get_chat_member(Config.FORCE_SUB, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hai you are Bannedfrom pyrogram.emoji import *

class TEXT:
    DOWNLOAD_START = f"Downloading Starts soon {SLEEPING_FACE}"
    UPLOAD_START = f"Upload Starting Soon {SLEEPING_FACE}"
    UPLOAD_SUCESS = f"Thanks for using [me](https://t.me/TgRenameV2Bot)"
    BANNED_USER_TEXT = f"**Sorry D U D E**, you are **BANNED** from using me {FACE_WITH_TEARS_OF_JOY}."
    NOT_LOGGED_TEXT = f"This bot was only for private use {LOCKED_WITH_KEY}. If you want to use this bot you need to send me correct password in the format `/login bot_password`"
    SAVED_CUSTOM_THUMBNAIL = f"Thumbnail Saved Permanently {NOTEBOOK_WITH_DECORATIVE_COVER}"
    DELETED_CUSTOM_THUMBNAIL = f"Thumbnail Deleted Successfully {CHECK_MARK_BUTTON}"
    NO_CUSTOM_THUMB_NAIL_FOUND = f"𝖭𝗈 𝗍𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖥𝗈𝗎𝗇𝖽 {THUMBS_DOWN_LIGHT_SKIN_TONE}"
    THUMBNAIL_CAPTION = f"{BACKHAND_INDEX_POINTING_UP_LIGHT_SKIN_TONE} Your Permanent thumbnail"


    ABOUT = """**𝖬𝗒 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 :**

** My Name:** {bot_name}
    
** Language:** [Python 3](https://www.python.org/)

** FrameWork:** [Pyrogram](https://github.com/pyrogram/pyrogram)

** Creator:** {bot_owner}

** Developer:** 


** Channel:** [MyTestBotZ](https://t.me/MyTestBotZ)

** Server:** [Heroku](https://www.heroku.com)

** Build version:** [Stable V1](https://t.me/TgRenameV2bot)
"""

    HELP_USER = """**Follow Below Steps:**
   
☞︎︎︎ Use /mode command to change upload mode.
☞︎︎︎ Send a photo to set as permanent thumbnail. (Optional)
☞︎︎︎ Now send me the Telegram file you want to rename.
☞︎︎︎ Send the new name when bot ask.


"""

    START_TEXT = """Hi {user_mention},

**A Simple Telegram RenameBot with Permanent Thumbnail Support.**



**Maintained By:** {bot_owner}
"""


    DONATE_USER = """**__Thanks for showing interest in donation.__**
 
All My Bots are hosted in free Server, if you Likes ma Works, & interested you donate some money it will be helpful for me to Pay my Internet Bills ☺️

**For Donate:** Message ** @OO7ROBot **"""
 from my updates channel. So, you are not able to use me',  quote=True)

        except UserNotParticipant:
            button = [[InlineKeyboardButton('join Updates channel', url=f'https://t.me/{Config.FORCE_SUB}')]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="Hey join in my updates channel to use me.", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            logger.warning(f"Make me admin in @{Config.FORCE_SUB}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{Config.FORCE_SUB}")

        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text("The forcesub username was Incorrect. Please give the correct username.")

        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                if m.from_user.id in Config.AUTH_USERS:
                    return await m.reply_text("Forcesub username must be a channel username Not yours or any other users username")
            logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [Him](https://t.me/OO7ROBot)", disable_web_page_preview=True, quote=True)

    await m.continue_propagation()

