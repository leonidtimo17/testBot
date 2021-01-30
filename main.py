import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text', 'document'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


def get_document(message):
    if message.text == 'Прайс':
        file = open('Prays.pdf', 'rb')
        bot.send_document(message.chat.id, file)


bot.polling(none_stop=True, interval=0)
