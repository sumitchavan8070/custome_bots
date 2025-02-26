
# import requests
# import asyncio
# from telegram import Bot
# from datetime import datetime

# # ✅ Telegram Bot Details
# BOT_TOKEN = "7814658922:AAEoaNZVspGN4QD5Jdm-peE45a9tYldIYRQ"
# # ✅ List of Telegram Channels (Add more channels here)
# CHANNEL_USERNAMES = ["@latestipodaily"]  # Add more if needed

# # ✅ Groww IPO API URL
# API_URL = "https://groww.in/v1/api/stocks_primary_market_data/v2/ipo/all"

# # ✅ Function to Fetch IPO Data from JSON API
# def get_ipos():
#     response = requests.get(API_URL)
#     if response.status_code != 200:
#         return {}
    
#     ipo_data = response.json()
    
#     # Extract the categorized IPO data
#     categorized_ipos = {
#         "active": ipo_data.get("ipoCompanyListingOrderMap", {}).get("ACTIVE", []),
#         "closed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("CLOSED", []),
#         "upcoming": ipo_data.get("ipoCompanyListingOrderMap", {}).get("UPCOMING", []),
#         "listed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("LISTED", [])
#     }
    
#     # Process each category
#     processed_ipos = {
#         "active": [],
#         "closed": [],
#         "upcoming": [],
#         "listed": []
#     }
    
#     for category, ipo_list in categorized_ipos.items():
#         for ipo in ipo_list[:5]:  # Limit to the latest 5 IPOs in each category
#             company_name = ipo.get("growwShortName", "N/A")
#             open_date = ipo.get("biddingStartDate", "N/A")
#             close_date = ipo.get("biddingEndDate", "N/A")
#             min_price = ipo.get("minPrice", "N/A")
#             max_price = ipo.get("maxPrice", "N/A")
#             price_band = f"₹{min_price} - ₹{max_price}"
#             subscription_rate = ipo.get("totalSubscriptionRate", "N/A")
#             lot_size = ipo.get("lotSize", "N/A")
#             listing_date = ipo.get("listingDate", "N/A")
            
#             # Extract Regular and HNI category details
#             regular_category = next((cat for cat in ipo.get("categories", []) if cat.get("category") == "IND"), {})
#             hni_category = next((cat for cat in ipo.get("categories", []) if cat.get("category") == "HNI"), {})
            
#             regular_details = regular_category.get("categoryDetails", {}).get("categoryInfo", ["N/A"])[0]
#             hni_details = hni_category.get("categoryDetails", {}).get("categoryInfo", ["N/A"])[0]
            
#             processed_ipos[category].append({
#                 "company_name": company_name,
#                 "open_date": open_date,
#                 "close_date": close_date,
#                 "price_band": price_band,
#                 "subscription_rate": subscription_rate,
#                 "lot_size": lot_size,
#                 "listing_date": listing_date,
#                 "regular_details": regular_details,
#                 "hni_details": hni_details
#             })
    
#     return processed_ipos

# # ✅ Asynchronous Function to Post IPOs on Telegram
# async def post_ipos():
#     bot = Bot(token=BOT_TOKEN)
#     categorized_ipos = get_ipos()
    
#     if not any(categorized_ipos.values()):  # Check if all categories are empty
#         for channel in CHANNEL_USERNAMES:
#             await bot.send_message(chat_id=channel, text="⚠️ *आज कोणतीही नवीन IPO माहिती उपलब्ध नाही.*", parse_mode="Markdown")
#         return
    
#     today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
#     # Generate separate messages for each category
#     messages = []
#     for category, ipos in categorized_ipos.items():
#         if not ipos:  # Skip empty categories
#             continue
        
#         message = (
#             f"🎯🚀 *IPO अपडेट्स ({today_date}) - {category.capitalize()} IPOs* 📢\n\n"
#             "====================\n"
#             "✨ *नवीन IPO माहिती येथे उपलब्ध!* ✨\n"
#             "====================\n\n"
#         )
        
#         for idx, ipo in enumerate(ipos, start=1):
#             message += (
#                 f"📌 *{idx}. {ipo['company_name']}*\n"
#                 f"📅 खुलण्याची तारीख: {ipo['open_date']}\n"
#                 f"📅 बंद होण्याची तारीख: {ipo['close_date']}\n"
#                 f"📊 प्राइस बँड: {ipo['price_band']}\n"
#                 f"📈 सब्सक्रिप्शन दर: {ipo['subscription_rate'] or 'N/A'}\n"
#                 f"📦 लॉट साईज: {ipo['lot_size']}\n"
#                 f"📋 लिस्टिंग तारीख: {ipo['listing_date'] or 'N/A'}\n"
#                 f"👤 रेग्युलर अर्ज: {ipo['regular_details']}\n"
#                 f"👤 HNI अर्ज: {ipo['hni_details']}\n"
#                 "---------------------\n"
#             )
        
#         messages.append(message)
    
