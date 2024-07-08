import telebot
from telebot import types

TOKEN = '7007092230:AAHAxYMq8GxCESJrjxCBfixYnzTA3XP_OMU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['info', 'start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Core Abierto? Yo te ayudaré a saberlo!\n\n-Usando /abierto podrás lanzar la pregunta a la que todos podrán responder de una manera más fácil.\nCon presionar el botón SÍ o el botón NO podrás notificar si Core Dumped está abierto o no a quien lo haya preguntado.")


@bot.message_handler(commands=["abierto"])
def send_options(message):
    markup=types.InlineKeyboardMarkup(row_width=2)
    btn_si=types.InlineKeyboardButton("Sí", callback_data="si")
    btn_no=types.InlineKeyboardButton("No", callback_data="no")
    markup.add(btn_si, btn_no)
    bot.send_message(message.chat.id, "Core abierto?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    
    if call.data == "si":
        markup=types.InlineKeyboardMarkup(row_width=4)
        hours = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        for i in range(0, len(hours), 4):
            row = hours[i:i+4]
            buttons = [types.InlineKeyboardButton(hour, callback_data=hour) for hour in row]
            markup.row(*buttons)
        bot.send_message(call.message.chat.id, "Hasta qué hora? (±)", reply_markup=markup)
    elif call.data == "no":
        bot.reply_to(call.message, "Core NO está abierto :(")
    else:
        bot.reply_to(call.message, f"CORE ABIERTO hasta las {call.data}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text.lower() == "no":
        bot.reply_to(message, ':(')
    

if __name__ == "__main__":
    bot.polling(none_stop=True)
