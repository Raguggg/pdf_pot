# fileName : plugins/dm/callBack/asZip.py
# copyright ยฉ๏ธ 2021 

from pyrogram import filters
from pyrogram import Client as ILovePDF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#--------------->
#--------> PDF IMAGES TO ZIP, TAR(CB/BUTTON)
#------------------->

zIp = filters.create(lambda _, __, query: query.data == "zip")
KzIp = filters.create(lambda _, __, query: query.data.startswith("Kzip|"))

# Extract pgNo as Zip(with unknown pdf page number)
@ILovePDF.on_callback_query(zIp)
async def _zip(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img ยป as Zip ยป Pages:           \nTotal pages: unknown__ ๐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All ๐", callback_data="zipA")
                    ],[
                        InlineKeyboardButton("With In Range ๐", callback_data="zipR")
                    ],[
                        InlineKeyboardButton("Single Page ๐", callback_data="zipS")
                    ],[
                        InlineKeyboardButton("ยซ Back ยซ", callback_data="BTPM")
                    ]
                ]
            )
        )
    except Exception:
        pass

# Extract pgNo as Zip(with known pdf page number)
@ILovePDF.on_callback_query(KzIp)
async def _Kzip(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img ยป as Zipยป Pages:           \nTotal pages: {number_of_pages}__ ๐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All ๐", callback_data=f"KzipA|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("With In Range ๐", callback_data=f"KzipR|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("Single Page ๐", callback_data=f"KzipS|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("ยซ Back ยซ", callback_data=f"KBTPM|{number_of_pages}")
                    ]
                ]
            )
        )
    except Exception:
        pass

tAr = filters.create(lambda _, __, query: query.data == "tar")
KtAr = filters.create(lambda _, __, query: query.data.startswith("Ktar|"))

# Extract pgNo as Zip(with unknown pdf page number)
@ILovePDF.on_callback_query(tAr)
async def _tar(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img ยป as Tar ยป Pages:           \nTotal pages: unknown__ ๐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All ๐", callback_data="tarA")
                    ],[
                        InlineKeyboardButton("With In Range ๐", callback_data="tarR")
                    ],[
                        InlineKeyboardButton("Single Page ๐", callback_data="tarS")
                    ],[
                        InlineKeyboardButton("ยซ Back ยซ", callback_data="BTPM")
                    ]
                ]
            )
        )
    except Exception:
        pass

# Extract pgNo as Zip(with known pdf page number)
@ILovePDF.on_callback_query(KtAr)
async def _Ktar(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img ยป as Tarยป Pages:           \nTotal pages: {number_of_pages}__ ๐",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Extract All ๐", callback_data=f"KtarA|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("With In Range ๐", callback_data=f"KtarR|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("Single Page ๐", callback_data=f"KtarS|{number_of_pages}")
                    ],[
                        InlineKeyboardButton("ยซ Back ยซ", callback_data=f"KBTPM|{number_of_pages}")
                    ]
                ]
            )
        )
    except Exception:
        pass


