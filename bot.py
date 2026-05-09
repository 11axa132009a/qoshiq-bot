import telebot
import yt_dlp
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Qoshiq nomini yubor!")

@bot.message_handler(content_types=['text'])
def search_music(message):
    query = message.text

    if query.startswith("http") or query.startswith("/"):
        return

    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch5:{query} music", download=False)

            if 'entries' in result and len(result['entries']) > 0:
                video = result['entries'][0]

                title = video.get('title', 'Nomaʼlum')
                url = video.get('webpage_url', '')

                bot.reply_to(message, f"🎵 Topildi:\n\n{title}\n{url}")
            else:
                bot.reply_to(message, "❌ Topilmadi! Boshqa nom yozib ko‘ring.")

    except Exception as e:
        bot.reply_to(message, "❌ Xatolik yuz berdi!")

bot.infinity_polling()
