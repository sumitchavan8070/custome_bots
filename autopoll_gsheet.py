import random
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Bot

# ✅ Telegram Bot Details
BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"
CHANNEL_USERNAME = "@mpscpaperss"

# ✅ Google Sheets API Setup
GOOGLE_SHEET_ID = "1cRx_3q3y0yiAlCHU3RnUkSjzR307qR2yGt0zLwxuq1M"  # Get from the Google Sheets URL
SHEET_NAME = "Sheet1"  # Change if your sheet has a different name
CREDENTIALS_FILE = "./meadhikari-97401480aec0.json"  # JSON key file

# ✅ Load MCQs from Google Sheets
def get_random_mcq():
    # Google Sheets API Authentication
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    # Read Google Sheet
    sheet = client.open_by_key(GOOGLE_SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()

    if not data:
        return None

    mcq = random.choice(data)  # Pick a random MCQ
    question = mcq["Question"]
    options = [mcq["Option1"], mcq["Option2"], mcq["Option3"], mcq["Option4"]]

    # ✅ Extract correct answer from "optionX" format (e.g., "option2")
    correct_option_text = mcq["Correct Answer"].strip().lower()  # E.g., "option2"
    
    # ✅ Convert "option2" to index 1 (0-based index for Telegram)
    if correct_option_text.startswith("option") and correct_option_text[6:].isdigit():
        correct_index = int(correct_option_text[6:]) - 1  # Convert last digit to index
    else:
        return None  # Invalid format, skip posting

    return question, options, correct_index

# ✅ Asynchronous Function to Post Poll
async def post_mcq_poll():
    bot = Bot(token=BOT_TOKEN)
    mcq = get_random_mcq()

    if mcq:
        question, options, correct_index = mcq

        await bot.send_poll(
            chat_id=CHANNEL_USERNAME,
            question=question,
            options=options,
            is_anonymous=True,
            type="quiz",
            correct_option_id=correct_index
        )
    else:
        await bot.send_message(chat_id=CHANNEL_USERNAME, text="No MCQs found in Google Sheet!")

# ✅ Run the Bot
asyncio.run(post_mcq_poll())
