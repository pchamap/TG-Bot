import os
import telebot

bot = telebot.TeleBot("6464754")

@bot.message_handler(commands=["start"])
def send_wellcome(message):
    bot.reply_to(message,"Hello I'm chamara chat box")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"755845")

bot.polling()