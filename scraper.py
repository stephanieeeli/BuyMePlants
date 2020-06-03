#!/usr/bin/python

"""PlantScraper v1.0
Scrape GabriellaPlants.com for rare plants!
First update the crontab -e file and environment variables to
include email secrets, and the configuration include any additional
plants you wish to track. Then, run this script in a cron job and
wait! We recommend a delay of ~30sec between runs, and the robot.txt
file on the site states that it cannot be run more than once
every 10 seconds.
"""

import os
import bs4
import requests
import smtplib
import yaml

with open('config.yml', 'r') as file:
    document = yaml.full_load(file)

# Format (full_name, URL) 
plant_templates = document['plant_templates']

# Email addresses to send to
toAddress = document['toAddress']

# My email secrets
my_email = os.environ['EMAIL']
my_password = os.environ['EMAILPASSWORD']

def main():
    # If there are in-stock matches, append their template to this list
    matched = []

    # Scrape page of Gabriella for plants
    getPage = requests.get('https://www.gabriellaplants.com/collections/home-page?sort_by=price-descending')
    getPage.raise_for_status()
    inventory = bs4.BeautifulSoup(getPage.text, 'html.parser')
    for plant in inventory.select('.cd.chp'):  # Iterate through all plants on the website
        # Attempt to match against all templates' full names
        for j, (full_name, _) in enumerate(plant_templates):
            # Slide a window across the website text to match for these full plant names as a substring
            for i in range(len(plant.text)):
                chunk = plant.text[i:i+len(full_name)].lower()
                if chunk == full_name:
                    matched.append(plant_templates[j])

    if matched:
        # Send to Gmail
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login(my_email, my_password)
        for  full_name, url in matched:
            conn.sendmail(my_email, toAddress,
                          ('Subject: %s In Stock Alert\n\nCome get your '
                           '%s from Gabriella\'s!\n\n%s\n\n'
                           'Plant Notifier V1.0') % (full_name, full_name, url))
        conn.quit()
        print('Sent notifs')
    else:
        print('Out of stock')

if __name__ == "__main__":
    main()
