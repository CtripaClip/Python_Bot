# Язык Python

from aiogram import Bot, types, Dispatcher, executor

TOCEN = 'Ваш токен с BotFather'

bot = Bot(token=TOCEN)
dp = Dispatcher(bot)

# создаём эхо-бота
@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    # Выводим на экран "Привет это эхо бот"
    await bot.send_message(message.from_user.id, "Привет это эхо бот")
    # Отправляем ему его сообщение
    await message.answer(message.text)

# задаём что наш бот будет работать только когда мы его включаем
executor.start_polling(dp, skip_updates=False)
