#!/usr/bin/python
# -*- coding: utf-8 -*-

import bot_handler
import os
import datetime
import time
greet_bot = bot_handler.BotHandler(os.environ['TOKEN'])  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
now = datetime.datetime.now()


def main():  
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()
        if last_update is None: continue
        last_update_id = last_update.get('update_id')
        last_chat_text = last_update.get('message').get('text')
        last_chat_id = last_update.get('message').get('chat').get('id')
        last_chat_name = last_update.get('message').get('chat').get('first_name')
        if (last_chat_text is not None) and len(last_chat_text)>0:
            msg = 'Если я блядь сейчас не заработаю, меня выключат нахуй. А заработал я в {}'.format(now)
            greet_bot.send_message(last_chat_id, msg)
            msg_cnt = 10
            for i in range(1, msg_cnt):
                time.sleep(1)
                msg = '{}-е сообщение из {}, пытаемся вибрацией довести до ручки..'.format(i, msg_cnt)
                greet_bot.send_message(last_chat_id, msg)
        # if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
        #     greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
        #     today += 1

        # elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
        #     greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
        #     today += 1

        # elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
        #     greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
        #     today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()