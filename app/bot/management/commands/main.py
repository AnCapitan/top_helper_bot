from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import types
import pytz
import datetime

from bot.management.commands.config import bot, GROUP_EDUCATIONAL, GROUPADMIN, GROUPDIRECTOR



# Клавиатуры для пользователя
keyboardStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardCancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardRedirect = types.InlineKeyboardMarkup()
keyboardGoIt = types.InlineKeyboardMarkup()
keyboardGoAffter = types.InlineKeyboardMarkup()

# Кнопки на клавиатурах
btn_admin= types.KeyboardButton("Поставить задачу Сис.Админам 👨‍💻")
btn_director = types.KeyboardButton("Вопрос директору 😎")
btn_educational = types.KeyboardButton("Вопрос учебной части 👩‍🏫")
btn_committee = types.KeyboardButton("Вопрос приемной комиссии 🧑‍💼")
btnCancel = types.KeyboardButton("🚫 Отменить")


keyboardStart.add(btn_admin, btn_director)
keyboardStart.add(btn_educational, btn_committee)
keyboardCancel.add(btnCancel)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "{0}, рад приветствовать в телеграм боте <b>TOP Helper | Красноярск</b>".format(message.from_user.first_name), parse_mode='html')
    bot.send_message(message.from_user.id, "Сделайте выбор с помощью кнопок внизу", reply_markup=keyboardStart)

@bot.message_handler(commands=['help'])
def help(message):
    text = "Перед оправкой сообщения четко сформулируйте у себя в голове вопрос\n после определитесь в какой отдел TOP вам надо отправить ваше сообщение"
    bot.send_message(chat_id=message.from_user.id, text=text, parse_mode="html")


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == "Поставить задачу Сис.Админам 👨‍💻":
        bot.send_message(message.from_user.id, "Напишите мне свой вопрос и я отправлю его спикеру", reply_markup=keyboardCancel)
        bot.register_next_step_handler(message, set_task_admin) 
    elif message.text == "Вопрос директору 😎":
        bot.send_message(message.from_user.id, "Напишите мне свой вопрос и я отправлю его спикеру", reply_markup=keyboardCancel)
        bot.register_next_step_handler(message, question_director)
    elif message.text == "Вопрос учебной части 👩‍🏫":
        bot.send_message(message.from_user.id, "Напишите мне свой вопрос и я отправлю его спикеру", reply_markup=keyboardCancel)
        bot.register_next_step_handler(message, question_educational_part) 
    elif message.text == "Вопрос приемной комиссии 🧑‍💼":
        bot.send_message(message.from_user.id, "Напишите мне свой вопрос и я отправлю его спикеру", reply_markup=keyboardCancel)
        bot.register_next_step_handler(message, question_selection_committee) 
    else:
        bot.send_message(message.from_user.id, "Извините, я Вас не понимаю... Воспользуйтесь кнопками", reply_markup=keyboardStart)


def set_task_admin(message):
    """Отправка сообщения в канал сис админов"""
    if message.text == "🚫 Отменить":
        """Если пользователь передумал отправлять сообщение в канал"""
        bot.send_message(message.from_user.id, "Дайте знать если еще что то понадобится", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)
    else:
        """Отправка и зануление переменных"""
        tz = pytz.timezone('Asia/Bangkok')
        now = datetime.datetime.now(tz)
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        text = f"Задача от {message.from_user.username}:\n<b>Дата и время постановки задачи:</b> {time_str}\n<b>Описание задачи/проблемы</b>:{message.text}\n\nСсылка на его TG: https://t.me/{message.from_user.username}"
        bot.send_message(GROUPADMIN, text, parse_mode='html')
        bot.send_message(message.from_user.id, "Ваша задача отправлена в чат сис админов", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)



def question_director(message):
    """Отправка сообщения в канал с директором"""
    if message.text == "🚫 Отменить":
        """Если пользователь передумал отправлять сообщение в канал"""
        bot.send_message(message.from_user.id, "Дайте знать если еще что то понадобится", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)
    else:
        """Отправка и зануление переменных"""
        tz = pytz.timezone('Asia/Bangkok')
        now = datetime.datetime.now(tz)
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        text = f"Вопрос в чат с директором от {message.from_user.username}:\n<b>Дата и время вопроса:</b> {time_str}\n<b>Вопрос</b>:{message.text}\n\nСсылка на его TG: https://t.me/{message.from_user.username}"
        bot.send_message(GROUPDIRECTOR, text, parse_mode='html')
        bot.send_message(message.from_user.id, "Ваше сообщение отправлено с директром", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)



def question_educational_part(message):
    """Отправка сообщения в канал учебной части"""
    if message.text == "🚫 Отменить":
        """Если пользователь передумал отправлять сообщение в канал"""
        bot.send_message(message.from_user.id, "Дайте знать если еще что то понадобится", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)
    else:
        """Отправка и зануление переменных"""
        tz = pytz.timezone('Asia/Bangkok')
        now = datetime.datetime.now(tz)
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        text = f"Вопрос в чат <b>учебной части</b> от {message.from_user.username}:\n<b>Дата и время вопроса:</b> {time_str}\n<b>Вопрос</b>:{message.text}\n\nСсылка на его TG: https://t.me/{message.from_user.username}"
        bot.send_message(GROUP_EDUCATIONAL, text, parse_mode='html')
        bot.send_message(message.from_user.id, "Ваше сообщение отправлен в чат учебной части", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)

def question_selection_committee(message):
    """Отправка сообщения в канал приемной комиссии"""
    if message.text == "🚫 Отменить":
        """Если пользователь передумал отправлять сообщение в канал"""
        bot.send_message(message.from_user.id, "Дайте знать если еще что то понадобится", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)
    else:
        """Отправка и зануление переменных"""
        tz = pytz.timezone('Asia/Bangkok')
        now = datetime.datetime.now(tz)
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        text = f"Вопрос в чат <b>приемной комиссии</b> от {message.from_user.username}:\n<b>Дата и время вопроса:</b> {time_str}\n<b>Вопрос</b>:{message.text}\n\nСсылка на его TG: https://t.me/{message.from_user.username}"
        bot.send_message(GROUP_EDUCATIONAL, text, parse_mode='html')
        bot.send_message(message.from_user.id, "Ваше сообщение отправлено в чат приемной комисии", reply_markup=keyboardStart)
        bot.register_next_step_handler(message, get_message)




bot.set_my_commands([
    types.BotCommand("/start", "Перезапуск бота"),
    types.BotCommand("/help", "Инструкция")
])


class Command(BaseCommand):

    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        print('RUN BOT . . .')
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling(none_stop=True)
        print('STOP BOT . . .')