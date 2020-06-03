# PlantScraper v1.0

Scraper for tracking any plant restocks from Gabriella's Plants. Great for watching for ghost updates especially for high demand plants. Now you don't have to obsessively reload in hopes of catching your dream plants. Uses BeautifulSoup4, SMTP, and YAML.

To run, set your email and password through the crontab file and environment variables with `EMAIL`, `EMAILPASSWORD` respsectively. Then run the script: `python3 scraper.py`.

To set this running continuously, go into the crontab file to create a job and set it to the frequency that you would like it to run. I recommend running this every 30 seconds and the robot.txt file specifies that it should not be run more than once every 10 seconds. Also pipe the print output to any miscellaneous file. 

Go into the configuration file to enter the plants that you would like to track and the emails you would like to notify. You will need the full plant name and the url from the product page. 

If you get an authentification error when trying to log into Gmail, first go to the Google Account and go into Security. There you will see an option for Less Secure Apps. Turn on Access and save. If the authentification continues to occur, visit url[https://accounts.google.com/DisplayUnlockCaptcha](accounts.google.com to unlock a captch first).
