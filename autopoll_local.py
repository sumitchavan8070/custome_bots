
# ✅ Load MCQs from Local Excel File
import pandas as pd
import random
import asyncio
from telegram import Bot

# ✅ Telegram Bot & Channel Details
BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"
CHANNEL_USERNAME = "@mpscpaperss"

# ✅ Load MCQs from Local Excel File
EXCEL_FILE = "/home/sumit/telegrammpscmockbot/mcqs.xlsx"

def get_random_mcq():
    # Read the Excel file
    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")  # Use openpyxl for .xlsx
    if df.empty:
        return None
    
    mcq = df.sample(n=1).iloc[0]  # Pick a random MCQ
    question = mcq["Question"]
    options = [mcq["Option 1"], mcq["Option 2"], mcq["Option 3"], mcq["Option 4"]]
    correct_answer = mcq["Correct Answer"]

    return question, options, correct_answer

# ✅ Asynchronous Function to Post Poll
async def post_mcq_poll():
    bot = Bot(token=BOT_TOKEN)
    mcq = get_random_mcq()
    
    if mcq:
        question, options, correct_answer = mcq
        correct_index = options.index(correct_answer)  # Find correct answer index
        
        await bot.send_poll(  # Use await here
            chat_id=CHANNEL_USERNAME,
            question=question,
            options=options,
is_anonymous=True,  # ✅ Make it anonymous (required for channels)
            type="quiz",
            correct_option_id=correct_index
        )
    else:
        await bot.send_message(chat_id=CHANNEL_USERNAME, text="No MCQs found in the Excel file!")

# ✅ Run the Bot
asyncio.run(post_mcq_poll())
