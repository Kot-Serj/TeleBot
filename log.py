import datetime
def log(message): # эта функция была взята из отурый источников

    dtn = datetime.datetime.now()
    botlogfile = open('watherbot.log', 'a', encoding="utf8")
    text = ''
    if message.text:
        text = message.text
        print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + text, file=botlogfile)
    botlogfile.close()