# This program is used to forward message from 'one-to-one' channel in telegram.


import logging
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"**Hi `{ok.user.first_name}`!**\n\n**I am a channel auto-forward bot!! Read /help to know more!\n\nI can be used in only two channels (one user) at a time.**\n\n[Our Channel](https://t.me/LuciferWorld77)..", buttons=[Button.url("Source Code", url="hhttps://github.com/Lucifer-00007/AutoForward_Bot_By_Luci")], link_preview=False)


@datgbot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\n**❄About this bot:\n➡This bot will send all new posts in one channel to the other channel. (without forwarded tag)!**\n\n**➡It can be used only in two channels at a time.**\n\n**❄How to use me?\n🏮Add me to both the channels.\n🏮Make me an admin in both.\n🏮Nowall new messages would be autoposted on the linked channel!!**\n\n**Liked the bot? Visit** [Our Channel](https://t.me/LuciferWorld77)")

@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl, event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Do visit @LuciferWorld77")
datgbot.run_until_disconnected()
