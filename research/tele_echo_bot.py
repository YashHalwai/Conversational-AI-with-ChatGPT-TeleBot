import logging
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
# print(API_TOKEN)

# configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """ This handler recieves messages with '/start' or '/help' command """
    await message.reply("Welcome to CodeYAA! 🚀 Your Youthful Approach to Coding and Tech!\n\nJoin us in mastering programming and technology. Explore resources, connect with a diverse community, and subscribe for a coding adventure!\n\n🌐 [Website](https://www.youtube.com/@CodeYAA)\n\n#CodeYAA #CodingCommunity #TechAdvancement")
    
@dp.message_handler()
async def echo(message: types.Message):
    """ This will return echo """
    await message.answer(message.text)
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
