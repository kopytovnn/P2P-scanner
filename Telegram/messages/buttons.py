from aiogram import Bot, Dispatcher, Router, types


FIND_CHAIN = types.InlineKeyboardButton(
        text="🔎 Найти связки",
        callback_data="find_chain")
SUPPORT_PROJECT = types.InlineKeyboardButton(
        text="🙏 Поддержать проект",
        callback_data="support_project")
COOPERATION = types.InlineKeyboardButton(
        text="💸 Сотрудничество",
        callback_data="cooperation")
