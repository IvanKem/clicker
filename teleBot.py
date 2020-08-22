import telebot
import config

token = config.token
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Cайт с кликером: 192.168.235.45:8080")


bot.polling(none_stop=True)