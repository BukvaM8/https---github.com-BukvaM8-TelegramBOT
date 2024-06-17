import telebot 
import webbrowser
from telebot import types

bot = telebot.TeleBot("7481417043:AAE33F4etOpga_jTuYiuAQJhgbth4ZU9Ot8")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./photo.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'Фото', reply_markup=markup)
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Photo is deleted')
    elif message.text == 'Изменить текст':
        bot.send_message(message.chat.id, 'Text is changed')
        
    

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com')

@bot.message_handler(commands=['weather', 'погода'])
def site(message):
    webbrowser.open('https://yandex.lv/pogoda/?lat=55.934281&lon=37.652301&utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home')

@bot.message_handler(commands=['start', 'start_bot', 'hello', 'main'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!', parse_mode='html')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "<b>Help</b> <em><u></u></em>", parse_mode='html')
    
@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower() == "привет":
            bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!', parse_mode='html')
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID:{message.from_user.id}')
    elif message.text.lower() == "старт":
            bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!', parse_mode='html')
   
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Ваша фотография', reply_markup=markup)

@bot.message_handler(content_types=['video'])
def get_video(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить видео', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Ваше видео', reply_markup=markup)
    
@bot.message_handler(content_types=['audio'])
def get_audio(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить аудио', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Ваше аудио', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'edit':
        bot.edit_message_text('Введите новый текст', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    
    
bot.polling(non_stop=True)