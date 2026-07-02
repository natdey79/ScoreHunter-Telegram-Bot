import os
import sys
import threading
import asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Flask App for Keep-Alive ---
app = Flask(__name__)import os
import sys
import threading
import asyncio
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

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ScoreHunter Bot\n\n"
        "Commands:\n"
        "/start - Show channel menu\n"
        "/help - Show this message"
    )

def run_bot():
    """Run the Telegram bot with proper event loop."""
    try:
        print(f"🐍 Python version: {sys.version}")
        
        # Create a new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Create application
        telegram_app = Application.builder().token(TOKEN).build()
        telegram_app.add_handler(CommandHandler("start", start))
        telegram_app.add_handler(CommandHandler("help", help_command))
        
        print("✅ Bot started successfully!")
        print("🔄 Running in polling mode...")
        print(f"🤖 Bot username: @{TOKEN.split(':')[0] if ':' in TOKEN else 'unknown'}")
        
        # Run the bot with the event loop
        loop.run_until_complete(telegram_app.run_polling())
        
    except Exception as e:
        print(f"❌ Bot Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Starting ScoreHunter Bot...")
    
    # Start the Telegram bot in a background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start the Flask web server
    run_flask()

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
    """Run the Telegram bot."""
    try:
        print(f"🐍 Python version: {sys.version}")
        telegram_app = Application.builder().token(TOKEN).build()
        telegram_app.add_handler(CommandHandler("start", start))
        
        print("✅ Bot started successfully!")
        print("🔄 Running in polling mode...")
        
        # Properly run the bot with asyncio
        asyncio.run(telegram_app.run_polling())
        
    except Exception as e:
        print(f"❌ Bot Error: {e}")

if __name__ == "__main__":
    # Start the Telegram bot in a background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start the Flask web server (this keeps the service "awake")
    run_flask()
