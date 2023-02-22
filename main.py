import openai
import uvicorn
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6263713060:AAG05IPQuzmXoIZPrUTUmSCLCMwoT_NcygQ'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send1(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])


async def send2(message: types.Message):
    response = openai.Image.create(
        prompt=message.photo,
        n=2,
        size="1024x1024"
    )


@dp.message_handler()
async def send3(message: types.Message):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=message.text,
        temperature=0,
        max_tokens=54,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"]
    )
    await message.answer(response['choices'][0]['text'])

if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True)
    uvicorn.run("index:app", host="0.0.0.0.1", port=5000, log_level="info")
