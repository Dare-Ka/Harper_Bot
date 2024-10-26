from admin.admin import error_handler
from settings.states import Settings
from events_text import send_message
from db.models import db, backup_db
from settings.settings_kb import settings_kb, menu_kb, again
from weather.weather_utils import get_weather_today
from weather.weather_text import weather_error
from random import choice
from weather.weather_kb import cities_kb
import asyncio
from aiogram import types, F, Bot, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "settings", flags={"chat_action": "typing"})
async def ask_settings(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Привет! Настраиваем рассылку!" "Отправлять утренние/вечерние сообщения?"
    )
    await asyncio.sleep(0.2)
    await callback.message.answer_sticker(
        sticker=choice(send_message), reply_markup=settings_kb
    )
    await state.set_state(Settings.mailing)


@router.message(Settings.mailing, flags={"chat_action": "typing"})
async def mailing_settings(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(mailing=message.text)
    context_data = await state.get_data()
    mailing = context_data.get("mailing")
    if mailing.strip().lower() == "да":
        await asyncio.sleep(0.2)
        await message.answer(
            "Выбери город для утренней рассылки погоды или введи свой",
            reply_markup=cities_kb,
        )
        await state.set_state(Settings.city)
    elif mailing.strip().lower() == "нет":
        try:
            await db.add_settings(tg_id=message.from_user.id, mailing=0, city="NULL")
            await backup_db.add_settings(
                tg_id=message.from_user.id, mailing=0, city="NULL"
            )
            await message.answer(
                text="Запомнил!\n" "Настройки в любой момент можно изменить😉",
                reply_markup=menu_kb,
            )
            await state.clear()
        except Exception as error:
            await error_handler("mailing_settings:\n" + str(error), bot)
            await state.clear()


@router.message(Settings.city, flags={"chat_action": "typing"})
async def city_settings(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(city=message.text)
    context_date = await state.get_data()
    city = context_date.get("city")
    try:
        if len(await get_weather_today(city)) != 0:
            await db.add_settings(tg_id=message.from_user.id, mailing=1, city=city)
            await backup_db.add_settings(
                tg_id=message.from_user.id, mailing=1, city=city
            )
            await message.answer(
                text="Запомнил!\n" "Настройки в любой момент можно изменить😉",
                reply_markup=menu_kb,
            )
            await state.clear()
        else:
            await message.answer(
                text=weather_error + "\nПопробуем еще?", reply_markup=again
            )
    except Exception as error:
        await error_handler("city_settings:\n" + str(error), bot)
        await state.clear()
