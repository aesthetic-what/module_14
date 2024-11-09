from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

import asyncio

# import asyncio

bot = Bot('7061646789:AAG93_Mw4fprHsi5aiuU7XEzr9PuYGv9XN0')
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    growth = State()
    gender = State()
    age = State()
    weight = State()

test_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'), 
                                               KeyboardButton(text='Информация')],
                                              [KeyboardButton(text='Купить')]], 
                                              resize_keyboard=True)

buy_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Product 1', callback_data='product_buying'), 
                                                      InlineKeyboardButton(text='Product 2', callback_data='product_buying'),
                                                      InlineKeyboardButton(text='Product 3', callback_data='product_buying'),
                                                      InlineKeyboardButton(text='Product 4', callback_data='product_buying')]])


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет я бот помогающий твоему здоровью',reply_markup=test_keyboard)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:', reply_markup=ReplyKeyboardRemove())
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_groth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(groth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес в кг:')

@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    await state.set_state(UserState.gender)
    await message.answer('Введите свой пол:')

@dp.message_handler(state=UserState.gender)
async def calculate(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    user_gender = data['gender']
    user_age = int(data['age'])
    user_growth = int(data['growth'])
    user_weight = int(data['weight'])
    if user_age < 13 or user_age > 80:
        await message.answer('Данный калькулятор не подходит под ваш возраст')
        return
    print(user_age, user_growth, user_weight, user_gender)
    
    if user_gender.lower() == 'женский':
        calc_callories = 10 * user_weight + 6.25 * user_growth - 5 * user_age - 161
        await message.answer(f'Ваша норма каллорий: {calc_callories}')
    elif user_gender.lower() == 'мужской':
        calc_callories = 10 * user_weight + 6.25 * user_growth - 5 * user_age + 5
        await message.answer(f'Ваша норма каллорий: {calc_callories}', reply_markup=test_keyboard)

async def main():
   await dp.start_polling(bot)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
        for i in range(1, 5):
            with open(f'energy_{i}.jpg', 'rb') as img:
                await message.answer_photo(img, f'Название: Product{i} |'
                                                f' Описание: описание {i} | Цена: {i * 100}')
        await message.answer('Выберите продукт для покупки: ', reply_markup=buy_keyboard)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call, state):
        await call.message.answer('Вы успешно приобрели продукт!')
        await call.answer()

        await state.finish()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot deactivated')