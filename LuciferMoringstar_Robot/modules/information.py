# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE

import os
from pyrogram import Client as lucifermoringstar_robot, filters, enums
from LuciferMoringstar_Robot.functions import get_file_id, extract_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@lucifermoringstar_robot.on_message(filters.command('id'))
async def showid(client, update):
    chat_type = update.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = update.chat.id
        first = update.from_user.first_name
        last = update.from_user.last_name or ""
        username = update.from_user.username
        dc_id = update.from_user.dc_id or ""
        await update.reply_text(f"β² π΅πΈπππ π½π°πΌπ΄: {first}\nβ² π»π°ππ π½π°πΌπ΄: {last}\nβ² πππ΄ππ½π°πΌπ΄: {username}\nβ² ππ΄π»π΄πΆππ°πΌ πΈπ³: <code>{user_id}</code>\nβ² π³π°ππ° π²π΄π½πππ΄: <code>{dc_id}</code>", quote=True)
        
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += f"β² π²π·π°π πΈπ³: <code>{update.chat.id}</code>\n"
        if update.reply_to_message:
            _id += f"β² πππ΄π πΈπ³: <code>{update.from_user.id if update.from_user else 'Anonymous'}</code>\n<b>β² ππ΄πΏπ»πΈπ΄π³ πππ΄π πΈπ³: <code>{update.reply_to_message.from_user.id if update.reply_to_message.from_user else 'Anonymous'}</code>\n"        
            file_info = get_file_id(update.reply_to_message)
        else:
            _id += f"β² πππ΄π πΈπ³: <code>{update.from_user.id if update.from_user else 'Anonymous'}</code>\n"
            file_info = get_file_id(update)
        if file_info:
            _id += f"<b>{file_info.message_type}</b>: <code>{file_info.file_id}</code>\n"
        await update.reply_text(_id, quote=True)
 


@lucifermoringstar_robot.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text("`π΅π΄ππ²π·πΈπ½πΆ πππ΄π πΈπ½π΅πΎ...`")
    await status_message.edit("`πΏππΎπ²π΄πππΈπ½πΆ πππ΄π πΈπ½π΅πΎ...`")    
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")


    last_name = from_user.last_name or "π½πΎπ½π΄"
    username = from_user.username or "π½πΎπ½π΄"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"

    message_out_str = ""
    message_out_str += f"β² π΅πΈπππ π½π°πΌπ΄: {from_user.first_name}\n"
    message_out_str += f"β² π»π°ππ π½π°πΌπ΄: {last_name}\n"
    message_out_str += f"β² ππ΄π»π΄πΆππ°πΌ πΈπ³: <code>{from_user.id}</code>\n"
    message_out_str += f"β² π³π°ππ° π²π΄π½πππ΄: <code>{dc_id}</code>\n"
    message_out_str += f"β² πππ΄ππ½π°πΌπ΄: @{username}\n"
    message_out_str += f"β² πππ΄π π»πΈπ½πΊ: <a href='tg://user?id={from_user.id}'><b>π²π»πΈπ²πΊ π·π΄ππ΄</b></a>\n"
    if message.chat.type in ((enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL)):
        try:
            await client.get_chat_member(chat_id=update.chat.id, user_id=update.from_user.id)
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += f"<b>β²πΉπΎπΈπ½π΄π³ ππ·πΈπ π²π·π°π πΎπ½: <code>{joined_date}</code>\n"            
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(message=chat_photo.big_file_id)
        
        pr0fess0r_99 = [[ InlineKeyboardButton('π π²π»πΎππ΄ π', callback_data='close') ]]
        pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
        await message.reply_photo(photo=local_user_photo, reply_markup=pr0fess0r_99, caption=message_out_str)        
        os.remove(local_user_photo)
    else:
        pr0fess0r_99 = [[ InlineKeyboardButton('π π²π»πΎππ΄ π', callback_data='close') ]]
        pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
        await message.reply_text(text=message_out_str, reply_markup=pr0fess0r_99, disable_notification=True)        

    await status_message.delete()
