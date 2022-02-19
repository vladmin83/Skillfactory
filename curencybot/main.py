import telebot
import requests
import json

from config import *
from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_sart_help(message: telebot.types.Message):
    text = 'Чтобы начать работу нажмите поочередно на кнопки с валютами и задайте количество конвертируемой валюты'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base, sym, amount = message.text.split()
    except ValueError as e:
        bot.reply_to("Неверное количество параметров")
    try:
        r = requests.get(f"http://api.currencylayer.com/live?access_key=cf0b7a82426dee5db479c1bec14250f8")
        resp = json.loads(r.content)
        new_price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f"Цена {amount} {base} в {sym} :{new_price}")
    except APIException as e:
        bot.reply_to(f'Ошибка в команде: \n{e}')

bot.polling()