import telebot
import keep_alive
from telebot import types

# import sqlite3 if you want to

r = open('text.txt', encoding='utf-8') # r = read. In text.txt you can add any text you want to show up in TG
# after you click

r2 = r
r2 = "\n".join(r2)

auth = ['Made by:', 'TG: @balbeskinss', 'GITHUB: https://github.com/balbeskins']
auth = "\n".join(auth)

bot = telebot.TeleBot('YOURTOKEN')

@bot.message_handler(commands=['start'])

def main(message): # Start message that'll show up after you wrote /start
    markup = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton('text 1', callback_data='but1')
    but2 = types.InlineKeyboardButton('text 2', callback_data='but2')
    markup.add(but1, but2)

    bot.send_message(message.chat.id, auth, reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def callback_message(call): # Bot main buttons config
    if call.message:
        if call.data == 'but1': # If clicked button 1
            if len(r2) != 0: # If nothing written in text.txt
                markup = types.InlineKeyboardMarkup(row_width=2)
                but2 = types.InlineKeyboardButton('text 1', callback_data='but2')
                author = types.InlineKeyboardButton('⭕ Author menu', callback_data='author') # Sends you back to the author page
                markup.add(author, but2)

                bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.id,
                             text=f'✅ Your text from the text.txt: {r2}', reply_markup=markup)
            if len(r2) == 0: # If something written in text.txt
                markup = types.InlineKeyboardMarkup(row_width=2)
                but2 = types.InlineKeyboardButton('text 2', callback_data='but2')
                author = types.InlineKeyboardButton('⭕ Author menu', callback_data='author')
                markup.add(but2, author)

                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.id,
                                      text=f'❌ Text isnt written in the text.txt. Go watch code comments in the beggining.', reply_markup=markup)

        if call.data == 'but2': # If clicked button 2
            markup = types.InlineKeyboardMarkup(row_width=2)
            but1 = types.InlineKeyboardButton('text 1', callback_data='but1')
            author = types.InlineKeyboardButton('⭕ Author menu', callback_data='author')
            markup.add(but1, author)

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=f'text tht u want to be written here lol', reply_markup=markup)
        if call.data == 'author': # If clicked author button
            markup = types.InlineKeyboardMarkup(row_width=2)
            but1 = types.InlineKeyboardButton('text 1', callback_data='but1')
            but2 = types.InlineKeyboardButton('text 2', callback_data='but2')
            markup.add(but1, but2)

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=auth,
                                  reply_markup=markup)


bot.polling()
keep_alive.keep_alive()