import requests
import telebot

TOKEN = "ваш_токен_бота"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот для парсинга Telegram-каналов запущен")

print("Telegram bot №1 запущен")
