from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="Help", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="Set", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="Group", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", url=f"https://t.me/Brazzersnotfree",),
            InlineKeyboardButton(text="𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="𝗖𝗼𝗺𝗺𝗮𝗻𝗱", callback_data="settings_back_helper")
        ],
    ]
    return buttons
