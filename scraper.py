#!/usr/bin/python
"""PlantScraper v1.0
Scrape GabriellaPlants.com and Logees.com for rare plants!
First update the configuration file to include email secrets,
and include any additional plants you wish to track. Then,
run this script in a cron job and wait! We recommend a delay
of ~30sec between runs, although neither site explicitly states
a preference (no robot.txt).
"""

import bs4
import requests
import smtplib

# TODO: move these constants into config file
# Format: (short name, full name, url)
plant_templates = [
    ('4" philodendron pink princess', 'https://www.gabriellaplants.com/collections/home-page/products/4-pink-princess-philodendron'),
    ('5" philodendron jose buono', 'https://www.gabriellaplants.com/collections/home-page/products/5-philodendron-jose-buono'),
    ('5" philodendron jose buono', 'https://www.gabriellaplants.com/collections/home-page/products/4-jose-bueno-philodendron'),
    ('4" syngonium podophyllum albo-variegatum', 'https://www.gabriellaplants.com/collections/home-page/products/4-variegated-emerald-gem-syngonium-arrow-head-house-plant-nephthytis'),
    ('3" philodendron \'gabby\' sport', 'https://www.gabriellaplants.com/collections/home-page/products/3-gabby-philodendron-sport'),
    ('4" philodendron birkin', 'https://www.gabriellaplants.com/collections/home-page/products/4-philodendron-birkin')
]
# Email addresses to send to
toAddress = []
# My email secrets
my_email = ""
my_password = ""

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
