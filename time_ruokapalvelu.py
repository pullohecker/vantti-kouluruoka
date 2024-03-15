import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import argparse

parser = argparse.ArgumentParser("python3 ruokaservice.py")
parser.add_argument("server", help="The address or ip of your smtp server", type=str)
parser.add_argument("port", help="The port of your smtp server", type=str)
parser.add_argument("username", help="The username of your smtp server", type=str)
parser.add_argument("password", help="The password of you'r smtp server", type=str)
parser.add_argument("mailbox", help="The email address that you want the food info to be sent", type=str)

args = parser.parse_args()
smtp_server = args.server
smtp_port = args.port
smtp_email = args.username
smtp_pass = args.password
email = args.mailbox

options=Options()
options.add_argument("--headless=new")
aakkoset = {ord('ä'):'a', ord('ö'):'o', ord('å'):'oe'}

while True:
    time.sleep(5*60)
    t = time.localtime()
    th = t.tm_hour
    if (th == 7):
        
        web = webdriver.Chrome(options=options)
        web.get('https://aromimenu.cgisaas.fi/VantaaAromieMenus/FI/Default/Vantti/KoivukylaKO/Restaurant.aspx')

        vege = web.find_element(By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[1]')
        otsikko = web.find_element(By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/span[2]')
        liha = web.find_element(By.XPATH, '/html/body/form/div[3]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[5]/div/div/div[3]/div/div[1]/div/div[1]')
        otsikkotext_raw = str(otsikko.text)
        vegetext_raw = str(vege.text)
        lihatext_raw = str(liha.text)
        vegetext = vegetext_raw.translate(aakkoset)
        lihatext = lihatext_raw.translate(aakkoset)
        otsikkotext = otsikkotext_raw.translate(aakkoset)

        print(vegetext)
        print(lihatext)

        sender = "pullohecker@kouluruoka.jee"
        receiver = email

        message = f"""\
Subject: Tanaan ruokana koulussa {otsikkotext}
To: {receiver}
From: {sender}
{vegetext}

{lihatext}"""

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_email, smtp_pass)
            server.sendmail(sender, receiver, message)
        web.quit()
        time.sleep(100*60)
