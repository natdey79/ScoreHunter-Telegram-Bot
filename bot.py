import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Get token from environment variable (for security)
TOKEN = os.environ.get("BOT_TOKEN")

# If no environment variable, use hardcoded token (remove this after testing)
if not TOKEN:
    TOKEN = "8751849176:AAGPtwzTmjJnPqmBrTbySqv84IAewcCz36c"  # ⚠️ REPLACE THIS WITH YOUR ACTUAL TOKEN

if not TOKEN or TOKEN == "YOUR_BOT_TOKEN_HERE":
    print("❌ ERROR: Please set your bot token!")
    print("Get it from @BotFather on Telegram")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📰 Sport News", url="https://t.me/scorehuntersports"),
            InlineKeyboardButton("💡 Betting Tips", url="https://t.me/scorehuntertips"),
        ],
        [
            InlineKeyboardButton("🎰 KuyaPlay Promotion", url="https://t.me/kuyaplay_CS"),
        ],
        [
            InlineKeyboardButton("🎮 Live CS", url="https://t.me/AhBoy_CS"),
        ],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Welcome to ScoreHunter!\n\n"
        "Choose a channel to explore:\n"
        "─────────────────────",
        reply_markup=reply_markup
    )

def main():
    try:
        print(f"🐍 Python version: {sys.version}")
        
        # Create application
        app = Application.builder().token(TOKEN).build()
        
        # Add command handler
        app.add_handler(CommandHandler("start", start))
        
        print("✅ Bot started successfully!")
        print("🔄 Running in polling mode...")
        
        # Start the bot
        app.run_polling()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
