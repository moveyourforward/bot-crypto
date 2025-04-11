	import requests
import telebot
import os

# Ambil token dari environment variable
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "Hai! Kirim /harga untuk cek harga BTC/USDT.")

@bot.message_handler(commands=['harga'])
def kirim_harga(message):
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        harga = data['bitcoin']['usd']
        bot.reply_to(message, f"Harga BTC/USD saat ini: ${harga}")
    except Exception as e:
        bot.reply_to(message, "Gagal mengambil harga. Coba lagi nanti.")
