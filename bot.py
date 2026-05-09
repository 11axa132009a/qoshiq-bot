import telebot
import yt_dlp
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Qoshiq nomini yubor!")

@bot.message_handler(func=lambda m: True)
def search_music(message):
    query = message.text

    ydl_opts = {
        'quiet': True,
        'extract_flat': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{query}", download=False)

        if result['entries']:
            video = result['entries'][0]

            title = video['title']
            url = f"https://www.youtube.com/watch?v={video['id']}"

            bot.reply_to(
                message,
                f"Topildi!\n\n{title}\n{url}"
            )
        else:
            bot.reply_to(message, "Topilmadi!")

bot.infinity_polling()
