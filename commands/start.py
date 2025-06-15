from telegram import Update
from telegram.ext import ContextTypes
import config as conf
from models import User
import services as ser
import buttons.keyboard as btn

# /start command handler
async def start_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.effective_user.first_name
    #user
    user, create = await User.get_or_create(user_id = user_id, defaults = { "name": name})
    
    # stepni main menyu qilish
    context.user_data['step'] = conf.Steps.main_menu
    
    button = btn.start if user and user.is_admin else None
    args = context.args
    if args:
        await ser.send_movie_by_id(context, user_id, args[0])
        return
    await update.message.reply_text(f"Assalomu alaykum, {name}!\n\nQiziqtirgan kino bormi? Kodini yuboring — birga tomosha qilamiz!", reply_markup=button)