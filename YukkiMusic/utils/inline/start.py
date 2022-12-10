from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], url=f"{SUPPORT_GROUP}"
            ),
            InlineKeyboardButton(
                text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_7"], user_id=OWNER
            )
        ],
     ]
    return buttons
