from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
#importtime
from time import sleep
import random
 
app = Client("my_account")

#Поиск лудшего друга
@app.on_message(filters.command("friend", prefixes=".") & filters.me)
def friend(_, msg):
    chat = msg.text.split(".friend")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Бот: Худшего друга ... " + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Бот: " + "Худший друг не найден!")
    sleep(3)
 
    msg.edit("Бот: " + "Поиск Фурри друга ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Бот: Поиск Фурри друга ... " + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 10)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Бот: " + "Найден Фурри друг!")
    sleep(3)
    msg.edit("Артём: " + "Он мой лудший друг?")
    sleep(3)
    msg.edit("Бот: " + "Происходит проверка...")
    sleep(1)
    while(perc < 100):
        try:
            text = "Бот: Происходит проверка ... " + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 10)
            sleep(0.10)
 
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Бот: " + "Да он ваш лудший друг!")
    

#Поиск жирных
@app.on_message(filters.command("ves", prefixes=".") & filters.me)
def ves(_, msg):
    chat = msg.text.split(".ves")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Бот: Поиск жирных в процессе... " + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Бот: " + "Жирные не обнаружены!")
    sleep(3)
 
    msg.edit("Бот: " + "Поиск красивых ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Бот: Поиск красивых ... " + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 10)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Бот: " + "Найден очень красивый объект!")
    sleep(3)

    msg.edit("Артём: Хмммм... Может этот 'объект' Ильдана?")
    sleep(5)
    msg.edit("Бот: Жаль, но этого распознать я не могу...")


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.02) # 50 ms
			tbp = tbp + text[0]
			text = text[1:]
			msg.edit(tbp)
			sleep(0.02)
		except FloodWait as e:
			sleep(e.x)
 
# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

#Танос
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
 
app.run()
