# fileName : plugins/dm/waste.py
# copyright ÂŠī¸ 2021 

from pyrogram import filters
from Configs.dm import Config
from pyrogram import Client as ILovePDF
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

#--------------->
#--------> Config var.
#------------------->

BANNED_USERS = Config.BANNED_USERS
ADMIN_ONLY = Config.ADMIN_ONLY
ADMINS = Config.ADMINS

#--------------->
#--------> LOCAL VARIABLES
#------------------->

UCantUse = "For Some Reason You Can't Use This Bot đ"


button=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "đ  Join Our Group  đ",
                    url="https://t.me/RG_bots"
                )
            ]
       ]
    )

#--------------->
#--------> PDF REPLY BUTTON
#------------------->

@ILovePDF.on_message(filters.private & ~filters.edited)
async def spam(bot, message):
    try:
        await message.reply_chat_action("typing")
        if (message.chat.id in BANNED_USERS) or (
            (ADMIN_ONLY) and (message.chat.id not in ADMINS)
        ):
            await message.reply_text(
                UCantUse, reply_markup=button
            )
            return
        await message.reply_text(
            f"`Wdym` đ¤, __if you are looking for text to pdf try:__ /txt2pdf..đ", quote=True
        )
    except Exception:
        pass


