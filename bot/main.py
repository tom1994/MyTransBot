import logging
import time

import telebot
from telebot import types, logger

from py_translator import Translator

API_TOKEN = '762659974:AAGNfULHfktNi9kVVZGgHdsDoFvpRCOHaIU'
en_flag_url = 'https://i.loli.net/2018/11/16/5bee8d83bfe85.png'
zh_flag_url = 'https://i.loli.net/2018/11/16/5bee8d842805b.png'
jp_flag_url = 'https://i.loli.net/2018/11/16/5bee8d842f01b.png'
fr_flag_url = 'https://i.loli.net/2018/11/16/5bee8d843c568.png'
ru_flag_url = 'https://i.loli.net/2018/11/16/5bee8d843c71d.png'
ko_flag_url = 'https://i.loli.net/2018/11/16/5bee8e0a3672d.png'

bot = telebot.TeleBot(API_TOKEN)
logger.setLevel(logging.DEBUG)
translator = Translator()


def create_text_makeup(query):
    markup = types.InlineKeyboardMarkup()
    row = []
    row.append(types.InlineKeyboardButton(text="Original Text", callback_data="t-" + query))
    markup.row(*row)
    return markup


@bot.inline_handler(lambda query: len(query.query) is not 0)
def default_query(inline_query):
    try:
        logger.info(inline_query.query)
        makeup = create_text_makeup(inline_query.query)
        en = translator.translate(text=inline_query.query, dest='en').text
        zh_cn = translator.translate(text=inline_query.query, dest='zh-cn').text
        ja = translator.translate(text=inline_query.query, dest='ja').text
        fr = translator.translate(text=inline_query.query, dest='fr').text
        ru = translator.translate(text=inline_query.query, dest='ru').text
        ko = translator.translate(text=inline_query.query, dest='ko').text
        r1 = types.InlineQueryResultArticle('1', title='English', description=en,
                                            input_message_content=types.InputTextMessageContent(en),
                                            reply_markup=makeup, thumb_url=en_flag_url, thumb_height=512,
                                            thumb_width=512)
        r2 = types.InlineQueryResultArticle('2', title='Chinese 中文', description=zh_cn,
                                            input_message_content=types.InputTextMessageContent(zh_cn),
                                            reply_markup=makeup, thumb_url=zh_flag_url, thumb_height=512,
                                            thumb_width=512)
        r3 = types.InlineQueryResultArticle('3', title='Japanese 日本語', description=ja,
                                            input_message_content=types.InputTextMessageContent(ja),
                                            reply_markup=makeup, thumb_url=jp_flag_url, thumb_height=512,
                                            thumb_width=512)
        r4 = types.InlineQueryResultArticle('4', title='French Le français', description=fr,
                                            input_message_content=types.InputTextMessageContent(fr),
                                            reply_markup=makeup, thumb_url=fr_flag_url, thumb_height=512,
                                            thumb_width=512)
        r5 = types.InlineQueryResultArticle('5', title='Russian Русский', description=ru,
                                            input_message_content=types.InputTextMessageContent(ru),
                                            reply_markup=makeup, thumb_url=ru_flag_url, thumb_height=512,
                                            thumb_width=512)
        r6 = types.InlineQueryResultArticle('6', title='Korean 한국어', description=ko,
                                            input_message_content=types.InputTextMessageContent(ko),
                                            reply_markup=makeup, thumb_url=ko_flag_url, thumb_height=512,
                                            thumb_width=512)
        bot.answer_inline_query(inline_query.id, [r1, r2, r3, r4, r5, r6])
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data.startswith('t-'))
def callback_text(call):
    call_query_id = call.id
    try:
        text = call.data[2:]
        bot.answer_callback_query(call_query_id, text=text, show_alert=False)
    except Exception as e:
        logger.error(str(e))


def main_loop():
    while True:
        try:
            bot.polling(none_stop=False)
        except Exception as e:
            time.sleep(5)
            bot.stop_polling()
            print('bot stop polling!')


if __name__ == '__main__':
    main_loop()
