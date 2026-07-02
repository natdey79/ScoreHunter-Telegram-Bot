import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Get token from environment variable (for security)
TOKEN = os.environ.get("BOT_TOKEN")
import os
import sys
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Flask App for Keep-Alive ---
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health_check():
    return "Bot is running!", 200

def run_flask():
    """Run Flask on the port Render expects."""
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# --- Telegram Bot ---
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("❌ ERROR: BOT_TOKEN not set!")
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

def run_bot():
    """Run the Telegram bot in a separate thread."""
    try:
        print(f"🐍 Python version: {sys.version}")
        telegram_app = Application.builder().token(TOKEN).build()
        telegram_app.add_handler(CommandHandler("start", start))
        
        print("✅ Bot started successfully!")
        print("🔄 Running in polling mode...")
        
        telegram_app.run_polling()
    except Exception as e:
        print(f"❌ Bot Error: {e}")

if __name__ == "__main__":
    # Start the Telegram bot in a background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start the Flask web server (this keeps the service "awake")
    run_flask()
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
