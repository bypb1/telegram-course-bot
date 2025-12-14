from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = ReplyKeyboardMarkup(
    [["📚 Курсы", "💸 Цена"],
     ["📝 Записаться", "📩 Вопрос"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Я бот с курсами.\n"
        "Выбери, что тебе интересно 👇",
        reply_markup=keyboard
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Курсы":
        await update.message.reply_text(
            "📚 Наши курсы:\n"
            "1️⃣ Деньги и мышление\n"
            "2️⃣ Навыки для дохода\n"
            "3️⃣ Создание ботов"
        )
    elif text == "💸 Цена":
        await update.message.reply_text("💸 Цена курсов: от 19€")
    elif text == "📝 Записаться":
        await update.message.reply_text("✍️ Напиши: ХОЧУ КУРС")
    elif text == "📩 Вопрос":
        await update.message.reply_text("Напиши свой вопрос")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
