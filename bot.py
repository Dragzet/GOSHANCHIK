import config
import telebot
from telebot import types


bot = telebot.TeleBot(token=config.token)


menu = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
item1 = types.KeyboardButton('Иешуа')
item2 = types.KeyboardButton('Воланд')
item3 = types.KeyboardButton('Мастер')
item4 = types.KeyboardButton('Маргарита')
menu.add(item1)
menu.add(item2)
menu.add(item3)
menu.add(item4)


@bot.message_handler(commands=['start'])
def send_menu(message):

    bot.send_message(message.chat.id, 'Выберите героя', reply_markup=menu)


@bot.message_handler(content_types=['text'])
def mains(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id - 2)
    if message.text == 'Иешуа':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('Иешуа #1')
        item2 = types.KeyboardButton('Иешуа #2')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите цитату', reply_markup=markup)
    if message.text == 'Иешуа #1':
        bot.send_message(message.chat.id, '…всякая власть является насилием над людьми…', reply_markup=menu)
    if message.text == "Иешуа #2":
        bot.send_message(message.chat.id, '…Правду говорить легко и приятно …', reply_markup=menu)

    if message.text == 'Воланд':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('Воланд #1')
        item2 = types.KeyboardButton('Воланд #2')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите цитату', reply_markup=markup)

    if message.text == 'Маргарита':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('Маргарита #1')
        item2 = types.KeyboardButton('Маргарита #2')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите цитату', reply_markup=markup)


    if message.text == 'Мастер':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('Мастер #1')
        item2 = types.KeyboardButton('Мастер #2')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выберите цитату', reply_markup=markup)

    if message.text == "Воланд #1":
        bot.send_message(message.chat.id, '…тот, кто любит, должен разделять участь того, кого он любит… ', reply_markup=menu)
    if message.text == "Воланд #2":
        bot.send_message(message.chat.id, '…Рукописи не горят…', reply_markup=menu)

    if message.text == "Маргарита #1":
        bot.send_message(message.chat.id, '…грусть перед дальней дорогой. Не правда ли, мессир, она вполне естественна, даже тогда, когда человек знает, что в конце этой дороги его ждет счастье?..', reply_markup=menu)
    if message.text == "Маргарита #2":
        bot.send_message(message.chat.id, '…Интуристы... До чего же вы все интуристов обожаете! А среди них, между прочим, разные попадаются…', reply_markup=menu)


    if message.text == "Мастер #1":
        bot.send_message(message.chat.id, '…вообще не бывает так, чтобы все стало, как было…', reply_markup=menu)
    if message.text == "Мастер #2":
        bot.send_message(message.chat.id, '…вообще человек без сюрприза внутри, в своем ящике, неинтересен…', reply_markup=menu)



if __name__ == '__main__':
    bot.polling(none_stop=True)