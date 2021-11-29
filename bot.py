import telebot
from convert import convert

token = "2115481100:AAHNGroAlVNhAaVc29oHmK2PMzUT5fPRq6o"
bot = telebot.TeleBot(token)

start_text = "Send me tex code and i will translate it into text message"


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start" or message.text == "/start@TexToTxtBot":
        bot.send_message(message.from_user.id, start_text)
    else:
        bot.send_message(message.from_user.id, convert(message.text))


bot.infinity_polling()



