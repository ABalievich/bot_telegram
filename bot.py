import telebot
import _config
from _currencies import currencies
from _weather import weather

bot = telebot.TeleBot(_config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Курсы валют', 'Погода')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, вы написали мне /start", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in _config.greetings:
        bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}")
    elif message.text.lower() in _config.partings:
        bot.send_message(message.chat.id, f"Прощайте, {message.chat.first_name}")
    elif message.text.lower() in ["/currencies", "курсы валют"]:
        answer = currencies()
        bot.send_message(message.chat.id, answer)
    elif message.text.lower() in ["/weather", "погода"]:
        answer = weather('Brest, BY')
        answer += "\n\n" + weather('Minsk, BY')
        answer += "\n\n" + weather('Hrodna, BY')
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, f"Извините, {message.chat.first_name}. Я вас не понимаю.")


bot.polling()
