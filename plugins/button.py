# (©)Codexbotz
# Recode by @mrismanaziz
# Modified by @SilenceSpe4ks
# t.me/SharingUserbot X t.me/infobotmusik


from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ]
        ]
        return buttons
     if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
         buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ]
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
         buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ]
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
         buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ]
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
         buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ]
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
     if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
     if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
      if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
     if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
     if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink4),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink1),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
     if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 4 •", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
        if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink4),
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink1),
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink4),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink1),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP:
        buttons = [
             [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 3 •", url=client.invitelink1),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 4 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
