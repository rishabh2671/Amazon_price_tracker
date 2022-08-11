import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    global converted_price
    URL = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-Camera/dp/B07B43WPVK/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1598029539&sr=8-1'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)
    price1 = price.split('₹')
    price1 = price1[1]
    price1 = price1.replace(',', '')
    price1 = price1.replace(' ', '')
    print("after"+price1)
    cost = float(price1)

    if cost > 140990:
        sent_mail()

    print(cost)
    print(title.strip())



def sent_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('anshulcooldude02@gmail.com','apziwmllvcmdhuql')
    subject = 'Price Fell Down!'
    body = 'check amazon link below \n https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-Camera/dp/B07B43WPVK/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1598029539&sr=8-1'
    msg = f"subject={subject}\n\n{body}"
    server.sendmail('anshulcooldude02@gmail.com','nehakmr6195@gmail.com',msg)
    print("Hey Email has been Sent!")
    server.quit()

while(True):
    check_price()
    time.sleep(60)

