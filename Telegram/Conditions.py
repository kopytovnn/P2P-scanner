from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from database.models.user import *
from aiogram import types


class Condition:
    def __init__(self, user):
        self.engine = create_engine("sqlite:///database/Data.db")
        Base.metadata.create_all(self.engine)
        self.user = user
        self.exodus = {

        }

    def condition(self, *args):
        if self:
            return True
        return False

    def check(self):
        answer = self.condition()
        return self.exodus[answer]


class UserIsSubscribed(Condition):
    def __init__(self, user, channel, bot):
        super().__init__(user)
        self.channel = channel
        self.bot = bot
        self.exodus = {
            True: True,
            False: True
        }

    async def condition(self):
        user_channel_status = await self.bot.get_chat_member(chat_id=self.channel, user_id=self.user)
        if user_channel_status.status != types.ChatMemberStatus.LEFT:
            return True
        else:
            return False


class UserHavePremium(Condition):
    def __init__(self, user, msg1='User is a premium user', msg2='User is not a premium user'):
        super().__init__(user)
        self.exodus = {
            True: msg1,
            False: msg2
        }

    def condition(self):
        status = self.user.status
        if status == 'premium':
            return True
        return False


class UserIsRegistered(Condition):
    def __init__(self, telegram_id):
        super().__init__(None)
        self.telegram_id = telegram_id
        self.exodus = {
            True: True,
            False: False
        }

    def condition(self):
        with Session(self.engine) as session:
            isRegistered = session.query(exists().where(User.telegram_id == str(self.telegram_id))).scalar()
            return isRegistered
