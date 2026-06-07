from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mention = update.effective_user.mention_html(
        update.effective_user.first_name
    )
    bot_username = context.bot.username

    text = (
    f"✦ ʜᴇʏ <b>{mention}</b> !\n\n"
    f'⊚ ᴛʜɪꜱ ɪꜱ <a href="https://t.me/{bot_username}"><b>{context.bot.first_name}</b></a>'
)

    await update.message.reply_html(text)
    
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
