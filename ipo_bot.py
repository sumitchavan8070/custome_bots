# # import requests
# # import asyncio
# # from telegram import Bot
# # from datetime import datetime

# # # ✅ Telegram Bot Details
# # BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"
# # # ✅ List of Telegram Channels (Add more channels here)
# # CHANNEL_USERNAMES = ["@mpscpaperss", "@policebhartipaperss"]  # Add more if needed

# # # ✅ Groww IPO API URL
# # API_URL = "https://groww.in/v1/api/stocks_primary_market_data/v2/ipo/all"

# # # ✅ Function to Fetch IPO Data from JSON API
# # def get_ipos():
# #     response = requests.get(API_URL)
# #     if response.status_code != 200:
# #         return {}
    
# #     ipo_data = response.json()
    
# #     # Extract the categorized IPO data
# #     categorized_ipos = {
# #         "active": ipo_data.get("ipoCompanyListingOrderMap", {}).get("ACTIVE", []),
# #         "closed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("CLOSED", []),
# #         "upcoming": ipo_data.get("ipoCompanyListingOrderMap", {}).get("UPCOMING", []),
# #         "listed": ipo_data.get("ipoCompanyListingOrderMap", {}).get("LISTED", [])
# #     }
    
# #     # Process each category
# #     processed_ipos = {
# #         "active": [],
# #         "closed": [],
# #         "upcoming": [],
# #         "listed": []
# #     }
    
# #     for category, ipo_list in categorized_ipos.items():
# #         for ipo in ipo_list[:5]:  # Limit to the latest 5 IPOs in each category
# #             company_name = ipo.get("companyName", "N/A")
# #             open_date = ipo.get("openDate", "N/A")
# #             close_date = ipo.get("closeDate", "N/A")
# #             issue_size = ipo.get("issueSizeCr", "N/A")
# #             price_band = f"{ipo.get('minPrice', 'N/A')} - {ipo.get('maxPrice', 'N/A')}"
# #             listing_at = ipo.get("listingAt", "N/A")
            
# #             processed_ipos[category].append({
# #                 "company_name": company_name,
# #                 "open_date": open_date,
# #                 "close_date": close_date,
# #                 "issue_size": issue_size,
# #                 "price_band": price_band,
# #                 "listing_at": listing_at
# #             })
    
# #     return processed_ipos

# # # ✅ Asynchronous Function to Post IPOs on Telegram
# # async def post_ipos():
# #     bot = Bot(token=BOT_TOKEN)
# #     categorized_ipos = get_ipos()
    
# #     if not any(categorized_ipos.values()):  # Check if all categories are empty
# #         for channel in CHANNEL_USERNAMES:
# #             await bot.send_message(chat_id=channel, text="⚠️ *आज कोणतीही नवीन IPO माहिती उपलब्ध नाही.*")
# #         return
    
# #     today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
# #     message = (
# #         f"🎯🚀 *IPO अपडेट्स ({today_date})* 📢\n\n"
# #         "====================\n"
# #         "✨ *नवीन IPO माहिती येथे उपलब्ध!* ✨\n"
# #         "====================\n\n"
# #     )
    
# #     # Add IPOs by category
# #     for category, ipos in categorized_ipos.items():
# #         if not ipos:  # Skip empty categories
# #             continue
        
# #         message += f"🔥 *{category.capitalize()} IPOs* 🔥\n"
# #         for idx, ipo in enumerate(ipos, start=1):
# #             message += (
# #                 f"📌 *{idx}. {ipo['company_name']}*\n"
# #                 f"📅 खुलण्याची तारीख: {ipo['open_date']}\n"
# #                 f"📅 बंद होण्याची तारीख: {ipo['close_date']}\n"
# #                 f"💰 इश्यू साईज: ₹{ipo['issue_size']} Cr\n"
# #                 f"📊 प्राइस बँड: ₹{ipo['price_band']}\n"
# #                 f"📋 लिस्टिंग: {ipo['listing_at']}\n"
# #                 "---------------------\n"
# #             )
# #         message += "\n"
    
# #     message += (
# #         "🎯🚀 *महाराष्ट्रात पहिल्यांदाच! Meadhikari – सर्व सरकारी परीक्षांसाठी जुन्या प्रश्नपत्रिकांसह (PYQ) सर्वोत्तम ऑनलाइन तयारी!* 🏆\n\n"
# #         "📚 सर्व परीक्षा, सर्व जुन्या प्रश्नपत्रिका (PYQ) – अनलिमिटेड सराव!\n"
# #         "🔥 100% जाहिरात-मुक्त ऑनलाइन टेस्ट सिरीज\n"
# #         "💰 फक्त ₹20/दिवस पासून सुरू होणारे आकर्षक आणि परवडणारे प्लान्स!\n\n"
# #         "🚀 *तुमच्या यशाचा प्रवास सुरू करा –*\n"
# #         "🌐 🔥🔥🔥 https://www.meadhikari.com/ \n\n\n"
# #     )
    
# #     for channel in CHANNEL_USERNAMES:
# #         await bot.send_message(chat_id=channel, text=message, parse_mode="Markdown")

# # # ✅ Run the Bot
# # asyncio.run(post_ipos())

# import requests
# import asyncio
# from telegram import Bot
# from datetime import datetime

