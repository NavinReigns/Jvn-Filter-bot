class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ Nᴀɴʙᴀ / Nᴀɴʙɪ 👋 ,{}
Mʏ Nᴀᴍᴇ ɪs <a href=https://t.me/jvn_filter_bot>Cᴀᴘᴛᴀɪɴ Jᴀᴄᴋ Sᴘᴀʀʀᴏᴡ😎</a>, I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs,
Jᴜsᴛ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ᴀɴᴅ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ, Tʜᴇɴ Sᴇᴇ Mʏ Pᴏᴡᴇʀs😎🔥

❤️ Pᴏᴡᴇʀᴇᴅ ʙʏ <a href=https://t.me/jvncreation>Jᴠɴ CʀᴇᴀTɪᴏɴ</a> 💫

🧑‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Navin_Reigns>Nᴀᴠɪɴ</a> </b>"""
    HELP_TXT = """
    <b>🙋🏻‍♂️ Hellooo {} 🤓

○  Join Official Channel here <a href=https://t.me/jvncreation>Jᴠɴ CʀᴇᴀTɪᴏɴ</a> 🌟

○  It's Official Group : <a href=https://t.me/+Mw5OHYKo9KkzODk9>Jᴠɴ Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ 24×7</a> ❤️

○  Search using inline mode
This methord works on any chat, Just type @jvn_filter_bot and then leave a space and search any movie you want...

○ Available Commands
     
 /start - Check I'm Alive..
 /status - Bot Status
 /info - User info 
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (owner only)

○ Notice 📙:-

○Dont Spam Me...🤒

❤️ Pᴏᴡᴇʀᴇᴅ ʙʏ <a href=https://t.me/jvncreation>Jᴠɴ CʀᴇᴀTɪᴏɴ</a> 💫

🧑‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Navin_Reigns>Nᴀᴠɪɴ</a> </b>"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Navin_Reigns>Nᴀᴠɪɴ</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://t.me/jvncreation  

<b>DEVS:</b>
- <a href=https://t.me/jvncreation>Navin</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/jvncreation)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """╭─────❪ 𝗦𝗧𝗔𝗧𝗨𝗦 ❫─────⍟
│
<b>├⍟ Tᴏᴛᴀʟ Fɪʟᴇs :</b> <code>{}</code>
│
<b>├⍟ Aᴄᴛɪᴠᴇ Uꜱᴇʀꜱ :</b> <code>{}</code>
│
<b>├⍟ Tᴏᴛᴀʟ Gʀᴏᴜᴘs :</b> <code>{}</code>
│
<b>├⍟ Dɪꜱᴋ Sɪᴢᴇ :</b> <code>512 MB</code>
│
<b>├⍟ Dɪꜱᴋ Uꜱᴇᴅ :</b> <code>{}</code>
│
<b>├⍟ Fʀᴇᴇ Dɪꜱᴋ :</b> <code>{}</code>
│
╰───❪ <b><a href=https://t.me/jvncreation>Jᴠɴ CʀᴇᴀTɪᴏɴ 💫</a></b> ❫───⍟"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
