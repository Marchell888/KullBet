from PyroUbot import *

__MODULE__ = "showid"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏᴡɪᴅ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>id</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴅᴀʀɪ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>id</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴅᴀʀɪ ᴜsᴇʀ/ᴍᴇᴅɪᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>id</code> [ᴜsᴇʀɴᴀᴍᴇ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴍᴇʟᴀʟᴜɪ ᴜsᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("id", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await getid(client, message)
