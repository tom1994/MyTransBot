# MyTransBot

MyTransBot is a Telegram inline bot which can translate your message to other languages. It runs on Python 3 and uses [py_translator](https://github.com/markolofsen/py_translator) and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

![Snipaste_2018-11-16_17-46-47.png](https://i.loli.net/2018/11/16/5bee92fdaaf43.png)
![Screenshot_20181116-174705.png](https://i.loli.net/2018/11/16/5bee9358ed033.png)

Now，you can use it just type **@my_trans_bot** in your message box, and then input your word and select a language from  the popup menu. Enjoy it !

## Setup

Just install [py_translator](https://github.com/markolofsen/py_translator) and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

```bash
$ pip install 
$ pip install pyTelegramBotAPI
```

and change the TOKEN in `bot/main.py` to your own bot's. How to create a new bot, refer to [Bots Introduction](https://core.telegram.org/bots#3-how-do-i-create-a-bot).

## Run it!

```shell
$ cd ./bot
$ python3 main.py
```

