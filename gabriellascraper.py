#!/usr/bin/python
import bs4, requests, smtplib

toAddress = []
getPage = requests.get('https://www.gabriellaplants.com/collections/home-page?sort_by=price-descending')
getPage.raise_for_status()

inventory = bs4.BeautifulSoup(getPage.text, 'html.parser')
plants = inventory.select('.cd.chp')

plant_availability = False

ppp = '4" philodendron pink princess'
ppp_stock = False 

jose5 = '5" philodendron jose buono'
jose5_stock = False

jose4 = '4" philodendron jose buono'
jose4_stock = False 

syng4 = '4" syngonium podophyllum albo-variegatum'
syng4_stock = False

gabby3 = '3" philodendron \'gabby\' sport'
gabby3_stock = False

wantedplants = [ppp, jose5, jose4, syng4, gabby3]

for plant in plants:
    for want in wantedplants:
        flength = len(want)
        for i in range(len(plant.text)):
            chunk = plant.text[i:i+flength].lower()
            if chunk == ppp:
                ppp_stock = True
                plant_availability = True
            if chunk == jose5:
                jose5_stock = True
                plant_availability = True
            if chunk == jose4:
                jose4_stock = True
                plant_availability = True 
            if chunk == syng4:
                syng4_stock = True
                plant_availability = True
            if chunk == gabby3:
                gabby3_stock = True
                plant_availability = True

if plant_availability == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('enter email here', 'enter email password')
    if ppp_stock == True:
        conn.sendmail('put email here', toAddress,'Subject: PPP In Stock Alert\n\nCome get your PPP from Gabriella\'s!\n\nhttps://www.gabriellaplants.com/collections/home-page/products/4-pink-princess-philodendron\n\nPlant Notifier V1.0')
    if jose5_stock == True:
        conn.sendmail('put email here', toAddress, 'Subject: 5" Jose Buono In Stock Alert\n\nCome get your 5" Jose Buono from Gabriella\'s!\n\nhttps://www.gabriellaplants.com/collections/home-page/products/5-philodendron-jose-buono\n\nPlant Notifier V1.0')
    if jose4_stock == True:
        conn.sendmail('put email here', toAddress, 'Subject: 4" Jose Buono In Stock Alert\n\nCome get your 4" Jose Buono from Gabriella\'s!\n\nhttps://www.gabriellaplants.com/collections/home-page/products/4-jose-bueno-philodendron\n\nPlant Notifier V1.0')
    if syng4_stock == True:
        conn.sendmail('put email here', toAddress, 'Subject: 4" Albo Syngonium In Stock Alert\n\nCome get your 4" Albo Syngonium from Gabriella\'s!\n\nhttps://www.gabriellaplants.com/collections/home-page/products/4-variegated-emerald-gem-syngonium-arrow-head-house-plant-nephthytis\n\nPlant Notifier V1.0')
    if gabby3_stock == True:
        conn.sendmail('put email here', toAddress, 'Subject: 3" Gabby In Stock Alert\n\nCome get your 3" Gabby from Gabriella\'s!\n\nhttps://www.gabriellaplants.com/collections/home-page/products/3-gabby-philodendron-sport\n\nPlant Notifier V1.0')
    conn.quit()
    print('Sent notifs')
else:
    print('Out of stock')

