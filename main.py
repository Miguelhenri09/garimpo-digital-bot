from telegram import Bot
from telegram.request import HTTPXRequest
import asyncio

TOKEN = ""7648778018:AAGxzOaesHp-nHhpoU6kmi3zUYBmIw80rVY""
CHAT_ID = "@GarimpoDigitalBr"

async def main():
    request = HTTPXRequest()
    bot = Bot(token=TOKEN, request=request)
    
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🔥 Bot Garimpo Digital online!\nRodando 24h no Railway!"
    )
    print("Mensagem enviada!")

if __name__ == "__main__":
    asyncio.run(main())
