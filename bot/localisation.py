#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @UniqueCoder

from bot.get_cfg import get_config

class Localisation:
    START_TEXT = "Greetings! \n\nWelcome to our Telegram <b>Video Encoding Bot</b>. \n\n<b>Please share a Telegram large video file, and I'll compress it into a smaller video!</b> \n\nFor more details, use /help. \n\nOwner: @ninja_naruto_sai_2"
   
    ABS_TEXT = " Please refrain from being self-centered."
    
    FORMAT_SELECTION = "Choose your desired format: <a href='{}'>file size might vary</a> \nIf you wish to set a custom thumbnail, send a photo before or immediately after selecting any of the buttons below.\nYou can use /deletethumbnail to remove the automatically generated thumbnail."
    
    DOWNLOAD_START = "⚡ Downloading...\n"
    
    UPLOAD_START = "⚡ Uploading...\n"
    
    COMPRESS_START = "⚡ Initiating encoding..."
    
    RCHD_BOT_API_LIMIT = "Size exceeds the maximum allowed (50MB). Nevertheless, attempting to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nI'm sorry, but I can't upload files larger than 1.95GB due to Telegram API restrictions."
    
    COMPRESS_SUCCESS = "Encoding completed {}"
    
    # ...

    file_name = "/app/downloads"

    # ...

    # Format COMPRESS_SUCCESS with the file name
    success_message = COMPRESS_SUCCESS.format(file_name)

    COMPRESS_PROGRESS = "🕛 ETA: {} ♻️ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video/file thumbnail saved. This image will be used in the video/file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared successfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared successfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom Thumbnail found."
    
    NO_VOID_FORMAT_FOUND = "Nobody is going to help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} until {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ There's already a process in progress! ⚠️ \n\nCheck the Live Status on the Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hello, I am the Video Compressor Bot. \n\n1. Send me your large Telegram video file. \n2. Reply to the file with: `/compress 50` \n\nSupport Group: "
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "Current Chat ID: <code>{CHAT_ID}</code>"
    )
