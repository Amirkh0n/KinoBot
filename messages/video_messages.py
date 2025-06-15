from models import User, Movie
import config as conf 

async def video_handle(update, context):
    user_id = update.effective_user.id 
    user = await User.get(user_id=user_id)
    step = context.user_data.get('step', 0)
    video = update.message.video 
    
    if user.is_admin:
        print(video)
        if video.file_size > 1016**3:
            size = f"{video.file_size/(1016**3):.2f} GB"
        else:
            size = f"{video.file_size/(1016**2):.2f} MB"
        
        hours = video.duration // 3600
        minutes = (video.duration % 3600) // 60
        duration = f"{hours:02d}:{minutes:02d}"
            
            
        if step == conf.Steps.add_movie:
            msg = await context.bot.copy_message(
                chat_id = conf.CHANNEL_ID["full_video"],
                from_chat_id = user_id, 
                message_id = update.message.message_id
            )
            await update.message.reply_text(text = "Kino nomini kiriting:")
            new_movie = await Movie.create(
                full_video_id=msg.message_id, 
                size = size,
                duration = duration
            )
            context.user_data["new_movie"] = new_movie
            context.user_data["step"] = conf.Steps.add_movie_title