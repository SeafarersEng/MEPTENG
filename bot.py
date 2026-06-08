import asyncio
import sys
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Your bot token
TOKEN = "8725396308:AAEcdfjIhkhMz6JrW_Es3YAY-advVUj9xoY"

# Fix for Windows + Python 3.14
if sys.platform == "win32" and hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Grammar questions (Set 1 – 20 questions)
grammar_questions = {
    1: {"text": "1. The crew ________ the deck every morning.", "options": ["clean", "cleans", "cleaning"], "answer": "cleans"},
    2: {"text": "2. The ship will leave the port ________ 5 p.m.", "options": ["in", "at", "on"], "answer": "at"},
    3: {"text": "3. They ________ lunch in the mess room now.", "options": ["have", "are having", "had"], "answer": "are having"},
    4: {"text": "4. The captain ________ the weather report yesterday.", "options": ["reads", "read", "reading"], "answer": "read"},
    5: {"text": "5. We always wear life jackets ________ drills.", "options": ["in", "during", "at"], "answer": "during"},
    6: {"text": "6. She ________ the engine room every day.", "options": ["visit", "visits", "visited"], "answer": "visits"},
    7: {"text": "7. The crews are ________ the ropes.", "options": ["check", "checking", "checked"], "answer": "checking"},
    8: {"text": "8. He didn't ________ the alarm.", "options": ["hears", "hear", "hearing"], "answer": "hear"},
    9: {"text": "9. This map is ________ than the old one.", "options": ["good", "better", "best"], "answer": "better"},
    10: {"text": "10. The radio officer is responsible ________ communication.", "options": ["to", "for", "of"], "answer": "for"},
    11: {"text": "11. They must ________ the cargo safely.", "options": ["loads", "load", "loading"], "answer": "load"},
    12: {"text": "12. The weather was very ________ yesterday.", "options": ["storm", "stormy", "storming"], "answer": "stormy"},
    13: {"text": "13. The captain ________ to the bridge now.", "options": ["goes", "is going", "went"], "answer": "is going"},
    14: {"text": "14. We arrived ________ the port early.", "options": ["in", "at", "on"], "answer": "at"},
    15: {"text": "15. The crew ________ finished the cleaning.", "options": ["has", "have", "having"], "answer": "have"},
    16: {"text": "16. He speaks very ________.", "options": ["clear", "clearly", "clearer"], "answer": "clearly"},
    17: {"text": "17. There are ________ lifejackets on board.", "options": ["much", "many", "little"], "answer": "many"},
    18: {"text": "18. The engineer ________ the engine last night.", "options": ["checks", "checked", "checking"], "answer": "checked"},
    19: {"text": "19. They were ________ when the bell rang.", "options": ["work", "working", "worked"], "answer": "working"},
    20: {"text": "20. She remembered ________ her ID card.", "options": ["bring", "to bring", "brought"], "answer": "to bring"},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚓ *MEPT Grammar Trainer Bot*\n\n"
        "Type /grammar to start the 20-question test.\n"
        "Type /help for commands.",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/grammar – Start a new test (20 questions)\n"
        "Choose answers by tapping the buttons.\n"
        "Good luck! ⚓"
    )

async def grammar_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["q_index"] = 1
    context.user_data["score"] = 0
    q = grammar_questions[1]
    keyboard = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in q["options"]]
    await update.message.reply_text(q["text"], reply_markup=InlineKeyboardMarkup(keyboard))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_choice = query.data
    idx = context.user_data.get("q_index", 1)
    if idx not in grammar_questions:
        await query.edit_message_text("Test already finished. Type /grammar to start over.")
        return
    correct = grammar_questions[idx]["answer"]
    if user_choice == correct:
        context.user_data["score"] += 1
        await query.edit_message_text(f"✅ Correct! Score: {context.user_data['score']}")
    else:
        await query.edit_message_text(f"❌ Wrong! Correct: {correct}. Score: {context.user_data['score']}")
    next_idx = idx + 1
    if next_idx in grammar_questions:
        context.user_data["q_index"] = next_idx
        q_next = grammar_questions[next_idx]
        keyboard = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in q_next["options"]]
        await query.message.reply_text(q_next["text"], reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        final = context.user_data["score"]
        total = len(grammar_questions)
        await query.message.reply_text(
            f"🏁 Test completed!\nFinal score: {final}/{total} ({final/total*100:.1f}%)\n"
            "Type /grammar to try again."
        )
        context.user_data.clear()

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("grammar", grammar_test))
    app.add_handler(CallbackQueryHandler(button_callback))
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Keep alive
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())