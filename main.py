# BU BOT NOMI-> Speak-English | Translate
# LINK -> https://t.me/speak_english_1950bot

import logging

from aiogram import Bot, Dispatcher, executor, types

from oxfordBookup import getDefinitions
from googletrans import Translator

translator = Translator()

API_TOKEN = '5400255468:AAGYlRPqGxGZasfKS5l4iUkDeu77dSEZfzA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):
    await message.reply("Assalamu alaykum 😎\nTarjimon Botga Xush Kelibsiz 🧐\nBot Ishlashga tayyot 👇")

@dp.message_handler()
async def tarjimon(message: types.Message):
    # -> Bu matn-ni qanaqa til-ekanini tekshiriladi
    lang = translator.detect(message.text).lang
    #  -> Bu user-dan kelgan matn-ni 2-ga bo`ladi
    if len(message.text.split()) > 1:
        # Bu user-dan kelgan matn-ni (uz bo`lsa en),(en bo`lsa uz) TILNI tanlaydi
        dest = 'uz' if lang == 'en' else 'en'
        # Bu Translate orqali TARJIMA QILADI
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so`z topilmadi...❌")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
