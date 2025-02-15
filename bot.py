import os
import requests
from pytube import YouTube
from whatsapp_web import WhatsApp

bot = WhatsApp()

@bot.on_message
def handle_message(msg):
    if msg.content.startswith("!يوتيوب "):
        url = msg.content.split(" ")[1]
        bot.send_message(msg.chat_id, "⏳ جاري تحميل الفيديو...")

        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filename = stream.download()

            bot.send_media(msg.chat_id, filename)
            os.remove(filename)  # حذف الفيديو بعد الإرسال
        except Exception as e:
            bot.send_message(msg.chat_id, "❌ فشل تحميل الفيديو!")

bot.run()
