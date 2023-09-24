#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config
import anitopy

class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram <b>Video Encoder Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as s small video file!</b> \n\n/help for more details. \n\nOwner : @ninja_naruto_sai_2"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "🔥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...\n"
    
    UPLOAD_START = "🌋 ᴜᴘʟᴏᴀᴅɪɴɢ ...\n"
    
    COMPRESS_START = "🌧️ ᴛʀʏɪɴɢ ᴛᴏ ᴇɴᴄᴏᴅᴇ ..."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
      
    COMPRESS_SUCCESS = "saved_file_path = video
      eni = saved_file_path.split("/")[-1]
      xnx = eni.split(".")[-1]
      opm = eni.replace(f".{xnx}", " .mkv")
      nam = opm.replace("_", " ")
      nam = opm.replace(".", " ")
      anitopy_options = {'allowed_delimiters': ' '}
      new_name = anitopy.parse(nam)
      anime_name = new_name['anime_title']
      episode_no = new_name['episode_number']  
      joined_string = f"[{anime_name}] [Episode {episode_no}] [@Anime_Compass!🧭.mkv]"
      if 'anime_season' in new_name.keys():
        animes_season = new_name['anime_season']
        joined_string = f"[{anime_name}] [Season {animes_season}] [Episode {episode_no}] [@Anime_Compass!🧭.mkv]""

    COMPRESS_PROGRESS = "🌄 ETA: {} 💦 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @Linux_Repo"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
