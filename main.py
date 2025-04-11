import requests
from telegram.ext import Updater, CommandHandler

TOKEN = "7511752303:AAHPuAKzvgcaGP0n7kgNpWTSK9I3BlF6Pko"

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=idr"
    try:
        print(f"Mengambil harga dari: {url}")
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        data = response.json()
        return data[coin_id]["idr"]
    except Exception as e:
        print(f"Terjadi error: {e}")
        return None

def harga(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Ketik: /harga [nama_koin] (contoh: /harga bitcoin)")
        return

    coin = context.args[0].lower()
    price = get_price(coin)

    if price:
        update.message.reply_text(f"Harga {coin.title()} saat ini adalah Rp {price:,}")
    else:
        update.message.reply_text("Gagal mengambil harga. Pastikan nama koin benar.")

def start(update, context):
    update.message.reply_text("Halo! Ketik /harga [nama_koin] untuk cek harga crypto!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("harga", harga))

updater.start_polling()
print("Bot telah berjalan... Menunggu perintah...")
updater.idle()
