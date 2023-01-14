from aiogram import Bot, Dispatcher, executor,types
import requests
from googletrans import Translator
import config



HELP_INFO = '''
Команды:
/date - Интересный факт о дате\n (Форма ввода: /date №Дня №Месяца)
'''

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def help_command(message: types.Message):
    await message.answer(text = "Приветствую.\n Введите /help для списка команд")
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_INFO)


@dp.message_handler(commands=["date"])
async def run(message: types.Message):
    text = message.text.split(maxsplit=1)[1]
    text = list(text.split())
    translator = Translator()
    response = requests.get("http://numbersapi.com/{month}/{day}/date".format(month=text[0],day=text[0]))
    result = translator.translate(response.text,src="en",dest="ru")
    await message.answer(result.text)


if __name__ == "__main__":
    executor.start_polling(dp)