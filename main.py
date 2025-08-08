import requests
import time
import os
from bs4 import BeautifulSoup
from telegram import Bot

# Your Telegram bot token
TELEGRAM_TOKEN = "8493864249:AAEsh3xxcclyFt7IdAPffSxGu4R3hihAgHs"
CHAT_ID = "1122971045"  # Your chat ID

# List of theaters to monitor
THEATERS = [
    "KG Cinemas",
    "The Cinema Brookefields",
    "SPI Cinemas Prozone"
]

# URL of the movie booking page
MOVIE_URL = "https://in.bookmyshow.com/movies/coimbatore/coolie/buytickets/ET00395817/20250814"

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

def check_tickets():
    try:
        response = requests.get(MOVIE_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text()

        found_theaters = []
        for theater in THEATERS:
            if theater.lower() in page_text.lower():
                found_theaters.append(theater)

        if found_theaters:
            send_message(f"🎟 Tickets Available in: {', '.join(found_theaters)}")
        else:
            print("No tickets yet...")
    except Exception as e:
        print("Error checking tickets:", e)

if __name__ == "__main__":
    send_message("🤖 Bot Started: Monitoring BookMyShow...")
    while True:
        check_tickets()
        time.sleep(300)  # Check every 5 minutes
