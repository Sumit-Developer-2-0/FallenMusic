active = set()
stream = {}


async def is_active_chat(chat_id: int) -> bool:
    return chat_id in active


async def add_active_chat(chat_id: int):
    active.add(chat_id)


async def remove_active_chat(chat_id: int):
    active.discard(chat_id)


async def get_active_chats() -> list:
    return list(active)


async def is_streaming(chat_id: int) -> bool:
    return stream.get(chat_id, False)  # Return False if chat_id not in stream


async def stream_on(chat_id: int):
    stream[chat_id] = True


async def stream_off(chat_id: int):
    stream[chat_id] = False
