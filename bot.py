#импорт либ
import requests
import datetime, time
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token="=====YOUR TOKEN========"

vk=vk_api.VkApi(token=token)

longpoll=VkLongPoll(vk)

text=["Кек","Лол","Ну ты и лох","bot by Xachapury","Бтс топ","порно асманской империи "," Чукча","водка плоха","Привет","Здорова", "хеллоу", "хелло","хай","зиг хаиль","как дела","че каво","пошол нахуй","как тебя зовут", "ты че пидр",]

running=True

def write_msg(message, user_id, random_id):
  vk.method('messages.send', {'message': message,'user_id': user_id,'random_id': random_id,})
  
for event in longpoll.listen():
    if event.type==VkEventType.MESSAGE_NEW:
      request=event.text
      if event.from_user:
        if request=='TEST':
          print('получено')
          write_msg(random.choice(text), event.user_id, random.getrandbits(64))
