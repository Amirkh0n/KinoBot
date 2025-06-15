# decorators.py
import asyncio
from functools import wraps
from telegram import ChatMember
from config import CHANNEL_ID

def require_subscriptions():
    def decorator(func):
        @wraps(func)
        async def wrapper(context, user_id, movie_id):
            ad_channels = CHANNEL_ID.get("ads", {})

            # Har bir kanal uchun get_chat_member bajariladi
            async def check_channel(ad):
                try:
                    member = await context.bot.get_chat_member(chat_id=ad["id"], user_id=user_id)
                    
                    if member.status not in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
                        return add["link"]
                except Exception:
                    return False

            # Parallel tekshiruv
            results = await asyncio.gather(
                *(check_channel(ad) for ad in ad_channels.values())
            )

            if results is None:
                return await func(context, user_id, movie_id)
            else:
                button = btn.channel_links(result, movie_id)
                # Linklar chiqariladi (agar yo‘q bo‘lsa, kanal ID ko‘rsatiladi)
                
                await context.bot.send_message(
                    chat_id=user_id,
                    text="❗Iltimos, quyidagi kanallarga obuna bo‘ling:",
                    reply_markup = button
                )
        return wrapper
    return decorator