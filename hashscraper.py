#! /usr/bin/python

import hashlib
import bs4
import random
import time 
import yaml
import os 
import smtplib

sleeptime = 30

with open('Insert path of config file here','r') as file:
    doc = yaml.full_load(file)

toAddress = doc['toAddress']
plant_templates = doc['plant_templates'] 

my_email = os.environ['EMAIL']
my_password = os.environ['EMAILPASSWORD']

def hashFinder(url):
    try:
        getPage = requests.get(url)
        getPage.raise_for_status()
        page = bs4.BeautifulSoup(getPage.text, 'html.parser')
        return hashlib.sha224(page).hexdigest()
    except Exception as e:
        pass 

def main():
    currHash = []
    matched = []
    for template in plant_templates:
        url = template["url"]
        currHash.append(hashFinder(url))

    time.sleep(30)
    
    for i, template in enumerate(plant_templates):
        url = template["url"]
        newHash = hashFinder(url)
        print(newHash)
        print(currHash[i])
        if newHash != currHash[i]:
            matched.append(plant_templates[i])
        
        if matched:
            # Send to Gmail
            conn = smtplib.SMTP('smtp.gmail.com', 587)
            conn.ehlo()
            conn.starttls()
            conn.login(my_email, my_password)
            conn.sendmail(my_email, toAddress,
                    ('Insert email subject and body here.'))
            conn.quit()
 
if __name__ == "__main__":
    main()



