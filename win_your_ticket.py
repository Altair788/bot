#    в Bash консоль: pip install --user pytelegrambotapi
#    если проблемы с кодировкой в начало строки добавить: # - *- coding: utf- 8 - *-
#    и:import sys
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
#     хак  bot.polling(none_stop=True)

# - *- coding: utf- 8 - *-
import token_bot
import telebot
from telebot import types
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
bot = telebot.TeleBot(token_bot.token)
from random import randrange

print('Привет! Меня зовут Рич, Маус Рич. Приглашаю тебя на экономическую игру "Денежный поток 101"')
answer = (input(
    "Стоимость игры определяет только Удача. Дается одна попытка. Испытаем удачу? (да = Да, Удача на моей стороне, нет = Испытывать удачу? Это не для меня): "))
for i in range(1):
    price = randrange(0, 500, 100)
    if answer.lower() == 'да':
        print('Определяется стоимость участия в игре...(Обычная цена билета 500 рублей)')
        print(price, "руб")
        if price < 500:
            print("Поздравляю! Сегодня Удача определенно на твоей стороне!")
        else:
            print('Не расстраивайся! Попробуешь в другой раз. Удача любит настойчивых')
        print("Отправь фото с ценой билета орнанизатору мероприятия и ожидай анонса ближайшей игры :)")
    elif answer.lower() == 'нет':
        print('Возвращайся когда передумаешь :)')
bot.polling(none_stop=True)
