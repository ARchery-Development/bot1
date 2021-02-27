import telebot
bot = telebot.TeleBot("1614962605:AAHq6xuAD8D9ZDRGHACh9nGDvUjPvHpGXt8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здаров, чекаво?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Салют, бро!')
    elif message.text =='Пока':
        bot.reply_to(message, 'Уябывай')
	#bot.reply_to(message, message.text)

bot.polling()