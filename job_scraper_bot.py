
import requests
from bs4 import BeautifulSoup
import asyncio
from telegram import Bot
from datetime import datetime

# ✅ Telegram Bot Details
BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"

# ✅ List of Telegram Channels (Add more channels here)
CHANNEL_USERNAMES = ["@mpscpaperss", "@meadhikariacademy" , "@policebhartipaperss"]  # Add more if needed

# ✅ Job Listings URL
URL = "https://majhinaukri.in/latest-jobs/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# ✅ Function to Scrape Job Listings
def get_jobs():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', class_='td_module_wrap')
    
    jobs = []
    for job in job_listings:
        title_tag = job.find('h3', class_='tdb_module_title')
        if title_tag:
            title = title_tag.text.strip()
            link = title_tag.find('a')['href']
            jobs.append({"title": title, "link": link})
    
    return jobs[:5]  # Limit to latest 5 jobs

# ✅ Function to Get Official Website Link
def get_official_website(job_url):
    response = requests.get(job_url, headers=HEADERS)
    if response.status_code != 200:
        return "🚫 🌍 अधिकृत संकेतस्थळ उपलब्ध नाही"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    website_tag = soup.find('a', text=lambda x: x and 'Official Website' in x)
    return website_tag['href'] if website_tag else "🚫 🌍 अधिकृत संकेतस्थळ उपलब्ध नाही"

# ✅ Asynchronous Function to Post Jobs on Telegram
async def post_jobs():
    bot = Bot(token=BOT_TOKEN)
    jobs = get_jobs()
    
    if not jobs:
        for channel in CHANNEL_USERNAMES:
            await bot.send_message(chat_id=channel, text="⚠️ *आज कोणतीही नवीन भरती नाही.*")
        return
    
    today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
    message = (
        f"🎯🚀 *नोकरी अपडेट्स ({today_date})* 📢\n\n"
        "====================\n"
        "✨ *नवीन सरकारी व खासगी नोकऱ्या येथे उपलब्ध!* ✨\n"
        "====================\n\n"
    )

    for idx, job in enumerate(jobs, start=1):
        official_website = get_official_website(job['link'])
        message += (
            f"🔥 *{idx}. {job['title']}*\n"
            f"🔗 🌍 [अधिकृत संकेतस्थळ]({official_website})\n"
            "====================\n\n"
        )
    
    message += (
        "🎯🚀 *महाराष्ट्रात पहिल्यांदाच! Meadhikari – सर्व सरकारी परीक्षांसाठी जुन्या प्रश्नपत्रिकांसह (PYQ) सर्वोत्तम ऑनलाइन तयारी!* 🏆\n\n"
        "📚 सर्व परीक्षा, सर्व जुन्या प्रश्नपत्रिका (PYQ) – अनलिमिटेड सराव!\n"
        "🔥 100% जाहिरात-मुक्त ऑनलाइन टेस्ट सिरीज\n"
        "💰 फक्त ₹20/दिवस पासून सुरू होणारे आकर्षक आणि परवडणारे प्लान्स!\n\n"
        "🚀 *तुमच्या यशाचा प्रवास सुरू करा –*\n"
        "🌐 🔥🔥🔥 https://www.meadhikari.com/ \n\n\n"
    )

    for channel in CHANNEL_USERNAMES:
        await bot.send_message(chat_id=channel, text=message, parse_mode="Markdown")

# ✅ Run the Bot
asyncio.run(post_jobs())