#     # Send messages to all channels
#     for channel in CHANNEL_USERNAMES:
#         for msg in messages:
#             await bot.send_message(chat_id=channel, text=msg, parse_mode="Markdown")

# # ✅ Run the Bot
# asyncio.run(post_ipos())

import requests
import asyncio
from telegram import Bot
from datetime import datetime

# ✅ Telegram Bot Details
BOT_TOKEN = "7814658922:AAEoaNZVspGN4QD5Jdm-peE45a9tYldIYRQ"
# ✅ List of Telegram Channels (Add more channels here)
CHANNEL_USERNAMES = ["@latestipodaily"]  # Add more if needed

# ✅ Groww IPO API URL
API_URL = "https://groww.in/v1/api/stocks_primary_market_data/v2/ipo/all"

# ✅ Function to Fetch IPO Data from JSON API
def get_ipos():
    response = requests.get(API_URL)
    if response.status_code != 200:
        return {}
    
    ipo_data = response.json()
    
    # Extract the categorized IPO data
    categorized_ipos = {
        "active": ipo_data.get("ipoCompanyListingOrderMap", {}).get("ACTIVE", []),
        "closed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("CLOSED", []),
        "upcoming": ipo_data.get("ipoCompanyListingOrderMap", {}).get("UPCOMING", []),
        "listed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("LISTED", [])
    }
    
    # Process each category
    processed_ipos = {
        "active": [],
        "closed": [],
        "upcoming": [],
        "listed": []
    }
    
    for category, ipo_list in categorized_ipos.items():
        for ipo in ipo_list[:5]:  # Limit to the latest 5 IPOs in each category
            company_name = ipo.get("growwShortName", "N/A")
            open_date = ipo.get("biddingStartDate", "N/A")
            close_date = ipo.get("biddingEndDate", "N/A")
            min_price = ipo.get("minPrice", "N/A")
            max_price = ipo.get("maxPrice", "N/A")
            price_band = f"₹{min_price} - ₹{max_price}"
            subscription_rate = ipo.get("totalSubscriptionRate", "N/A")
            lot_size = ipo.get("lotSize", "N/A")
            listing_date = ipo.get("listingDate", "N/A")
            
            # Extract Regular and HNI category details
            regular_category = next((cat for cat in ipo.get("categories", []) if cat.get("category") == "IND"), {})
            hni_category = next((cat for cat in ipo.get("categories", []) if cat.get("category") == "HNI"), {})
            
            regular_details = regular_category.get("categoryDetails", {}).get("categoryInfo", ["N/A"])[0]
            hni_details = hni_category.get("categoryDetails", {}).get("categoryInfo", ["N/A"])[0]
            
            processed_ipos[category].append({
                "company_name": company_name,
                "open_date": open_date,
                "close_date": close_date,
                "price_band": price_band,
                "subscription_rate": subscription_rate,
                "lot_size": lot_size,
                "listing_date": listing_date,
                "regular_details": regular_details,
                "hni_details": hni_details
            })
    
    return processed_ipos

# ✅ Asynchronous Function to Post IPOs on Telegram
async def post_ipos():
    bot = Bot(token=BOT_TOKEN)
    categorized_ipos = get_ipos()
    
    if not any(categorized_ipos.values()):  # Check if all categories are empty
        for channel in CHANNEL_USERNAMES:
            await bot.send_message(chat_id=channel, text="⚠️ *No new IPO information available today.*", parse_mode="Markdown")
        return
    
    today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
    # Generate separate messages for each category
    messages = []
    for category, ipos in categorized_ipos.items():
        if not ipos:  # Skip empty categories
            continue
        
        message = (
            f"🎯🚀 *IPO Updates ({today_date}) - {category.capitalize()} IPOs* 📢\n\n"
            "✨ *New IPO Information Available!* ✨\n"
            "-----------------------------\n\n"
        )
        
        for idx, ipo in enumerate(ipos, start=1):
            message += (
                f"📌 *{idx}. {ipo['company_name']}*\n"
                f"📅 Open Date: `{ipo['open_date']}`\n"
                f"📅 Close Date: `{ipo['close_date']}`\n"
                f"📊 Price Band: `{ipo['price_band']}`\n"
                f"📈 Subscription Rate: `{ipo['subscription_rate'] or 'N/A'}`\n"
                f"📦 Lot Size: `{ipo['lot_size']}`\n"
                f"📋 Listing Date: `{ipo['listing_date'] or 'N/A'}`\n"
                f"👤 Regular Application: `{ipo['regular_details']}`\n"
                f"👤 HNI Application: `{ipo['hni_details']}`\n"
                "-----------------------------\n"
            )
        
        messages.append(message)
    
    # Send messages to all channels
    for channel in CHANNEL_USERNAMES:
        for msg in messages:
            await bot.send_message(chat_id=channel, text=msg, parse_mode="Markdown")

# ✅ Run the Bot
asyncio.run(post_ipos())