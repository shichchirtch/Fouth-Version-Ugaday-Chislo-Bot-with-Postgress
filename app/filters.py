from aiogram.filters import BaseFilter
from aiogram.types import Message
import sqlalchemy as db


class DATA_IS_NOT_DIGIT(BaseFilter):
    async  def __call__(self, message:Message):
        if not message.text.isdigit():
            return True
        return False

class CHECK_GAME_STATUS(BaseFilter):
    async  def __call__(self, table: db.Table):

        if not message.text.isdigit():
            return True
        return False