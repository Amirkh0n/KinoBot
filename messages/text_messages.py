from models import User 
import config as conf
import services as ser 


async def message_handle(update, context):
    user_id = update.effective_user.id 
    user = await User.get(user_id = user_id)
    message = update.message.text
    step = context.user_data.get("step", 0)
    
    if user.is_admin:
        if message == "Kino qo'shish➕️":
            context.user_data['step'] = conf.Steps.add_movie
            await update.message.reply_text(
                text = "Marhamat, qo'shmoqchi bo'lgan kinoning to'liq videosini yuboring."
            )
            return
        elif step == conf.Steps.add_movie_title:
            movie = context.user_data.get("new_movie")
            movie.title = message
            await movie.save()
            await update.message.reply_text("1")
            return
    
    if message.isdigit():
        await ser.send_movie_by_id(
            context = context, 
            user_id = user_id,
            movie_id = message
        )
    