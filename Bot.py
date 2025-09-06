import os
import telebot

BOT_TOKEN = os.getenv("8293627914:AAHsIddC1XExdUo2_4KOacwJVj17SLQBkBw")

if not BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN provided. Please set it in Render Environment Variables.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to VaultXOfficialBot 🚀\nThis is a test message to confirm the bot is running.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
