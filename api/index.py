import telebot;
from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(getenv('TG_TOKEN'))

@bot.message_handler(content_types=['text', 'document'], chat_types=["private", "group"])
def get_text_messages(message):
   bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)