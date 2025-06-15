from fastapi import FastAPI, Request
from telegram.ext.webhook import WebhookServer


from telegram.ext import (
    Application, 
    CommandHandler,
    MessageHandler,
    filters
)
from config import TOKEN, WEBHOOK_URL
import commands as cmd
from models.main import on_startup, on_shutdown
import messages as msg

app = Application.builder().token(TOKEN).post_init(on_startup).post_shutdown(on_shutdown).build()
app.add_handler(CommandHandler("start", cmd.start_handle))
app.add_handler(MessageHandler(filters.TEXT, msg.message_handle))
app.add_handler(MessageHandler(filters.VIDEO, msg.video_handle))

def main():
    print("Bot is running...!")
    app.run_polling()


web = FastAPI()

@web.on_event("startup")
async def startup():
    await app.bot.set_webhook(url=WEBHOOK_URL)
    print("Webhook ulandi")

@web.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, app.bot)
    await app.process_update(update)
    return {"ok": True}

#if __name__ == "__main__":
#    main()