import config as conf
from models import Movie


async def send_movie_by_id(context, user_id, movie_id):
    movie = await Movie.filter(id = movie_id).first()
    if movie:
        await movie.view()
        caption = f"""{movie.title}
💽: {movie.size}
🕒: {movie.duration}

📥: {movie.views}
"""
        
        await context.bot.copy_message(
            chat_id = user_id,
            from_chat_id = conf.CHANNEL_ID["full_video"],
            message_id = movie.full_video_id,
            caption = caption
        )
        
    else:
        await context.bot.send_message(
            chat_id = user_id,
            text = "Kino topilmadi!"
        )
