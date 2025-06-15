from telegram.ext import (
    Application, 
    CommandHandler,
    MessageHandler,
    filters
)
from config import TOKEN
import commands as cmd
from models.main import on_startup, on_shutdown
import messages as msg


def main():
    app = Application.builder().token(TOKEN).post_init(on_startup).post_shutdown(on_shutdown).build()
    app.add_handler(CommandHandler("start", cmd.start_handle))
    app.add_handler(MessageHandler(filters.TEXT, msg.message_handle))
    app.add_handler(MessageHandler(filters.VIDEO, msg.video_handle))

    print("Bot is running...!")
    app.run_polling()
				
if __name__ == "__main__":
    main()