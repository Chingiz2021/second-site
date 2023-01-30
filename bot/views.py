from telebot import TeleBot, types
from rest_framework.response import Response
from rest_framework.views import APIView
# from TelegramBot.settings import TOKEN
from .models import ChatUser
TOKEN ='5959383988:AAH3Nadk4iRp56DNfOPb7uxJMQ6WZhXOIus'
 
bot = TeleBot(TOKEN)
 
 
class UpdateBot(APIView):
    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
 
        return Response({'code': 200})

class UpdateTestBot(APIView):
    def post(self, request):
        for item in ChatUser.objects.all():
            text = 'Поступила заявка на заказ номер 1'
            bot.send_message(item.chat_id, text=text, parse_mode='HTML')
        return Response({'code': 'ok'})
 
def send_order_bot(text):
        for item in ChatUser.objects.filter(active = True):
            bot.send_message(item.chat_id, text=text, parse_mode='HTML')
        return Response({'code': 'ok'})
        
@bot.message_handler(commands=['start'])
def start_message(message):
    # User написал /start в диалоге с ботом
    text = f'<b>Привет, {message.from_user.full_name}!</b>\n\n'
    text += 'В этот бот будут приходить оставленные на сайте заявки.\n\n'

 
    keyboard = types.InlineKeyboardMarkup()
    key_begin = types.InlineKeyboardButton(text='🖊️ Начать', callback_data='begin')
    keyboard.add(key_begin)
    if ChatUser.objects.filter(chat_id = message.chat.id).first():
        
        pass
    else:

        ChatUser.objects.create(chat_id = message.chat.id,full_name = message.from_user.full_name)
    bot.send_message(message.chat.id, text=text, parse_mode='HTML')
 
@bot.message_handler()
def start(message: types.Message):
    """
    {
        "message_id": 19, 
        "from": 
        {"id": 321044549, "is_bot": false, "first_name": "Gleb", "username": "hleb89", "language_code": "ru"}, 
        "chat": {"id": 321044549, "first_name": "Gleb", "username": "hleb89", "type": "private"}, 
        "date": 1666899794, "text": "rrrrrr"}
    """
    print(message.text)
    bot.send_message(message.chat.id, text=f"ответил, {message.from_user.full_name}, {message.text}", parse_mode='HTML')


# Webhook  https://api.telegram.org/bot5959383988:AAH3Nadk4iRp56DNfOPb7uxJMQ6WZhXOIus/setWebHook?url=https://unwanted.ae/api/bot
bot.set_webhook(url="https://unwanted.ae/api/bot/" + TOKEN)
