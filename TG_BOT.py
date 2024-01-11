import telebot
from  tokenTGbot import Token
# Замените 'YOUR_TOKEN' на ваш токен Telegram бота
TOKEN = Token

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Создаем клавиатуру с тремя кнопками
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton('Твич'))
keyboard.add(telebot.types.KeyboardButton('Дискорд'))
keyboard.add(telebot.types.KeyboardButton('ВКонтакте'))


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Приветсвую тебя в боте от RAID TEAM, тут ты можешь перейти на 1 из любых наших соц. сетей", reply_markup=keyboard)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()

    if text == 'твич':
        bot.send_message(message.chat.id, "Наши твич каналы, Пантерка:https://www.twitch.tv/black_cat_panter, Волк:https://www.twitch.tv/d_m_d_s_h_k_a")

    elif text == 'дискорд':
        bot.send_message(message.chat.id, "Наш дискорд сервер:https://discord.gg/VJhYAgCKNA")
    elif text == 'вконтакте':
        bot.send_message(message.chat.id, "Наш паблик вконтакте:https://vk.com/raid__team")
    else:
        bot.send_message(message.chat.id, "Неизвестная команда. Выберите одну из кнопок на клавиатуре.")


# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