# # ✅ Telegram Bot Details
# BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"
# # ✅ List of Telegram Channels (Add more channels here)
# CHANNEL_USERNAMES = ["@mpscpaperss", "@meadhikariacademy", "@policebhartipaperss"]  # Add more if needed

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
#             logo_url = ipo.get("logoUrl", "")
            
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
#                 "logo_url": logo_url,
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
#             await bot.send_message(chat_id=channel, text="⚠️ *आज कोणतीही नवीन IPO माहिती उपलब्ध नाही.*")
#         return
    
#     today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
#     message = (
#         f"🎯🚀 *IPO अपडेट्स ({today_date})* 📢\n\n"
#         "====================\n"
#         "✨ *नवीन IPO माहिती येथे उपलब्ध!* ✨\n"
#         "====================\n\n"
#     )
    
#     # Add IPOs by category
#     for category, ipos in categorized_ipos.items():
#         if not ipos:  # Skip empty categories
#             continue
        
#         message += f"🔥 *{category.capitalize()} IPOs* 🔥\n"
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
#                 f"🖼️ [Logo]({ipo['logo_url']})\n"
#                 "---------------------\n"
#             )
#         message += "\n"
    
#     message += (
#         "🎯🚀 *महाराष्ट्रात पहिल्यांदाच! Meadhikari – सर्व सरकारी परीक्षांसाठी जुन्या प्रश्नपत्रिकांसह (PYQ) सर्वोत्तम ऑनलाइन तयारी!* 🏆\n\n"
#         "📚 सर्व परीक्षा, सर्व जुन्या प्रश्नपत्रिका (PYQ) – अनलिमिटेड सराव!\n"
#         "🔥 100% जाहिरात-मुक्त ऑनलाइन टेस्ट सिरीज\n"
#         "💰 फक्त ₹20/दिवस पासून सुरू होणारे आकर्षक आणि परवडणारे प्लान्स!\n\n"
#         "🚀 *तुमच्या यशाचा प्रवास सुरू करा –*\n"
#         "🌐 🔥🔥🔥 https://www.meadhikari.com/ \n\n\n"
#     )
    
#     for channel in CHANNEL_USERNAMES:
#         await bot.send_message(chat_id=channel, text=message, parse_mode="Markdown")

# # ✅ Run the Bot
# asyncio.run(post_ipos())

import requests
import asyncio
from telegram import Bot
from datetime import datetime

# ✅ Telegram Bot Details
BOT_TOKEN = "7303519859:AAGdw5kJa2rSqTwQkF0lJoxkfgvqLcNlyb8"
# ✅ List of Telegram Channels (Add more channels here)
CHANNEL_USERNAMES = ["@mpscpaperss", "@meadhikariacademy", "@policebhartipaperss"]  # Add more if needed

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
            logo_url = ipo.get("logoUrl", "")
            
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
                "logo_url": logo_url,
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
            await bot.send_message(chat_id=channel, text="⚠️ *आज कोणतीही नवीन IPO माहिती उपलब्ध नाही.*", parse_mode="Markdown")
        return
    
    today_date = datetime.now().strftime("%d-%m-%Y")  # Get today's date in DD-MM-YYYY format
    
    # Generate separate messages for each category
    messages = []
    for category, ipos in categorized_ipos.items():
        if not ipos:  # Skip empty categories
            continue
        
        message = (
            f"🎯🚀 *IPO अपडेट्स ({today_date}) - {category.capitalize()} IPOs* 📢\n\n"
            "====================\n"
            "✨ *नवीन IPO माहिती येथे उपलब्ध!* ✨\n"
            "====================\n\n"
        )
        
        for idx, ipo in enumerate(ipos, start=1):
            message += (
                f"📌 *{idx}. {ipo['company_name']}*\n"
                f"📅 खुलण्याची तारीख: {ipo['open_date']}\n"
                f"📅 बंद होण्याची तारीख: {ipo['close_date']}\n"
                f"📊 प्राइस बँड: {ipo['price_band']}\n"
                f"📈 सब्सक्रिप्शन दर: {ipo['subscription_rate'] or 'N/A'}\n"
                f"📦 लॉट साईज: {ipo['lot_size']}\n"
                f"📋 लिस्टिंग तारीख: {ipo['listing_date'] or 'N/A'}\n"
                f"👤 रेग्युलर अर्ज: {ipo['regular_details']}\n"
                f"👤 HNI अर्ज: {ipo['hni_details']}\n"
                f"🖼️ [Logo]({ipo['logo_url']})\n"
                "---------------------\n"
            )
        
        messages.append(message)
    
    # Add footer message
    footer_message = (
        "🎯🚀 *महाराष्ट्रात पहिल्यांदाच! Meadhikari – सर्व सरकारी परीक्षांसाठी जुन्या प्रश्नपत्रिकांसह (PYQ) सर्वोत्तम ऑनलाइन तयारी!* 🏆\n\n"
        "📚 सर्व परीक्षा, सर्व जुन्या प्रश्नपत्रिका (PYQ) – अनलिमिटेड सराव!\n"
        "🔥 100% जाहिरात-मुक्त ऑनलाइन टेस्ट सिरीज\n"
        "💰 फक्त ₹20/दिवस पासून सुरू होणारे आकर्षक आणि परवडणारे प्लान्स!\n\n"
        "🚀 *तुमच्या यशाचा प्रवास सुरू करा –*\n"
        "🌐 🔥🔥🔥 https://www.meadhikari.com/ \n\n\n"
    )
    messages.append(footer_message)
    
    # Send messages to all channels
    for channel in CHANNEL_USERNAMES:
        for msg in messages:
            await bot.send_message(chat_id=channel, text=msg, parse_mode="Markdown")

# ✅ Run the Bot
asyncio.run(post_ipos())