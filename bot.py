import os
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
    """Run Flask in a background thread."""
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

# --- Telegram Bot ---
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("❌ ERROR: BOT_TOKEN not set!")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"✅ /start received from: {update.effective_user.username}")
    
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
    print("✅ Reply with buttons sent!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ScoreHunter Bot\n\n"
        "Commands:\n"
        "/start - Show channel menu\n"
        "/help - Show this message"
    )

def run_bot():
    """Run the Telegram bot in the main thread."""
    try:
        print(f"🐍 Python version: {sys.version}")
        print(f"🤖 Bot Token: {TOKEN[:10]}... (truncated)")
        
        # Create application
        telegram_app = Application.builder().token(TOKEN).build()
        telegram_app.add_handler(CommandHandler("start", start))
        telegram_app.add_handler(CommandHandler("help", help_command))
        
        print("✅ Bot started successfully!")
        print("🔄 Running in polling mode...")
        
        # Run the bot - this blocks the main thread
        telegram_app.run_polling()
        
    except Exception as e:
        print(f"❌ Bot Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Starting ScoreHunter Bot...")
    
    # Start Flask in a background thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("✅ Flask server started in background")
    
    # Run the bot in the main thread
    run_bot()
