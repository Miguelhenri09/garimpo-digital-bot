import os
os.system("pip uninstall -y telegram")  # remove a biblioteca errada

from telegram.bot import Bot
import time

TOKEN = "7648778018:AAGxzOaesHp-nHhpoU6kmi3zUYBmIw80rVY"
CHAT_ID = "@GarimpoDigitalBr"

bot = telegram.Bot(token=TOKEN)

while True:
    bot.send_message(
        chat_id=CHAT_ID,
        text="⏰ Mensagem automática do Garimpo Digital!\nO bot está funcionando perfeitamente!"
    )

    print("Mensagem enviada!")

    # time.sleep(60)  # espera 60 segundos para enviar de novo
