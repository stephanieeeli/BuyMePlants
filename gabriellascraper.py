#!/usr/bin/python
import bs4, requests, smtplib

toAddress = []
getPage = requests.get('https://www.gabriellaplants.com/collections/home-page?sort_by=price-descending')
getPage.raise_for_status()

inventory = bs4.BeautifulSoup(getPage.text, 'html.parser')
plants = inventory.select('.cd.chp')

plant_availability = False

ppp = '4" philodendron pink princess'
flength_ppp = len(ppp)
ppp_stock = False 

jose5 = '5" philodendron jose buono'
flength_jose5 = len(jose5)
jose5_stock = False

jose4 = '4" philodendron jose buono'
flength_jose4 = len(jose4)
jose4_stock = False 

syng4 = '4" syngonium podophyllum albo-variegatum'
flength_syng4 = len(syng4)
syng4_stock = False

gabby3 = '3" philodendron \'gabby\' sport'
flength_gabby3 = len(gabby3)
gabby3_stock = False

for plant in plants:
    for i in range(len(plant.text)):
        chunk_ppp = plant.text[i:i+flength_ppp].lower()
        chunk_jose5 = plant.text[i:i+flength_jose5].lower()
        chunk_jose4 = plant.text[i:i+flength_jose4].lower()
        chunk_syng4 = plant.text[i:i+flength_syng4].lower()
        chunk_gabby3 = plant.text[i:i+flength_gabby3].lower()
        if chunk_ppp == ppp:
            ppp_stock = True
            plant_availability = True
        if chunk_jose5 == jose5:
            jose5_stock = True
            plant_availability = True
        if chunk_jose4 == jose4:
            jose4_stock = True
            plant_availability = True 
        if chunk_syng4 == syng4:
            syng4_stock = True
            plant_availability = True
        if chunk_gabby3 == gabby3:
            gabby3_stock = True
            plant_availability = True

if plant_availability == True:
    conn = smtplin.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('put email here', 'email password')
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

