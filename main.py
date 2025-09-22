from telegram.ext import Application, CommandHandler
from config import Config

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name}! 👋\nربات کلکسیون فوتبال زنان فعال شد!")

async def help(update, context):
    await update.message.reply_text("راهنما:\n/start - شروع کار\n/help - راهنما")

def main():
    app = Application.builder().token(Config.TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    
    print("🤖 ربات شروع به کار کرد...")
    app.run_polling()

if __name__ == "__main__":
    main()
