from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit(
            "ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ"
        )
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b>")
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        return await Tm.edit("ᴅɪᴀ sᴜᴅᴀʜ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ")
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        await Tm.edit(
            f"<b>•> ɪᴅ: {get_id}\n•> ɴᴀᴍᴇ: {user.mention}\n•> ᴍᴀsᴀ ᴀᴋᴛɪғ: {get_bulan} ʙᴜʟᴀɴ\n•> ᴋᴇᴛᴇʀᴀɴɢᴀɴ: 𝘗𝘳𝘦𝘮𝘪𝘶𝘮\n•> ʙʏ: ᴍᴀxɢᴜɴs ᴜʙᴏᴛ</b>"
        )
        await bot.send_message(
            OWNER_ID,
            f"<b>•> ɪᴅ-sᴇʟʟᴇʀ: {message.from_user.id}\n\n•> ɪᴅ-ᴄᴜsᴛᴏᴍᴇʀ: {get_id}</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 sᴇʟʟᴇʀ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴄᴜsᴛᴏᴍᴇʀ ⚜️", callback_data=f"profil {get_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(f"<b> ✅ {user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_prem_user(client, message):
    text = "<b>📁ᴅᴀғᴛᴀʀ ᴘʀᴇᴍɪᴜᴍ ᴜʙᴏᴛ\n</b>"
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            userlist = f"<a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"   •> {userlist}\n"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blacklist(client, message):
    emot_1 = await get_vars(client.me.id, "EMOJI_TUNGGU")
    emot_tunggu = emot_1 if emot_1 else "6298454498884978957"
    
    if client.me.is_premium:
        _tunggu = f"""
<b><emoji id={emot_tunggu}>⏰</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>
"""
    else:
        _tunggu = f"""
<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>
"""

    Tm = await message.reply(_tunggu)
    chat_id = message.chat.id  # Assuming 'chat_id' is defined somewhere

    blacklist_result = await add_chat(client.me.id, chat_id)

    # Check if adding to blacklist was successful
    if blacklist_result:  
        emot_1 = await get_vars(client.me.id, "EMOJI_UDADA")
        emot_udada = emot_1 if emot_1 else "4942776109449085714"
        
        if client.me.is_premium:
            _udada = f"""
<b><emoji id={emot_udada}>❌</emoji> ɢʀᴏᴜᴘ ɪɴɪ sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʙʟᴀᴄᴋʟɪsᴛ</b>
"""
        else:
            _udada = f"""
<b>ɢʀᴏᴜᴘ ɪɴɪ sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʙʟᴀᴄᴋʟɪsᴛ</b>
"""
        return await Tm.edit(_udada)

        # Continue with the rest of your code...
    emot_1 = await get_vars(client.me.id, "EMOJI_BERHASIL")
    emot_berhasil = emot_1 if emot_1 else "4943174368881542467"
    
    if client.me.is_premium:
        _berhasil = f"""
<b><emoji id={emot_berhasil}>✅</emoji>{message.chat.title} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ</b>
"""
    else:
        _berhasil = f"""
<b>{message.chat.title} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ</b>
"""
    await Tm.edit(_berhasil)

    else:
        emot_1 = await get_vars(client.me.id, "EMOJI_KESALAHAN")
        emot_kesalahan = emot_1 if emot_1 else "4942820145748771860"
        
        if client.me.is_premium:
            _kesalahan = f"""
<b><emoji id={emot_kesalahan}>❌</emoji>ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ</b>
"""
        else:
            _kesalahan = f"""
<b>ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ</b>
"""
        await Tm.edit(_kesalahan)



async def get_blacklist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    msg = f"<b>• ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪsᴛ {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await Tm.delete()
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....</b>", quote=True)
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit("<b>ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴀɴᴅᴀ ᴋᴏsᴏɴɢ</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit("<b>sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )
    try:
        user = await client.get_users(user_id)
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("sᴜᴅᴀʜ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<b>•> ɪᴅ: {get_id}\n•> ɴᴀᴍᴇ: {user.mention}\n•> ᴋᴇᴛᴇʀᴀɴɢᴀɴ: 𝘙𝘦𝘴𝘦𝘭𝘭𝘦𝘳\n•> ʙʏ: ᴍᴀxɢᴜɴs ᴜʙᴏᴛ </b>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</n>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_seles_user(cliebt, message):
    text = f"<b>📁ᴅᴀғᴛᴀʀ ʀᴇsᴇʟʟᴇʀ ᴜʙᴏᴛ\n</b>"
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            user = f"<a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"   •> {user}\n"
    if not text:
        await message.reply_text("Tᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʜᴀʀɪ</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"•> ɪᴅ: {get_id}\n•> ᴀᴋᴛɪғᴋᴀɴ_sᴇʟᴀᴍᴀ: {get_day} ʜᴀʀɪ")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ")
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} ʙᴇʟᴜᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"•> ɪᴅ: {user_id}\n•> ᴀᴋᴛɪғ_ʜɪɴɢɢᴀ: {expired_date.strftime('%d-%m-%Y %H:%M:%S')}\n•> ᴡᴀᴋᴛᴜ_ᴀᴋᴛɪғ: {remaining_days} ʜᴀʀɪ"
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await Tm.edit(f"<b>✅ {user.id} ᴇxᴘɪʀᴇᴅ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs</b>")
