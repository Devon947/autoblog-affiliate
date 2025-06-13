import schedule
import time
import main

schedule.every().day.at("08:00").do(main.main)
schedule.every().day.at("20:00").do(main.main)

while True:
    schedule.run_pending()
    time.sleep(60)
