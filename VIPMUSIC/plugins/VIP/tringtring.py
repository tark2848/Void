import requests
from requests import get 
from VIPMUSIC import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from google_images_download import google_images_download

@app.on_message(filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

     response = google_images_download.googleimagesdownload()
     arguments = {"keywords": query, "limit": 6, "format": "jpg", "no_directory": True}
     paths = response.download(arguments)

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ɢᴏᴏɢʟᴇ...")
     for path in paths[0][query][:6]:
          media_group.append(InputMediaPhoto(media=open(path, 'rb')))
          count += 1
          await msg.edit(f"=> ᴏᴡᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:
        
        await app.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
