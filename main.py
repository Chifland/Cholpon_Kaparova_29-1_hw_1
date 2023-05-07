from aiogram.utils import executor
import logging

from config import db
from handler import commands, extra, callback, admin


commands.register_handlers_commands(db)
callback.register_handlers_callback(db)
admin.register_handlers_admin(db)
extra.register_handlers_extra(db)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)