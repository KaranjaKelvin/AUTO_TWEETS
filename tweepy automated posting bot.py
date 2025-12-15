#tweepy automated posting bot
import tweepy
import schedule 
import time
import random
from datetime import datetime, timedelta
API_KEY = 'EPsLpUEPxQ9ZcsxLW2rpxPMnB'
API_SECRET_KEY = 'QJAXdqKM61DSXiNPLerPAtnNFPeokMRodER3dtf6lu5fCeGlHZ'
ACCESS_TOKEN = '1170973503631319041-As4Y1jFxaIAlBwk2XCwN6hqV9hZQEr'
ACCESS_TOKEN_SECRET = 'sKkYsOuNBJS2L7uEBp8Wf70ULiWC4Lc7yjxWT3seO4PR1'


# Replace these with your credentials

# Authentication
auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY, 
                                 consumer_secret=API_SECRET_KEY, 
                                 access_token=ACCESS_TOKEN, 
                                 access_token_secret=ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Check if authentication is successful
try:
    api.verify_credentials()
    print("Authentication Successful!")
except Exception as e:
    print("Authentication Failed", e)
client = tweepy.Client( consumer_key = API_KEY, consumer_secret = API_SECRET_KEY, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_TOKEN_SECRET)   
tweet_text = "Hello from my Python script using Tweepy!"
response = client.create_tweet(text=tweet_text)

def send_tweet(text="Automated tweet!"):
    try:
        client.create_tweet(text=text)
        print(f"[{datetime.now()}] Tweet sent: {text}")
    except Exception as e:
        print("Error sending tweet:", e)

# ------------------------------
# 3. SCHEDULE 15 RANDOM TIMES
# ------------------------------
def schedule_daily_posts():
    print("\n--- Scheduling 15 Posts for Today ---")

    for _ in range(15):
        # Generate random time between 2:00 AM and 11:00 AM
        start = datetime.now().replace(hour=2, minute=0, second=0, microsecond=0)
        end = datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)

        # If current time > 11 AM, schedule for next day
        if datetime.now() > end:
            start += timedelta(days=1)
            end += timedelta(days=1)

        # Pick a random second in the interval
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        post_time = start + timedelta(seconds=random_seconds)

        run_time_str = post_time.strftime("%H:%M:%S")
        
        # Schedule the tweet
        schedule.every().day.at(run_time_str).do(send_tweet, text="Random scheduled tweet!")
        print("Scheduled post at:", run_time_str)

# Run scheduling once at startup
schedule_daily_posts()


# Reschedule every day at midnight
schedule.every().day.at("00:01").do(schedule_daily_posts)

# ------------------------------
# 4. MAIN LOOP
# ------------------------------
print("\nTweet scheduler running...\n")

while True:
    schedule.run_pending()
    time.sleep(1)