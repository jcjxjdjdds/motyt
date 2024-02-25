import inspect
import json
import os.path
from functools import wraps, partial
from glob import glob
from typing import List, Dict

from pyrogram.types import CallbackQuery

from consts import group_types
from dbh import dbcGeneral, dbGeneral


def set_db_lang(chat_id: int, chat_type: str, lang_code: str):
    if chat_type == "private":
        dbcGeneral.execute("UPDATE users SET chat_lang = ? WHERE user_id = ?", (lang_code, chat_id))
        dbGeneral.commit()
    elif chat_type in group_types:  # groups and supergroups share the same table
        dbcGeneral.execute("UPDATE groups SET chat_lang = ? WHERE chat_id = ?", (lang_code, chat_id))
        dbGeneral.commit()
    elif chat_type == "channel":
        dbcGeneral.execute("UPDATE channels SET chat_lang = ? WHERE chat_id = ?", (lang_code, chat_id))
        dbGeneral.commit()
    else:
        raise TypeError("Unknown chat type '%s'." % chat_type)


def get_db_lang(chat_id: int, chat_type: str) -> str:
    if chat_type == "private":
        dbcGeneral.execute("SELECT chat_lang FROM users WHERE user_id = ?", (chat_id,))
        ul = dbcGeneral.fetchone()
    elif chat_type in group_types:  # groups and supergroups share the same table
        dbcGeneral.execute("SELECT chat_lang FROM groups WHERE chat_id = ?", (chat_id,))
        ul = dbcGeneral.fetchone()
    elif chat_type == "channel":
        dbcGeneral.execute("SELECT chat_lang FROM channels WHERE chat_id = ?", (chat_id,))
        ul = dbcGeneral.fetchone()
    else:
        raise TypeError("Unknown chat type '%s'." % chat_type)
    return ul[0] if ul else None


def get_locale_string(dic: dict, language: str, default_context: str, key: str, context: str = None) -> str:
    if context:
        default_context = context
        dic = langdict[language].get(context, langdict[default_language][context])
    res: str = dic.get(key) or langdict[default_language][default_context].get(key) or key
    return res


def get_lang(message) -> str:
    if isinstance(message, CallbackQuery):
        chat = message.message.chat
    else:
        chat = message.chat

    lang = get_db_lang(chat.id, chat.type)


def use_chat_lang(context=None):
    if not context:
        frame = inspect.stack()[1]
        context = frame[0].f_code.co_filename.split(os.path.sep)[-1].split(".")[0]

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            lang = get_lang(message)

            dic = langdict.get(lang, langdict[default_language])

            lfunc = partial(get_locale_string, dic.get(context, {}), lang, context)
            return await func(client, message, lfunc)

        return wrapper
    return decorator
