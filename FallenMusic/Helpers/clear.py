import logging

from FallenMusic import fallendb
from FallenMusic.Helpers import remove_active_chat

# Configure logging (if not already configured)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def _clear_(chat_id):
    try:
        # Assuming fallendb is a dictionary-like object for demonstration
        if chat_id in fallendb:
            fallendb[chat_id] = []
        else:
            logging.warning(f"Chat ID {chat_id} not found in fallendb.")
            return  # Or create the entry if appropriate: fallendb[chat_id] = []

        await remove_active_chat(chat_id)
        logging.info(f"Cleared music queue and removed active chat for chat ID {chat_id}")

    except KeyError:
        logging.error(f"KeyError: Chat ID {chat_id} not found in fallendb.")
    except Exception as e:
        logging.exception(f"An unexpected error occurred while clearing chat {chat_id}: {e}")
        # Consider re-raising the exception if you can't handle it completely
        # raise
