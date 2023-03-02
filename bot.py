import logging
from pyrogram import filters
from pyrogram import Client
from voice_translate import recognize_voice
from video_translate import recognize_video


logging.basicConfig(level=logging.INFO)

app = Client(
        "Name of your app",
        api_id="your api_id https://my.telegram.org/apps",
        api_hash="your api_hash https://my.telegram.org/apps",
        bot_token="your token https://my.telegram.org/apps"
    )


@app.on_message(filters.video)
async def send_subtitles(app, message):
    """
    Responds to video-messages and tries to convert them into text
    """""
    file = await app.download_media(message)
    video_text = recognize_video(
        file_path=file
    )

    await message.reply(
       f'Текст из видео:\n{video_text}',
        quote=True,
    )


@app.on_message(filters.voice & filters.incoming)
async def voice_getter(app, message):
    """
    Responds to voice messages and tries to convert them into text
    """""

    file = await app.download_media(message)

    voice_texted = recognize_voice(
        file_path=file,
    )

    await message.reply(
        voice_texted,
        quote=True,
    )

app.run()
