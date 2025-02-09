from typing import Callable, Union

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from FallenMusic import SUDOERS, app


async def is_admin(chat_id: int, user_id: int) -> bool:
    """Checks if a user is an admin or owner in a chat, and has can_manage_video_chats privilege."""
    try:
        check = await app.get_chat_member(chat_id, user_id)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in is_admin: {e}")  # Replace with proper logging
        return False  # Assume not an admin if there's an error

    if check.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        admin = check.privileges
        return admin.can_manage_video_chats
    return False


def admin_check(func: Callable) -> Callable:
    async def wrapper(_, obj: Union[Message, CallbackQuery]):
        chat_id = obj.chat.id if isinstance(obj, Message) else obj.message.chat.id
        user_id = obj.from_user.id if isinstance(obj, Message) else obj.from_user.id

        if not await is_active_chat(chat_id):
            if isinstance(obj, Message):
                return await obj.reply_text("ʙᴏᴛ ɪsɴ'ᴛ sᴛʀᴇᴀᴍɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.")
            else:
                return await obj.answer(
                    "ʙᴏᴛ ɪsɴ'ᴛ sᴛʀᴇᴀᴍɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.", show_alert=True
                )

        if user_id in SUDOERS:
            return await func(_, obj)

        if await is_admin(chat_id, user_id):
            return await func(_, obj)
        else:
            if isinstance(obj, Message):
                return await obj.reply_text(
                    "» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs."
                )
            else:
                return await obj.answer(
                    "» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪts.",
                    show_alert=True,
                )

    return wrapper
