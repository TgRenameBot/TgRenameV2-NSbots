from pyrogram.emoji import *

class TEXT:
    DOWNLOAD_START = f"**AnalyZing your File** {SLEEPING_FACE}"
    UPLOAD_START = f"**Renaming File** {SLEEPING_FACE}"
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
   
➠ Use /toggle command to change upload mode.
➠ Send a photo to set as permanent thumbnail. (Optional)
➠ Now send me the Telegram file you want to rename.
➠ Send the new name with extension when bot ask.


"""

    START_TEXT = """Hi {user_mention},

**A Simple Telegram RenameBot with Permanent Thumbnail Support.**



**Maintained By:** {bot_owner}
"""


    DONATE_USER = """**__Thanks for showing interest in donation.__**
 
All My Bots are hosted in free Server, if you Likes ma Works, & interested you donate some money it will be helpful for me to Pay my Internet Bills ☺️

**For Donate:** Message ** @OO7ROBot **"""
