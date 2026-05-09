import telebot
import yt_dlp
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def search_music(message):
    query = message.text

    if query.startswith("/") or query.startswith("http"):
        return

    ydl_opts = {
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 🔥 3 xil variant bilan qidiramiz
            searches = [
                f"ytsearch5:{query} music",
                f"ytsearch5:{query} uzbek song",
                f"ytsearch5:{query} official"
            ]

            for s in searches:
                result = ydl.extract_info(s, download=False)

                if 'entries' in result and len(result['entries']) > 0:
                    video = result['entries'][0]

                    title = video.get('title', 'Nomaʼlum')
                    url = video.get('webpage_url', '')

                    bot.reply_to(message, f"🎵 Topildi:\n\n{title}\n{url}")
                    return

            bot.reply_to(message, "❌ Topilmadi! To‘liqroq nom yozing.")

    except Exception as e:
        bot.reply_to(message, "❌ Xatolik yuz berdi!")

bot.infinity_polling()
