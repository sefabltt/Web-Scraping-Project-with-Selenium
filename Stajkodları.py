
##### LÜTFEN RUNLADIKTAN SONRA SELENİUMUN GÜNLER İÇİN DATALARI ÇEKMESİ İÇİN EN AZ 20 SANİYE BEKLEYİNİZ #####

import time
import xml.etree.cElementTree as et
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://www.isbank.com.tr/doviz-kurlari"
browser.get(url)

tarih = '13/03/2024'
script = f"document.getElementById('dK_dateInput').value = '{tarih}';" # TARİH SEÇTİREBİLMEK İÇİN.
browser.execute_script(script)
tür = 'IS'
döviztürü = f"document.getElementById('fxRateType').value = '{tür}';" # DÖVİZ TÜRÜNÜ SEÇTİREBİLMEK İÇİN - İŞ BANKASI GİŞELERİNE GÖRE UYARLANDI.
browser.execute_script(döviztürü)

browser.execute_script("CallHandler();") ## TIKLATTIRABİLMEK İÇİN

time.sleep(5)

abddolarialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[2]').text
abddolarisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[3]').text

euroalis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[2]').text
eurosatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[3]').text

sterlinalis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[2]').text
sterlinsatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[3]').text

avustralyadolarialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[2]').text
avustralyadolarisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[3]').text

yuanalis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[2]').text
yuansatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[3]').text

danimarkakronualis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[2]').text
danimarkakronusatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[3]').text

isveckronualis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[2]').text
isveçkronusatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[3]').text

isviçrefrangıalis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[2]').text
isviçrefrangısatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[3]').text

japonyenialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[2]').text
japonyenisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[3]').text

kanadadolarıalis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[2]').text
kanadadolarisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[3]').text

kuveytdinarialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[2]').text
kuveytdinarisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[3]').text

norveçkronualis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[2]').text
norveçkronusatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[3]').text

rusrublesialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[2]').text
rusrublesisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[3]').text

suudiriyalialis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[2]').text
suudiriyalisatis = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[3]').text


## İŞ BANKASI 13 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##


abddolarispread = float(abddolarisatis) - float(abddolarialis)

eurospread = float(eurosatis) - float(euroalis)

sterlinspread = float(sterlinsatis) - float(sterlinalis)

avustralyadolarispread = float(avustralyadolarisatis) - float(avustralyadolarialis)

yuanspread = float(yuansatis) - float(yuanalis)

danimarkakronuspread = float(danimarkakronusatis) - float(danimarkakronualis)

isveckronuspread = float(isveçkronusatis) - float(isveckronualis)

isvicrefrangıspread = float(isviçrefrangısatis) - float(isviçrefrangıalis)

japonyenispread = float(japonyenisatis) - float(japonyenialis)

kanadadolarispread = float(kanadadolarisatis) - float(kanadadolarıalis)

kuveytdinarispread = float(kuveytdinarisatis) - float(kuveytdinarialis)

norveçkronuspread = float(norveçkronusatis) - float(norveçkronualis)

rusrublesispread = float(rusrublesisatis) - float(rusrublesialis)

suudiriyalispread = float(suudiriyalisatis) - float(suudiriyalialis)


data1 = {
    'USD': [float(abddolarialis),float(abddolarisatis), abddolarispread ],
    'EUR': [float(euroalis),float(eurosatis),eurospread],
    'GBP': [float(sterlinalis),float(sterlinsatis),sterlinspread],
    'AUD': [float(avustralyadolarialis),float(avustralyadolarisatis),avustralyadolarispread],
    'CNY': [float(yuanalis),float(yuansatis),yuanspread],
    'DKK': [float(danimarkakronualis),float(danimarkakronusatis),danimarkakronuspread],
    'SEK': [float(isveckronualis),float(isveçkronusatis),isveckronuspread],
    'CHF': [float(isviçrefrangıalis),float(isviçrefrangısatis),isvicrefrangıspread],
    'JPY': [float(japonyenialis),float(japonyenisatis),japonyenispread],
    'CAD': [float(kanadadolarıalis),float(kanadadolarisatis),kanadadolarispread],
    'KWD': [float(kuveytdinarialis),float(kuveytdinarisatis),kuveytdinarispread],
    'NOK': [float(norveçkronualis),float(norveçkronusatis),norveçkronuspread],
    'RUB': [float(rusrublesialis),float(rusrublesisatis),rusrublesispread],
    'SAR': [float(suudiriyalialis),float(suudiriyalisatis),suudiriyalispread]
}

df1 = pd.DataFrame(data1, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["İş Bankası Döviz Alış-13Mart","İş Bankası Döviz Satış-13Mart","İş Bankası Satış Alış Fark(Spread)-13Mart"])
#print(df1)

####################           MERKEZ BANKASI 13 MART 2024 KISMI              ################################


xml13 = et.ElementTree(file=urlopen("https://www.tcmb.gov.tr/kurlar/202403/13032024.xml")) # 13 MART 2024 MERKEZ BANKASI
root = xml13.getroot()

abddolari2 = root.findall("Currency")[0]
avustralyadolari2 = root.findall("Currency")[1]
danimarkakronu2 = root.findall("Currency")[2]
euro2 = root.findall("Currency")[3]
sterlin2 = root.findall("Currency")[4]
isvicrefrangı2 = root.findall("Currency")[5]
isveckronu2 = root.findall("Currency")[6]
kanadadolari2 = root.findall("Currency")[7]
kuveytdinari2 = root.findall("Currency")[8]
norveçkronu2 = root.findall("Currency")[9]
suudiriyali2 = root.findall("Currency")[10]
japonyeni2 = root.findall("Currency")[11]
rusrublesi2 = root.findall("Currency")[14] # bazı para birimleri iş bankasında olmadığı için indeksler atlandı.
yuan2 = root.findall("Currency")[16]

dolaralis2 = float(abddolari2.find("ForexBuying").text) # ABD DOLARI ALIŞ
dolarsatis2 = float(abddolari2.find("ForexSelling").text) # ABD DOLARI SATIŞ

avustralyadolaralis2 = float(avustralyadolari2.find("ForexBuying").text) # AVUSTRALYA DOLARI ALIŞ
avustralyadolarsatis2 = float(avustralyadolari2.find("ForexSelling").text) # AVUSTRALYA DOLARI SATIŞ

danimarkakronualis2 = float(danimarkakronu2.find("ForexBuying").text) # DANİMARKA KRONU ALIŞ
danimarkakronusatis2 = float(danimarkakronu2.find("ForexSelling").text) # DANİMARKA KRONU SATIŞ

euroalis2 = float(euro2.find("ForexBuying").text) # EURO ALIŞ
eurosatis2 = float(euro2.find("ForexSelling").text) # EURO SATIŞ

sterlinalis2 = float(sterlin2.find("ForexBuying").text) # İNGİLİZ STERLİNİ ALIŞ
sterlinsatis2 = float(sterlin2.find("ForexSelling").text) # İNGİLİZ STERLİNİ SATIŞ

isvicrefrangialis2 = float(isvicrefrangı2.find("ForexBuying").text) # İSVİÇRE FRANGI ALIŞ
isvicrefrangisatis2= float(isvicrefrangı2.find("ForexSelling").text) # İSVİÇRE FRANGI SATIŞ

isveckronualis2 = float(isveckronu2.find("ForexBuying").text) # İSVEÇ KRONU ALIŞ
isveckronusatis2 = float(isveckronu2.find("ForexSelling").text) # İSVEÇ KRONU SATIŞ

kanadadolarialis2 = float(kanadadolari2.find("ForexBuying").text) # KANADA DOLARI ALIŞ
kanadadolarisatis2 = float(kanadadolari2.find("ForexSelling").text) # KANADA DOLARI SATIŞ

kuveytdinarialis2 = float(kuveytdinari2.find("ForexBuying").text) # KUVEYT DİNARİ ALIŞ
kuveytdinarisatis2 = float(kuveytdinari2.find("ForexSelling").text) # KUVEYT DİNARİ SATIŞ

norveçkronualis2 = float(norveçkronu2.find("ForexBuying").text) # NORVEÇ KRONU ALIŞ
norveçkronusatis2 = float(norveçkronu2.find("ForexSelling").text) # NORVEÇ KRONU SATIŞ

suudiriyalialis2 = float(suudiriyali2.find("ForexBuying").text) # SUUDİ RİYALİ ALIŞ
suudiriyalisatis2 = float(suudiriyali2.find("ForexSelling").text) # SUUDİ RİYALİ SATIŞ

japonyenialis2 = float(japonyeni2.find("ForexBuying").text) / (100)  # JAPON YENİ ALIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.
japonyenisatis2 = float(japonyeni2.find("ForexSelling").text) / (100)  # JAPON YENİ SATIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.

rusrublesialis2 = float(rusrublesi2.find("ForexBuying").text) # RUS RUBLESİ ALIŞ
rusrublesisatis2 = float(rusrublesi2.find("ForexSelling").text) # RUS RUBLESİ SATIŞ

yuanalis2 = float(yuan2.find("ForexBuying").text) # ÇİN YUANI ALIŞ
yuansatis2 = float(yuan2.find("ForexSelling").text) # ÇİN YUANI SATIŞ

## MERKEZ BANKASI 13 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##

abddolarispread2 = dolarsatis2 - dolaralis2

eurospread2 = eurosatis2 - euroalis2

avustralyadolarispread2 = avustralyadolarsatis2 - avustralyadolaralis2

danimarkakronuspread2 = danimarkakronusatis2 - danimarkakronualis2

sterlinspread2 = sterlinsatis2 - sterlinalis2

isvicrefrangıspread2 = isvicrefrangisatis2 - isvicrefrangialis2

isveckronuspread2= isveckronusatis2 - isveckronualis2

kanadadolarispread2 = kanadadolarisatis2 - kanadadolarialis2

kuveytdinarispread2 = kuveytdinarisatis2 - kuveytdinarialis2

norveçkronuspread2 = norveçkronusatis2 - norveçkronualis2

suudiriyalispread2 = suudiriyalisatis2 - suudiriyalialis2

japonyenispread2 = japonyenisatis2 - japonyenialis2

rusrublesispread2 = rusrublesisatis2 - rusrublesialis2

yuanspread2 = yuansatis2 - yuanalis2

data2 = {
    'USD': [dolaralis2,dolarsatis2, abddolarispread2 ],
    'EUR': [euroalis2,eurosatis2,eurospread2],
    'GBP': [sterlinalis2,sterlinsatis2,sterlinspread2],
    'AUD': [avustralyadolaralis2,avustralyadolarsatis2,avustralyadolarispread2],
    'CNY': [yuanalis2,yuansatis2,avustralyadolarispread2],
    'DKK': [danimarkakronualis2,danimarkakronusatis2,danimarkakronuspread2],
    'SEK': [isveckronualis2,isveckronusatis2,isveckronuspread2],
    'CHF': [isvicrefrangialis2,isvicrefrangisatis2,isvicrefrangıspread2],
    'JPY': [japonyenialis2,japonyenisatis2,japonyenispread2],
    'CAD': [kanadadolarialis2,kanadadolarisatis2,kanadadolarispread2],
    'KWD': [kuveytdinarialis2,kuveytdinarisatis2,kuveytdinarispread2],
    'NOK': [norveçkronualis2,norveçkronusatis2,norveçkronuspread2],
    'RUB': [rusrublesialis2,rusrublesisatis2,avustralyadolarispread2],
    'SAR': [suudiriyalialis2,suudiriyalisatis2,suudiriyalispread2]
}

df2 = pd.DataFrame(data2, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["TCMB Döviz Alış-13Mart","TCMB Döviz Satış-13Mart","TCMB Satış Alış Fark(Spread)-13Mart"])
result1 = pd.concat([df2, df1], axis=0)
#print(result1)


#### FARKLILIK HESAPLAMA >>> MERKEZ BANKASI'NIN İŞ BANKASI'NDAN FARKI HESAPLANMIŞTIR(13 MART 2024) #####


abddolarialisfarki = float(abddolari2.find("ForexBuying").text) - float(abddolarialis)
abddolarisatisfarki = float(abddolari2.find("ForexSelling").text) - float(abddolarisatis)

avustralyadolarialisfarki = float(avustralyadolari2.find("ForexBuying").text) - float(avustralyadolarialis)
avustralyadolarisatisfarki = float(avustralyadolari2.find("ForexSelling").text) - float(avustralyadolarisatis)

danimarkakronualisfarki = float(danimarkakronu2.find("ForexBuying").text) - float(danimarkakronualis)
danimarkakronusatisfarki = float(danimarkakronu2.find("ForexSelling").text) - float(danimarkakronusatis)

euroalisfarki = float(euro2.find("ForexBuying").text) - float(euroalis)
eurosatisfarki = float(euro2.find("ForexSelling").text) - float(eurosatis)

sterlinalisfarki = float(sterlin2.find("ForexBuying").text) - float(sterlinalis)
sterlinsatisfarki = float(sterlin2.find("ForexSelling").text) - float(sterlinsatis)

isvicrefrangialisfarki = float(isvicrefrangı2.find("ForexBuying").text) - float(isviçrefrangıalis)
isvicrefrangisatisfarki = float(isvicrefrangı2.find("ForexSelling").text) - float(isviçrefrangısatis)

isveçkronualisfarki = float(isveckronu2.find("ForexBuying").text) - float(isveckronualis)
isveçkronusatisfarki = float(isveckronu2.find("ForexSelling").text) - float(isveçkronusatis)

kanadadolarıalisfarki = float(kanadadolari2.find("ForexBuying").text) - float(kanadadolarıalis)
kanadadolarısatisfarki = float(kanadadolari2.find("ForexSelling").text) - float(kanadadolarıalis)

kuveytdinarialisfarki = float(kuveytdinari2.find("ForexBuying").text) - float(kuveytdinarialis)
kuveytdinarisatisfarki = float(kuveytdinari2.find("ForexSelling").text) - float(kuveytdinarisatis)

norveçkronualisfarki = float(norveçkronu2.find("ForexBuying").text) - float(norveçkronualis)
norveçkronusatisfarki = float(norveçkronu2.find("ForexSelling").text) - float(norveçkronusatis)

suudiriyalialisfarki = float(suudiriyali2.find("ForexBuying").text) - float(suudiriyalialis)
suudiriyalisatisfarki = float(suudiriyali2.find("ForexSelling").text) - float(suudiriyalisatis)

japonyenialisfarki = (float(japonyeni2.find("ForexBuying").text) / (100) ) - float(japonyenialis) ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.
japonyenisatisfarki = (float(japonyeni2.find("ForexSelling").text) / (100) ) - float(japonyenisatis) ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.

rusrublesialisfarki = float(rusrublesi2.find("ForexBuying").text) - float(rusrublesialis)
rusrublesisatisfarki = float(rusrublesi2.find("ForexSelling").text) - float(rusrublesisatis)

yuanalisfarki = float(yuan2.find("ForexBuying").text) - float(yuanalis)
yuansatisfarki = float(yuan2.find("ForexSelling").text) - float(yuansatis)


data3 = {
    'USD': [abddolarialisfarki,abddolarisatisfarki],
    'EUR': [euroalisfarki,eurosatisfarki],
    'GBP': [sterlinalisfarki,sterlinsatisfarki],
    'AUD': [avustralyadolarialisfarki,avustralyadolarisatisfarki],
    'CNY': [yuanalisfarki,yuansatisfarki],
    'DKK': [danimarkakronualisfarki,danimarkakronusatisfarki],
    'SEK': [isveçkronualisfarki,isveçkronusatisfarki],
    'CHF': [isvicrefrangialisfarki,isvicrefrangisatisfarki],
    'JPY': [round(japonyenialisfarki,4),japonyenisatisfarki], ## JAPON YENİ ÇOK KÜÇÜK BİR FARK VAR BU YÜZDEN YUVARLADIK.
    'CAD': [kanadadolarıalisfarki,kanadadolarısatisfarki],
    'KWD': [kuveytdinarialisfarki,kuveytdinarisatisfarki],
    'NOK': [norveçkronualisfarki,norveçkronusatisfarki],
    'RUB': [rusrublesialisfarki,rusrublesisatisfarki],
    'SAR': [suudiriyalialisfarki,suudiriyalisatisfarki]
}

df3 = pd.DataFrame(data3, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["Bankalar arası döviz alış farkı-13Mart","Bankalar arası döviz satış farkı-13Mart"])

result2 = pd.concat([result1, df3], axis=0)

# print(result2)
# result2.to_excel('13Mart2024.xlsx', index=True)



########################################       12 MART 2024  MERKEZ BANKASI            #######################################

xml12 = et.ElementTree(file=urlopen("https://www.tcmb.gov.tr/kurlar/202403/12032024.xml")) # 12 MART 2024 MERKEZ BANKASI
root = xml12.getroot()

abddolari3 = root.findall("Currency")[0]
avustralyadolari3 = root.findall("Currency")[1]
danimarkakronu3 = root.findall("Currency")[2]
euro3 = root.findall("Currency")[3]
sterlin3 = root.findall("Currency")[4]
isvicrefrangı3 = root.findall("Currency")[5]
isveckronu3 = root.findall("Currency")[6]
kanadadolari3 = root.findall("Currency")[7]
kuveytdinari3 = root.findall("Currency")[8]
norveçkronu3 = root.findall("Currency")[9]
suudiriyali3 = root.findall("Currency")[10]
japonyeni3 = root.findall("Currency")[11]
rusrublesi3 = root.findall("Currency")[14] # bazı para birimleri iş bankasında olmadığı için indeksler atlandı.
yuan3 = root.findall("Currency")[16]

dolaralis3 = float(abddolari3.find("ForexBuying").text) # ABD DOLARI ALIŞ
dolarsatis3 = float(abddolari3.find("ForexSelling").text) # ABD DOLARI SATIŞ

avustralyadolaralis3 = float(avustralyadolari3.find("ForexBuying").text) # AVUSTRALYA DOLARI ALIŞ
avustralyadolarsatis3 = float(avustralyadolari3.find("ForexSelling").text) # AVUSTRALYA DOLARI SATIŞ

danimarkakronualis3 = float(danimarkakronu3.find("ForexBuying").text) # DANİMARKA KRONU ALIŞ
danimarkakronusatis3 = float(danimarkakronu3.find("ForexSelling").text) # DANİMARKA KRONU SATIŞ

euroalis3 = float(euro3.find("ForexBuying").text) # EURO ALIŞ
eurosatis3 = float(euro3.find("ForexSelling").text) # EURO SATIŞ

sterlinalis3 = float(sterlin3.find("ForexBuying").text) # İNGİLİZ STERLİNİ ALIŞ
sterlinsatis3 = float(sterlin3.find("ForexSelling").text) # İNGİLİZ STERLİNİ SATIŞ

isvicrefrangialis3 = float(isvicrefrangı3.find("ForexBuying").text) # İSVİÇRE FRANGI ALIŞ
isvicrefrangisatis3= float(isvicrefrangı3.find("ForexSelling").text) # İSVİÇRE FRANGI SATIŞ

isveckronualis3 = float(isveckronu3.find("ForexBuying").text) # İSVEÇ KRONU ALIŞ
isveckronusatis3 = float(isveckronu3.find("ForexSelling").text) # İSVEÇ KRONU SATIŞ

kanadadolarialis3 = float(kanadadolari3.find("ForexBuying").text) # KANADA DOLARI ALIŞ
kanadadolarisatis3 = float(kanadadolari3.find("ForexSelling").text) # KANADA DOLARI SATIŞ

kuveytdinarialis3 = float(kuveytdinari3.find("ForexBuying").text) # KUVEYT DİNARİ ALIŞ
kuveytdinarisatis3 = float(kuveytdinari3.find("ForexSelling").text) # KUVEYT DİNARİ SATIŞ

norveçkronualis3 = float(norveçkronu3.find("ForexBuying").text) # NORVEÇ KRONU ALIŞ
norveçkronusatis3 = float(norveçkronu3.find("ForexSelling").text) # NORVEÇ KRONU SATIŞ

suudiriyalialis3 = float(suudiriyali3.find("ForexBuying").text) # SUUDİ RİYALİ ALIŞ
suudiriyalisatis3 = float(suudiriyali3.find("ForexSelling").text) # SUUDİ RİYALİ SATIŞ

japonyenialis3 = float(japonyeni3.find("ForexBuying").text) / (100)  # JAPON YENİ ALIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.
japonyenisatis3 = float(japonyeni3.find("ForexSelling").text) / (100)  # JAPON YENİ SATIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.

rusrublesialis3 = float(rusrublesi3.find("ForexBuying").text) # RUS RUBLESİ ALIŞ
rusrublesisatis3 = float(rusrublesi3.find("ForexSelling").text) # RUS RUBLESİ SATIŞ

yuanalis3 = float(yuan3.find("ForexBuying").text) # ÇİN YUANI ALIŞ
yuansatis3 = float(yuan3.find("ForexSelling").text) # ÇİN YUANI SATIŞ

## MERKEZ BANKASI 12 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##

abddolarispread3 = dolarsatis3 - dolaralis3

eurospread3 = eurosatis3 - euroalis3

avustralyadolarispread3 = avustralyadolarsatis3 - avustralyadolaralis3

danimarkakronuspread3 = danimarkakronusatis3 - danimarkakronualis3

sterlinspread3 = sterlinsatis3 - sterlinalis3

isvicrefrangıspread3 = isvicrefrangisatis3 - isvicrefrangialis3

isveckronuspread3 = isveckronusatis3 - isveckronualis3

kanadadolarispread3 = kanadadolarisatis3 - kanadadolarialis3

kuveytdinarispread3 = kuveytdinarisatis3 - kuveytdinarialis3

norveçkronuspread3 = norveçkronusatis3 - norveçkronualis3

suudiriyalispread3 = suudiriyalisatis3 - suudiriyalialis3

japonyenispread3 = japonyenisatis3 - japonyenialis3

rusrublesispread3 = rusrublesisatis3 - rusrublesialis3

yuanspread3 = yuansatis3 - yuanalis3

data4 = {
    'USD': [dolaralis3,dolarsatis3, abddolarispread3 ],
    'EUR': [euroalis3,eurosatis3,eurospread3],
    'GBP': [sterlinalis3,sterlinsatis3,sterlinspread3],
    'AUD': [avustralyadolaralis3,avustralyadolarsatis3,avustralyadolarispread3],
    'CNY': [yuanalis3,yuansatis3,yuanspread3],
    'DKK': [danimarkakronualis3,danimarkakronusatis3,danimarkakronuspread3],
    'SEK': [isveckronualis3,isveckronusatis3,isveckronuspread3],
    'CHF': [isvicrefrangialis3,isvicrefrangisatis3,isvicrefrangıspread3],
    'JPY': [japonyenialis3,japonyenisatis3,japonyenispread3],
    'CAD': [kanadadolarialis3,kanadadolarisatis3,kanadadolarispread3],
    'KWD': [kuveytdinarialis3,kuveytdinarisatis3,kuveytdinarispread3],
    'NOK': [norveçkronualis3,norveçkronusatis3,norveçkronuspread3],
    'RUB': [rusrublesialis3,rusrublesisatis3,rusrublesispread3],
    'SAR': [suudiriyalialis3,suudiriyalisatis3,suudiriyalispread3]
}

df4 = pd.DataFrame(data4, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["TCMB Döviz Alış-12Mart","TCMB Döviz Satış-12Mart","TCMB Satış Alış Fark(Spread)-12Mart"])
#print(df4)

########### İŞ BANKASI 12 MART 2024 #######################


url2 = "https://www.isbank.com.tr/doviz-kurlari"
browser.get(url2)

tarih2 = '12/03/2024'
script2 = f"document.getElementById('dK_dateInput').value = '{tarih2}';" # TARİH SEÇTİREBİLMEK İÇİN.
browser.execute_script(script2)
tür2 = 'IS'
döviztürü2 = f"document.getElementById('fxRateType').value = '{tür2}';" # DÖVİZ TÜRÜNÜ SEÇTİREBİLMEK İÇİN - İŞ BANKASI GİŞELERİNE GÖRE UYARLANDI.
browser.execute_script(döviztürü2)

browser.execute_script("CallHandler();") ## TIKLATTIRABİLMEK İÇİN

time.sleep(5)


abddolarialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[2]').text
abddolarisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[3]').text

euroalis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[2]').text
eurosatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[3]').text

sterlinalis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[2]').text
sterlinsatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[3]').text

avustralyadolarialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[2]').text
avustralyadolarisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[3]').text

yuanalis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[2]').text
yuansatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[3]').text

danimarkakronualis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[2]').text
danimarkakronusatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[3]').text

isveckronualis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[2]').text
isveçkronusatis4= browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[3]').text

isviçrefrangıalis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[2]').text
isviçrefrangısatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[3]').text

japonyenialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[2]').text
japonyenisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[3]').text

kanadadolarıalis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[2]').text
kanadadolarisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[3]').text

kuveytdinarialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[2]').text
kuveytdinarisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[3]').text

norveçkronualis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[2]').text
norveçkronusatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[3]').text

rusrublesialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[2]').text
rusrublesisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[3]').text

suudiriyalialis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[2]').text
suudiriyalisatis4 = browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[3]').text




## İŞ BANKASI 12 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##



abddolarispread4 = float(abddolarisatis4) - float(abddolarialis4)

eurospread4 = float(eurosatis4) - float(euroalis4)

sterlinspread4 = float(sterlinsatis4) - float(sterlinalis4)

avustralyadolarispread4 = float(avustralyadolarisatis4) - float(avustralyadolarialis4)

yuanspread4 = float(yuansatis4) - float(yuanalis4)

danimarkakronuspread4 = float(danimarkakronusatis4) - float(danimarkakronualis4)

isveckronuspread4 = float(isveçkronusatis4) - float(isveckronualis4)

isvicrefrangıspread4 = float(isviçrefrangısatis4) - float(isviçrefrangıalis4)

japonyenispread4 = float(japonyenisatis4) - float(japonyenialis4)

kanadadolarispread4 = float(kanadadolarisatis4) - float(kanadadolarıalis4)

kuveytdinarispread4 = float(kuveytdinarisatis) - float(kuveytdinarialis)

norveçkronuspread4 = float(norveçkronusatis) - float(norveçkronualis)

rusrublesispread4 = float(rusrublesisatis) - float(rusrublesialis)

suudiriyalispread4 = float(suudiriyalisatis) - float(suudiriyalialis)


data5 = {
    'USD': [float(abddolarialis4),float(abddolarisatis), abddolarispread4 ],
    'EUR': [float(euroalis4),float(eurosatis4),eurospread4],
    'GBP': [float(sterlinalis4),float(sterlinsatis4),sterlinspread4],
    'AUD': [float(avustralyadolarialis4),float(avustralyadolarisatis4),avustralyadolarispread4],
    'CNY': [float(yuanalis4),float(yuansatis4),yuanspread4],
    'DKK': [float(danimarkakronualis4),float(danimarkakronusatis4),danimarkakronuspread4],
    'SEK': [float(isveckronualis4),float(isveçkronusatis4),isveckronuspread4],
    'CHF': [float(isviçrefrangıalis4),float(isviçrefrangısatis4),isvicrefrangıspread4],
    'JPY': [float(japonyenialis4),float(japonyenisatis4),japonyenispread4],
    'CAD': [float(kanadadolarıalis4),float(kanadadolarisatis4),kanadadolarispread4],
    'KWD': [float(kuveytdinarialis4),float(kuveytdinarisatis4),kuveytdinarispread4],
    'NOK': [float(norveçkronualis4),float(norveçkronusatis4),norveçkronuspread4],
    'RUB': [float(rusrublesialis4),float(rusrublesisatis4),rusrublesispread4],
    'SAR': [float(suudiriyalialis4),float(suudiriyalisatis4),suudiriyalispread4]
}

df5 = pd.DataFrame(data5, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["İş Bankası Döviz Alış-12Mart","İş Bankası Döviz Satış-12Mart","İş Bankası Satış Alış Fark(Spread)-12Mart"])
result3 = pd.concat([df4, df5], axis=0)
#print(result3)

#### FARKLILIK HESAPLAMA >>> MERKEZ BANKASI'NIN İŞ BANKASI'NDAN FARKI HESAPLANMIŞTIR(12 MART 2024) #####


abddolarialisfarki2 = float(abddolari3.find("ForexBuying").text) - float(abddolarialis4)
abddolarisatisfarki2 = float(abddolari3.find("ForexSelling").text) - float(abddolarisatis4)

avustralyadolarialisfarki2 = float(avustralyadolari3.find("ForexBuying").text) - float(avustralyadolarialis4)
avustralyadolarisatisfarki2 = float(avustralyadolari3.find("ForexSelling").text) - float(avustralyadolarisatis4)

danimarkakronualisfarki2 = float(danimarkakronu3.find("ForexBuying").text) - float(danimarkakronualis4)
danimarkakronusatisfarki2 = float(danimarkakronu3.find("ForexSelling").text) - float(danimarkakronusatis4)

euroalisfarki2 = float(euro3.find("ForexBuying").text) - float(euroalis4)
eurosatisfarki2 = float(euro3.find("ForexSelling").text) - float(eurosatis4)

sterlinalisfarki2 = float(sterlin3.find("ForexBuying").text) - float(sterlinalis4)
sterlinsatisfarki2 = float(sterlin3.find("ForexSelling").text) - float(sterlinsatis4)

isvicrefrangialisfarki2 = float(isvicrefrangı3.find("ForexBuying").text) - float(isviçrefrangıalis4)
isvicrefrangisatisfarki2 = float(isvicrefrangı3.find("ForexSelling").text) - float(isviçrefrangısatis4)

isveçkronualisfarki2 = float(isveckronu3.find("ForexBuying").text) - float(isveckronualis4)
isveçkronusatisfarki2 = float(isveckronu3.find("ForexSelling").text) - float(isveçkronusatis4)

kanadadolarıalisfarki2 = float(kanadadolari3.find("ForexBuying").text) - float(kanadadolarıalis4)
kanadadolarısatisfarki2 = float(kanadadolari3.find("ForexSelling").text) - float(kanadadolarıalis4)

kuveytdinarialisfarki2 = float(kuveytdinari3.find("ForexBuying").text) - float(kuveytdinarialis4)
kuveytdinarisatisfarki2 = float(kuveytdinari3.find("ForexSelling").text) - float(kuveytdinarisatis4)

norveçkronualisfarki2 = float(norveçkronu3.find("ForexBuying").text) - float(norveçkronualis4)
norveçkronusatisfarki2 = float(norveçkronu3.find("ForexSelling").text) - float(norveçkronusatis4)

suudiriyalialisfarki2 = float(suudiriyali3.find("ForexBuying").text) - float(suudiriyalialis4)
suudiriyalisatisfarki2 = float(suudiriyali3.find("ForexSelling").text) - float(suudiriyalisatis4)

japonyenialisfarki2 = (float(japonyeni3.find("ForexBuying").text) / (100) ) - float(japonyenialis4) ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.
japonyenisatisfarki2 = (float(japonyeni3.find("ForexSelling").text) / (100) ) - float(japonyenisatis4) ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.

rusrublesialisfarki2 = float(rusrublesi3.find("ForexBuying").text) - float(rusrublesialis4)
rusrublesisatisfarki2 = float(rusrublesi3.find("ForexSelling").text) - float(rusrublesisatis4)

yuanalisfarki2 = float(yuan3.find("ForexBuying").text) - float(yuanalis4)
yuansatisfarki2 = float(yuan3.find("ForexSelling").text) - float(yuansatis4)


data6 = {
    'USD': [abddolarialisfarki2,abddolarisatisfarki2],
    'EUR': [euroalisfarki2,eurosatisfarki2],
    'GBP': [sterlinalisfarki2,sterlinsatisfarki2],
    'AUD': [avustralyadolarialisfarki2,avustralyadolarisatisfarki2],
    'CNY': [yuanalisfarki2,yuansatisfarki2],
    'DKK': [danimarkakronualisfarki2,danimarkakronusatisfarki2],
    'SEK': [isveçkronualisfarki2,isveçkronusatisfarki2],
    'CHF': [isvicrefrangialisfarki2,isvicrefrangisatisfarki2],
    'JPY': [japonyenialisfarki2,japonyenisatisfarki2],
    'CAD': [kanadadolarıalisfarki2,kanadadolarısatisfarki2],
    'KWD': [kuveytdinarialisfarki2,kuveytdinarisatisfarki2],
    'NOK': [norveçkronualisfarki2,norveçkronusatisfarki2],
    'RUB': [rusrublesialisfarki2,rusrublesisatisfarki2],
    'SAR': [suudiriyalialisfarki2,suudiriyalisatisfarki2]
}

df6 = pd.DataFrame(data6, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["Bankalar arası döviz alış farkı-12Mart","Bankalar arası döviz satış farkı-12Mart"])

result4 = pd.concat([result3, df6], axis=0)

#####print(result4)
#####result4.to_excel('12Mart2024.xlsx', index=True)


########################################       14 MART 2024  MERKEZ BANKASI            #######################################

xml14 = et.ElementTree(file=urlopen("https://www.tcmb.gov.tr/kurlar/202403/14032024.xml")) # 14 MART 2024 MERKEZ BANKASI
root = xml14.getroot()

abddolari5 = root.findall("Currency")[0]
avustralyadolari5 = root.findall("Currency")[1]
danimarkakronu5 = root.findall("Currency")[2]
euro5 = root.findall("Currency")[3]
sterlin5 = root.findall("Currency")[4]
isvicrefrangı5 = root.findall("Currency")[5]
isveckronu5 = root.findall("Currency")[6]
kanadadolari5 = root.findall("Currency")[7]
kuveytdinari5 = root.findall("Currency")[8]
norveçkronu5 = root.findall("Currency")[9]
suudiriyali5 = root.findall("Currency")[10]
japonyeni5 = root.findall("Currency")[11]
rusrublesi5 = root.findall("Currency")[14] # bazı para birimleri iş bankasında olmadığı için indeksler atlandı.
yuan5 = root.findall("Currency")[16]

dolaralis5 = float(abddolari5.find("ForexBuying").text) # ABD DOLARI ALIŞ
dolarsatis5 = float(abddolari5.find("ForexSelling").text) # ABD DOLARI SATIŞ

avustralyadolaralis5 = float(avustralyadolari5.find("ForexBuying").text) # AVUSTRALYA DOLARI ALIŞ
avustralyadolarsatis5 = float(avustralyadolari5.find("ForexSelling").text) # AVUSTRALYA DOLARI SATIŞ

danimarkakronualis5 = float(danimarkakronu5.find("ForexBuying").text) # DANİMARKA KRONU ALIŞ
danimarkakronusatis5 = float(danimarkakronu5.find("ForexSelling").text) # DANİMARKA KRONU SATIŞ

euroalis5 = float(euro5.find("ForexBuying").text) # EURO ALIŞ
eurosatis5 = float(euro5.find("ForexSelling").text) # EURO SATIŞ

sterlinalis5 = float(sterlin5.find("ForexBuying").text) # İNGİLİZ STERLİNİ ALIŞ
sterlinsatis5 = float(sterlin5.find("ForexSelling").text) # İNGİLİZ STERLİNİ SATIŞ

isvicrefrangialis5 = float(isvicrefrangı5.find("ForexBuying").text) # İSVİÇRE FRANGI ALIŞ
isvicrefrangisatis5= float(isvicrefrangı5.find("ForexSelling").text) # İSVİÇRE FRANGI SATIŞ

isveckronualis5 = float(isveckronu5.find("ForexBuying").text) # İSVEÇ KRONU ALIŞ
isveckronusatis5 = float(isveckronu5.find("ForexSelling").text) # İSVEÇ KRONU SATIŞ

kanadadolarialis5 = float(kanadadolari5.find("ForexBuying").text) # KANADA DOLARI ALIŞ
kanadadolarisatis5 = float(kanadadolari5.find("ForexSelling").text) # KANADA DOLARI SATIŞ

kuveytdinarialis5 = float(kuveytdinari5.find("ForexBuying").text) # KUVEYT DİNARİ ALIŞ
kuveytdinarisatis5 = float(kuveytdinari5.find("ForexSelling").text) # KUVEYT DİNARİ SATIŞ

norveçkronualis5 = float(norveçkronu5.find("ForexBuying").text) # NORVEÇ KRONU ALIŞ
norveçkronusatis5 = float(norveçkronu5.find("ForexSelling").text) # NORVEÇ KRONU SATIŞ

suudiriyalialis5 = float(suudiriyali5.find("ForexBuying").text) # SUUDİ RİYALİ ALIŞ
suudiriyalisatis5 = float(suudiriyali5.find("ForexSelling").text) # SUUDİ RİYALİ SATIŞ

japonyenialis5 = float(japonyeni5.find("ForexBuying").text) / (100)  # JAPON YENİ ALIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.
japonyenisatis5 = float(japonyeni5.find("ForexSelling").text) / (100)  # JAPON YENİ SATIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.

rusrublesialis5 = float(rusrublesi5.find("ForexBuying").text) # RUS RUBLESİ ALIŞ
rusrublesisatis5 = float(rusrublesi5.find("ForexSelling").text) # RUS RUBLESİ SATIŞ

yuanalis5 = float(yuan5.find("ForexBuying").text) # ÇİN YUANI ALIŞ
yuansatis5 = float(yuan5.find("ForexSelling").text) # ÇİN YUANI SATIŞ

## MERKEZ BANKASI 14 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##

abddolarispread5 = dolarsatis5 - dolaralis5

eurospread5 = eurosatis5 - euroalis5

avustralyadolarispread5 = avustralyadolarsatis5 - avustralyadolaralis5

danimarkakronuspread5 = danimarkakronusatis5 - danimarkakronualis5

sterlinspread5 = sterlinsatis5 - sterlinalis5

isvicrefrangıspread5 = isvicrefrangisatis5 - isvicrefrangialis5

isveckronuspread5 = isveckronusatis5 - isveckronualis5

kanadadolarispread5 = kanadadolarisatis5 - kanadadolarialis5

kuveytdinarispread5 = kuveytdinarisatis5 - kuveytdinarialis5

norveçkronuspread5 = norveçkronusatis5 - norveçkronualis5

suudiriyalispread5 = suudiriyalisatis5 - suudiriyalialis5

japonyenispread5 = japonyenisatis5 - japonyenialis5

rusrublesispread5 = rusrublesisatis5 - rusrublesialis5

yuanspread5 = yuansatis5 - yuanalis5

data7 = {
    'USD': [dolaralis5,dolarsatis5, abddolarispread5],
    'EUR': [euroalis5,eurosatis5,eurospread5],
    'GBP': [sterlinalis5,sterlinsatis5,sterlinspread5],
    'AUD': [avustralyadolaralis5,avustralyadolarsatis5,avustralyadolarispread5],
    'CNY': [yuanalis5,yuansatis5,yuanspread5],
    'DKK': [danimarkakronualis5,danimarkakronusatis5,danimarkakronuspread5],
    'SEK': [isveckronualis5,isveckronusatis5,isveckronuspread5],
    'CHF': [isvicrefrangialis5,isvicrefrangisatis5,isvicrefrangıspread5],
    'JPY': [japonyenialis5,japonyenisatis5,japonyenispread5],
    'CAD': [kanadadolarialis5,kanadadolarisatis5,kanadadolarispread5],
    'KWD': [kuveytdinarialis5,kuveytdinarisatis5,kuveytdinarispread5],
    'NOK': [norveçkronualis5,norveçkronusatis5,norveçkronuspread5],
    'RUB': [rusrublesialis5,rusrublesisatis5,rusrublesispread5],
    'SAR': [suudiriyalialis5,suudiriyalisatis5,suudiriyalispread5]
}

df7 = pd.DataFrame(data7, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["TCMB Döviz Alış-14Mart","TCMB Döviz Satış-14Mart","TCMB Satış Alış Fark(Spread)-14Mart"])
#print(df7)

########### İŞ BANKASI 14 MART 2024 #######################


url3 = "https://www.isbank.com.tr/doviz-kurlari"
browser.get(url3)

tarih3 = '14/03/2024'
script3 = f"document.getElementById('dK_dateInput').value = '{tarih3}';" # TARİH SEÇTİREBİLMEK İÇİN.
browser.execute_script(script3)
tür3 = 'IS'
döviztürü3 = f"document.getElementById('fxRateType').value = '{tür3}';" # DÖVİZ TÜRÜNÜ SEÇTİREBİLMEK İÇİN - İŞ BANKASI GİŞELERİNE GÖRE UYARLANDI.
browser.execute_script(döviztürü3)

browser.execute_script("CallHandler();") ## TIKLATTIRABİLMEK İÇİN

time.sleep(5)


abddolarialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[2]').text)
abddolarisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[3]').text)

euroalis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[2]').text)
eurosatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[3]').text)

sterlinalis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[2]').text)
sterlinsatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[3]').text)

avustralyadolarialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[2]').text)
avustralyadolarisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[3]').text)

yuanalis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[2]').text)
yuansatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[3]').text)

danimarkakronualis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[2]').text)
danimarkakronusatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[3]').text)

isveckronualis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[2]').text)
isveçkronusatis6= float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[3]').text)

isviçrefrangıalis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[2]').text)
isviçrefrangısatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[3]').text)

japonyenialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[2]').text)
japonyenisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[3]').text)

kanadadolarıalis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[2]').text)
kanadadolarisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[3]').text)

kuveytdinarialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[2]').text)
kuveytdinarisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[3]').text)

norveçkronualis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[2]').text)
norveçkronusatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[3]').text)

rusrublesialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[2]').text)
rusrublesisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[3]').text)

suudiriyalialis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[2]').text)
suudiriyalisatis6 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[3]').text)




## İŞ BANKASI 14 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##



abddolarispread6 = abddolarisatis6 - abddolarialis6

eurospread6 = eurosatis6 - euroalis6

sterlinspread6 = sterlinsatis6 - sterlinalis6

avustralyadolarispread6 = avustralyadolarisatis6 - avustralyadolarialis6

yuanspread6 = yuansatis6 - yuanalis6

danimarkakronuspread6 = danimarkakronusatis6 - danimarkakronualis6

isveckronuspread6 = isveçkronusatis6 - isveckronualis6

isvicrefrangıspread6 = isviçrefrangısatis6 - isviçrefrangıalis6

japonyenispread6 = japonyenisatis6 - japonyenialis6

kanadadolarispread6 = kanadadolarisatis6 - kanadadolarıalis6

kuveytdinarispread6 = kuveytdinarisatis6 - kuveytdinarialis6

norveçkronuspread6 = norveçkronusatis6 - norveçkronualis6

rusrublesispread6 = rusrublesisatis6 - rusrublesialis6

suudiriyalispread6 = suudiriyalisatis6 - suudiriyalialis6


data8 = {
    'USD': [abddolarialis6,abddolarisatis6, abddolarispread6 ],
    'EUR': [euroalis6,eurosatis6,eurospread6],
    'GBP': [sterlinalis6,sterlinsatis6,sterlinspread6],
    'AUD': [avustralyadolarialis6,avustralyadolarisatis6,avustralyadolarispread6],
    'CNY': [yuanalis6,yuansatis6,yuanspread6],
    'DKK': [danimarkakronualis6,danimarkakronusatis6,danimarkakronuspread6],
    'SEK': [isveckronualis6,isveçkronusatis6,isveckronuspread6],
    'CHF': [isviçrefrangıalis6,isviçrefrangısatis6,isvicrefrangıspread6],
    'JPY': [japonyenialis6,japonyenisatis6,japonyenispread6],
    'CAD': [kanadadolarıalis6,kanadadolarisatis6,kanadadolarispread6],
    'KWD': [kuveytdinarialis6,kuveytdinarisatis6,kuveytdinarispread6],
    'NOK': [norveçkronualis6,norveçkronusatis6,norveçkronuspread6],
    'RUB': [rusrublesialis6,rusrublesisatis6,rusrublesispread6],
    'SAR': [suudiriyalialis6,suudiriyalisatis6,suudiriyalispread6]
}

df8 = pd.DataFrame(data8, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["İş Bankası Döviz Alış-14Mart","İş Bankası Döviz Satış-14Mart","İş Bankası Satış Alış Fark(Spread)-14Mart"])
result5 = pd.concat([df7, df8], axis=0)
#print(result5)

#### FARKLILIK HESAPLAMA >>> MERKEZ BANKASI'NIN İŞ BANKASI'NDAN FARKI HESAPLANMIŞTIR(14 MART 2024) #####


abddolarialisfarki3 = float(abddolari5.find("ForexBuying").text) - abddolarialis6
abddolarisatisfarki3 = float(abddolari5.find("ForexSelling").text) - abddolarisatis6

avustralyadolarialisfarki3 = float(avustralyadolari5.find("ForexBuying").text) - avustralyadolarialis6
avustralyadolarisatisfarki3 = float(avustralyadolari5.find("ForexSelling").text) - avustralyadolarisatis6

danimarkakronualisfarki3 = float(danimarkakronu5.find("ForexBuying").text) - danimarkakronualis6
danimarkakronusatisfarki3 = float(danimarkakronu5.find("ForexSelling").text) - danimarkakronusatis6

euroalisfarki3 = float(euro5.find("ForexBuying").text) - euroalis6
eurosatisfarki3 = float(euro5.find("ForexSelling").text) - eurosatis6

sterlinalisfarki3 = float(sterlin5.find("ForexBuying").text) - sterlinalis6
sterlinsatisfarki3 = float(sterlin5.find("ForexSelling").text) - sterlinsatis6

isvicrefrangialisfarki3 = float(isvicrefrangı5.find("ForexBuying").text) - isviçrefrangıalis6
isvicrefrangisatisfarki3 = float(isvicrefrangı5.find("ForexSelling").text) - isviçrefrangısatis6

isveçkronualisfarki3 = float(isveckronu5.find("ForexBuying").text) - isveckronualis6
isveçkronusatisfarki3 = float(isveckronu5.find("ForexSelling").text) - isveçkronusatis6

kanadadolarıalisfarki3 = float(kanadadolari5.find("ForexBuying").text) - kanadadolarıalis6
kanadadolarısatisfarki3 = float(kanadadolari5.find("ForexSelling").text) - kanadadolarıalis6

kuveytdinarialisfarki3 = float(kuveytdinari5.find("ForexBuying").text) - kuveytdinarialis6
kuveytdinarisatisfarki3 = float(kuveytdinari5.find("ForexSelling").text) - kuveytdinarisatis6

norveçkronualisfarki3 = float(norveçkronu5.find("ForexBuying").text) - norveçkronualis6
norveçkronusatisfarki3 = float(norveçkronu5.find("ForexSelling").text) - norveçkronusatis6

suudiriyalialisfarki3 = float(suudiriyali5.find("ForexBuying").text) - suudiriyalialis6
suudiriyalisatisfarki3 = float(suudiriyali5.find("ForexSelling").text) - suudiriyalisatis6

japonyenialisfarki3 = (float(japonyeni5.find("ForexBuying").text) / (100) ) - japonyenialis6 ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.
japonyenisatisfarki3 = (float(japonyeni5.find("ForexSelling").text) / (100) ) - japonyenisatis6 ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.

rusrublesialisfarki3 = float(rusrublesi5.find("ForexBuying").text) - rusrublesialis6
rusrublesisatisfarki3 = float(rusrublesi5.find("ForexSelling").text) - rusrublesisatis6

yuanalisfarki3 = float(yuan5.find("ForexBuying").text) - yuanalis6
yuansatisfarki3 = float(yuan5.find("ForexSelling").text) - yuansatis6


data9 = {
    'USD': [abddolarialisfarki3,abddolarisatisfarki3],
    'EUR': [euroalisfarki3,eurosatisfarki3],
    'GBP': [sterlinalisfarki3,sterlinsatisfarki3],
    'AUD': [avustralyadolarialisfarki3,avustralyadolarisatisfarki3],
    'CNY': [yuanalisfarki3,yuansatisfarki3],
    'DKK': [danimarkakronualisfarki3,danimarkakronusatisfarki3],
    'SEK': [isveçkronualisfarki3,isveçkronusatisfarki3],
    'CHF': [isvicrefrangialisfarki3,isvicrefrangisatisfarki3],
    'JPY': [japonyenialisfarki3,japonyenisatisfarki3],
    'CAD': [kanadadolarıalisfarki3,kanadadolarısatisfarki3],
    'KWD': [kuveytdinarialisfarki3,kuveytdinarisatisfarki3],
    'NOK': [norveçkronualisfarki3,norveçkronusatisfarki3],
    'RUB': [rusrublesialisfarki3,rusrublesisatisfarki3],
    'SAR': [suudiriyalialisfarki3,suudiriyalisatisfarki3]
}

df9 = pd.DataFrame(data9, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["Bankalar arası döviz alış farkı-14Mart","Bankalar arası döviz satış farkı-14Mart"])

result6 = pd.concat([result5, df9], axis=0)

######print(result6)
######result6.to_excel('14Mart2024.xlsx', index=True)

result7 = pd.concat([result4,result2,result6],axis=0)
#print(result7)


########################################       15 MART 2024  MERKEZ BANKASI            #######################################

xml15 = et.ElementTree(file=urlopen("https://www.tcmb.gov.tr/kurlar/202403/15032024.xml")) # 15 MART 2024 MERKEZ BANKASI
root = xml15.getroot()

abddolari7 = root.findall("Currency")[0]
avustralyadolari7 = root.findall("Currency")[1]
danimarkakronu7 = root.findall("Currency")[2]
euro7 = root.findall("Currency")[3]
sterlin7 = root.findall("Currency")[4]
isvicrefrangı7 = root.findall("Currency")[5]
isveckronu7 = root.findall("Currency")[6]
kanadadolari7 = root.findall("Currency")[7]
kuveytdinari7 = root.findall("Currency")[8]
norveçkronu7 = root.findall("Currency")[9]
suudiriyali7 = root.findall("Currency")[10]
japonyeni7 = root.findall("Currency")[11]
rusrublesi7 = root.findall("Currency")[14] # bazı para birimleri iş bankasında olmadığı için indeksler atlandı.
yuan7 = root.findall("Currency")[16]

dolaralis7 = float(abddolari7.find("ForexBuying").text) # ABD DOLARI ALIŞ
dolarsatis7 = float(abddolari7.find("ForexSelling").text) # ABD DOLARI SATIŞ

avustralyadolaralis7 = float(avustralyadolari7.find("ForexBuying").text) # AVUSTRALYA DOLARI ALIŞ
avustralyadolarsatis7 = float(avustralyadolari7.find("ForexSelling").text) # AVUSTRALYA DOLARI SATIŞ

danimarkakronualis7 = float(danimarkakronu7.find("ForexBuying").text) # DANİMARKA KRONU ALIŞ
danimarkakronusatis7 = float(danimarkakronu7.find("ForexSelling").text) # DANİMARKA KRONU SATIŞ

euroalis7 = float(euro7.find("ForexBuying").text) # EURO ALIŞ
eurosatis7 = float(euro7.find("ForexSelling").text) # EURO SATIŞ

sterlinalis7 = float(sterlin7.find("ForexBuying").text) # İNGİLİZ STERLİNİ ALIŞ
sterlinsatis7 = float(sterlin7.find("ForexSelling").text) # İNGİLİZ STERLİNİ SATIŞ

isvicrefrangialis7 = float(isvicrefrangı7.find("ForexBuying").text) # İSVİÇRE FRANGI ALIŞ
isvicrefrangisatis7= float(isvicrefrangı7.find("ForexSelling").text) # İSVİÇRE FRANGI SATIŞ

isveckronualis7 = float(isveckronu7.find("ForexBuying").text) # İSVEÇ KRONU ALIŞ
isveckronusatis7 = float(isveckronu7.find("ForexSelling").text) # İSVEÇ KRONU SATIŞ

kanadadolarialis7 = float(kanadadolari7.find("ForexBuying").text) # KANADA DOLARI ALIŞ
kanadadolarisatis7 = float(kanadadolari7.find("ForexSelling").text) # KANADA DOLARI SATIŞ

kuveytdinarialis7 = float(kuveytdinari7.find("ForexBuying").text) # KUVEYT DİNARİ ALIŞ
kuveytdinarisatis7 = float(kuveytdinari7.find("ForexSelling").text) # KUVEYT DİNARİ SATIŞ

norveçkronualis7 = float(norveçkronu7.find("ForexBuying").text) # NORVEÇ KRONU ALIŞ
norveçkronusatis7 = float(norveçkronu7.find("ForexSelling").text) # NORVEÇ KRONU SATIŞ

suudiriyalialis7 = float(suudiriyali7.find("ForexBuying").text) # SUUDİ RİYALİ ALIŞ
suudiriyalisatis7 = float(suudiriyali7.find("ForexSelling").text) # SUUDİ RİYALİ SATIŞ

japonyenialis7 = float(japonyeni7.find("ForexBuying").text) / (100)  # JAPON YENİ ALIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.
japonyenisatis7 = float(japonyeni7.find("ForexSelling").text) / (100)  # JAPON YENİ SATIŞ 100'E BÖLÜNDÜ ÇÜNKÜ MERKEZ BANKASINDA 100 BİRİM ÜZERİNDEN HESAPLANIRKEN İŞ BANKASI'NDA 1 BİRİM ÜZERİNDEN HESAPLANIYOR.

rusrublesialis7 = float(rusrublesi7.find("ForexBuying").text) # RUS RUBLESİ ALIŞ
rusrublesisatis7 = float(rusrublesi7.find("ForexSelling").text) # RUS RUBLESİ SATIŞ

yuanalis7 = float(yuan7.find("ForexBuying").text) # ÇİN YUANI ALIŞ
yuansatis7 = float(yuan7.find("ForexSelling").text) # ÇİN YUANI SATIŞ

## MERKEZ BANKASI 15 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##

abddolarispread7 = dolarsatis7 - dolaralis7

eurospread7 = eurosatis7 - euroalis7

avustralyadolarispread7 = avustralyadolarsatis7 - avustralyadolaralis7

danimarkakronuspread7 = danimarkakronusatis7 - danimarkakronualis7

sterlinspread7 = sterlinsatis7 - sterlinalis7

isvicrefrangıspread7 = isvicrefrangisatis7 - isvicrefrangialis7

isveckronuspread7 = isveckronusatis7 - isveckronualis7

kanadadolarispread7 = kanadadolarisatis7 - kanadadolarialis7

kuveytdinarispread7 = kuveytdinarisatis7 - kuveytdinarialis7

norveçkronuspread7 = norveçkronusatis7 - norveçkronualis7

suudiriyalispread7 = suudiriyalisatis7 - suudiriyalialis7

japonyenispread7 = japonyenisatis7 - japonyenialis7

rusrublesispread7 = rusrublesisatis7 - rusrublesialis7

yuanspread7 = yuansatis7 - yuanalis7

data10 = {
    'USD': [dolaralis7,dolarsatis7, abddolarispread7],
    'EUR': [euroalis7,eurosatis7,eurospread7],
    'GBP': [sterlinalis7,sterlinsatis7,sterlinspread7],
    'AUD': [avustralyadolaralis7,avustralyadolarsatis7,avustralyadolarispread7],
    'CNY': [yuanalis7,yuansatis7,yuanspread7],
    'DKK': [danimarkakronualis7,danimarkakronusatis7,danimarkakronuspread7],
    'SEK': [isveckronualis7,isveckronusatis7,isveckronuspread7],
    'CHF': [isvicrefrangialis7,isvicrefrangisatis7,isvicrefrangıspread7],
    'JPY': [japonyenialis7,japonyenisatis7,japonyenispread7],
    'CAD': [kanadadolarialis7,kanadadolarisatis7,kanadadolarispread7],
    'KWD': [kuveytdinarialis7,kuveytdinarisatis7,kuveytdinarispread7],
    'NOK': [norveçkronualis7,norveçkronusatis7,norveçkronuspread7],
    'RUB': [rusrublesialis7,rusrublesisatis7,rusrublesispread7],
    'SAR': [suudiriyalialis7,suudiriyalisatis7,suudiriyalispread7]
}

df10 = pd.DataFrame(data10, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["TCMB Döviz Alış-15Mart","TCMB Döviz Satış-15Mart","TCMB Satış Alış Fark(Spread)-15Mart"])
#print(df10)

########### İŞ BANKASI 15 MART 2024 #######################


url4 = "https://www.isbank.com.tr/doviz-kurlari"
browser.get(url4)

tarih4 = '15/03/2024'
script4 = f"document.getElementById('dK_dateInput').value = '{tarih4}';" # TARİH SEÇTİREBİLMEK İÇİN.
browser.execute_script(script4)
tür4 = 'IS'
döviztürü4 = f"document.getElementById('fxRateType').value = '{tür4}';" # DÖVİZ TÜRÜNÜ SEÇTİREBİLMEK İÇİN - İŞ BANKASI GİŞELERİNE GÖRE UYARLANDI.
browser.execute_script(döviztürü4)

browser.execute_script("CallHandler();") ## TIKLATTIRABİLMEK İÇİN

time.sleep(5)


abddolarialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[2]').text)
abddolarisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[2]/td[3]').text)

euroalis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[2]').text)
eurosatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[3]/td[3]').text)

sterlinalis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[2]').text)
sterlinsatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[4]/td[3]').text)

avustralyadolarialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[2]').text)
avustralyadolarisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[5]/td[3]').text)

yuanalis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[2]').text)
yuansatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[6]/td[3]').text)

danimarkakronualis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[2]').text)
danimarkakronusatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[7]/td[3]').text)

isveckronualis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[2]').text)
isveçkronusatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[8]/td[3]').text)

isviçrefrangıalis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[2]').text)
isviçrefrangısatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[9]/td[3]').text)

japonyenialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[2]').text)
japonyenisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[10]/td[3]').text)

kanadadolarıalis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[2]').text)
kanadadolarisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[11]/td[3]').text)

kuveytdinarialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[2]').text)
kuveytdinarisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[12]/td[3]').text)

norveçkronualis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[2]').text)
norveçkronusatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[13]/td[3]').text)

rusrublesialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[2]').text)
rusrublesisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[14]/td[3]').text)

suudiriyalialis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[2]').text)
suudiriyalisatis8 = float(browser.find_element(By.XPATH,'//*[@id="ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73"]/div/div[2]/table/tr[15]/td[3]').text)




## İŞ BANKASI 15 MART 2024 ALIM SATIM SPREAD(SATIŞ ALIŞ FARKI) ##



abddolarispread8 = abddolarisatis8 - abddolarialis8

eurospread8 = eurosatis8 - euroalis8

sterlinspread8 = sterlinsatis8 - sterlinalis8

avustralyadolarispread8 = avustralyadolarisatis8 - avustralyadolarialis8

yuanspread8 = yuansatis8 - yuanalis8

danimarkakronuspread8 = danimarkakronusatis8 - danimarkakronualis8

isveckronuspread8 = isveçkronusatis8 - isveckronualis8

isvicrefrangıspread8 = isviçrefrangısatis8 - isviçrefrangıalis8

japonyenispread8 = japonyenisatis8 - japonyenialis8

kanadadolarispread8 = kanadadolarisatis8 - kanadadolarıalis8

kuveytdinarispread8 = kuveytdinarisatis8 - kuveytdinarialis8

norveçkronuspread8 = norveçkronusatis8 - norveçkronualis8

rusrublesispread8 = rusrublesisatis8 - rusrublesialis8

suudiriyalispread8 = suudiriyalisatis8 - suudiriyalialis8


data11 = {
    'USD': [abddolarialis8,abddolarisatis8, abddolarispread8],
    'EUR': [euroalis8,eurosatis8,eurospread8],
    'GBP': [sterlinalis8,sterlinsatis8,sterlinspread8],
    'AUD': [avustralyadolarialis8,avustralyadolarisatis8,avustralyadolarispread8],
    'CNY': [yuanalis8,yuansatis8,yuanspread8],
    'DKK': [danimarkakronualis8,danimarkakronusatis8,danimarkakronuspread8],
    'SEK': [isveckronualis8,isveçkronusatis8,isveckronuspread8],
    'CHF': [isviçrefrangıalis8,isviçrefrangısatis8,isvicrefrangıspread8],
    'JPY': [japonyenialis8,japonyenisatis8,japonyenispread8],
    'CAD': [kanadadolarıalis8,kanadadolarisatis8,kanadadolarispread8],
    'KWD': [kuveytdinarialis8,kuveytdinarisatis8,kuveytdinarispread8],
    'NOK': [norveçkronualis8,norveçkronusatis8,norveçkronuspread8],
    'RUB': [rusrublesialis8,rusrublesisatis8,rusrublesispread8],
    'SAR': [suudiriyalialis8,suudiriyalisatis8,suudiriyalispread8]
}

df11 = pd.DataFrame(data11, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["İş Bankası Döviz Alış-15Mart","İş Bankası Döviz Satış-15Mart","İş Bankası Satış Alış Fark(Spread)-15Mart"])
result8 = pd.concat([df10, df11], axis=0)
#print(result8)

#### FARKLILIK HESAPLAMA >>> MERKEZ BANKASI'NIN İŞ BANKASI'NDAN FARKI HESAPLANMIŞTIR(15 MART 2024) #####


abddolarialisfarki4 = float(abddolari7.find("ForexBuying").text) - abddolarialis8
abddolarisatisfarki4 = float(abddolari7.find("ForexSelling").text) - abddolarisatis8

avustralyadolarialisfarki4 = float(avustralyadolari7.find("ForexBuying").text) - avustralyadolarialis8
avustralyadolarisatisfarki4 = float(avustralyadolari7.find("ForexSelling").text) - avustralyadolarisatis8

danimarkakronualisfarki4 = float(danimarkakronu7.find("ForexBuying").text) - danimarkakronualis8
danimarkakronusatisfarki4 = float(danimarkakronu7.find("ForexSelling").text) - danimarkakronusatis8

euroalisfarki4 = float(euro7.find("ForexBuying").text) - euroalis8
eurosatisfarki4 = float(euro7.find("ForexSelling").text) - eurosatis8

sterlinalisfarki4 = float(sterlin7.find("ForexBuying").text) - sterlinalis8
sterlinsatisfarki4 = float(sterlin7.find("ForexSelling").text) - sterlinsatis8

isvicrefrangialisfarki4 = float(isvicrefrangı7.find("ForexBuying").text) - isviçrefrangıalis8
isvicrefrangisatisfarki4 = float(isvicrefrangı7.find("ForexSelling").text) - isviçrefrangısatis8

isveçkronualisfarki4 = float(isveckronu7.find("ForexBuying").text) - isveckronualis8
isveçkronusatisfarki4 = float(isveckronu7.find("ForexSelling").text) - isveçkronusatis8

kanadadolarıalisfarki4 = float(kanadadolari7.find("ForexBuying").text) - kanadadolarıalis8
kanadadolarısatisfarki4 = float(kanadadolari7.find("ForexSelling").text) - kanadadolarıalis8

kuveytdinarialisfarki4 = float(kuveytdinari7.find("ForexBuying").text) - kuveytdinarialis8
kuveytdinarisatisfarki4 = float(kuveytdinari7.find("ForexSelling").text) - kuveytdinarisatis8

norveçkronualisfarki4 = float(norveçkronu7.find("ForexBuying").text) - norveçkronualis8
norveçkronusatisfarki4 = float(norveçkronu7.find("ForexSelling").text) - norveçkronusatis8

suudiriyalialisfarki4 = float(suudiriyali7.find("ForexBuying").text) - suudiriyalialis8
suudiriyalisatisfarki4 = float(suudiriyali7.find("ForexSelling").text) - suudiriyalisatis8

japonyenialisfarki4 = (float(japonyeni7.find("ForexBuying").text) / (100) ) - japonyenialis8 ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.
japonyenisatisfarki4 = (float(japonyeni7.find("ForexSelling").text) / (100) ) - japonyenisatis8 ## KARIŞIKLIK OLMAMASI İÇİN ÇÜNKÜ JAPON YENİ 100 BİRİM ÜZERİNDEN HESAPLANMIŞ MERKEZ BANKASINDA.

rusrublesialisfarki4 = float(rusrublesi7.find("ForexBuying").text) - rusrublesialis8
rusrublesisatisfarki4 = float(rusrublesi7.find("ForexSelling").text) - rusrublesisatis8

yuanalisfarki4 = float(yuan7.find("ForexBuying").text) - yuanalis8
yuansatisfarki4 = float(yuan7.find("ForexSelling").text) - yuansatis8


data12 = {
    'USD': [abddolarialisfarki4,abddolarisatisfarki4],
    'EUR': [euroalisfarki4,eurosatisfarki4],
    'GBP': [sterlinalisfarki4,sterlinsatisfarki4],
    'AUD': [avustralyadolarialisfarki4,avustralyadolarisatisfarki4],
    'CNY': [yuanalisfarki4,yuansatisfarki4],
    'DKK': [danimarkakronualisfarki4,danimarkakronusatisfarki4],
    'SEK': [isveçkronualisfarki4,isveçkronusatisfarki4],
    'CHF': [isvicrefrangialisfarki4,isvicrefrangisatisfarki4],
    'JPY': [japonyenialisfarki4,japonyenisatisfarki4],
    'CAD': [kanadadolarıalisfarki4,kanadadolarısatisfarki4],
    'KWD': [kuveytdinarialisfarki4,kuveytdinarisatisfarki4],
    'NOK': [norveçkronualisfarki4,norveçkronusatisfarki4],
    'RUB': [rusrublesialisfarki4,rusrublesisatisfarki4],
    'SAR': [suudiriyalialisfarki4,suudiriyalisatisfarki4]
}

df12 = pd.DataFrame(data12, columns= ["USD","EUR","GBP","AUD","CNY","DKK","SEK","CHF","JPY","CAD","KWD","NOK","RUB","SAR"], index= ["Bankalar arası döviz alış farkı-15Mart","Bankalar arası döviz satış farkı-15Mart"])

result9 = pd.concat([result8, df12], axis=0)

result10 = pd.concat([result4,result2,result6,result9],axis=0)
#print(result10)
result10.to_excel('data1.xlsx', index=True)
print("data1.xlsx oluşturuldu!\nLütfen kontrol edin...")


###### VERİ GÖRSELLEŞTİRME KISMI 12 MART #############


parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]
dövizalıştcmb1 = [round(float(japonyenialis3),4), round(float(rusrublesialis3),4), float(norveçkronualis3), float(isveckronualis3), ## japon yeni ve rus rubleleri yuvarlandı çünkü virgülden sonraki kısım çok uzun idi.
                  float(yuanalis3), float(danimarkakronualis3), float(suudiriyalialis3), float(avustralyadolaralis3),
                  float(kanadadolarialis3), float(dolaralis3), float(euroalis3), float(isvicrefrangialis3),
                  float(sterlinalis3), float(kuveytdinarialis3)]
dövizalışib1 = [round(float(japonyenialis4),4), round(float(rusrublesialis4),4), float(norveçkronualis4), float(isveckronualis4), ## japon yeni ve rus rubleleri yuvarlandı çünkü virgülden sonraki kısım çok uzun idi.
                float(yuanalis4), float(danimarkakronualis4), float(suudiriyalialis4), float(avustralyadolarialis4),
                float(kanadadolarıalis4), float(abddolarialis4), float(euroalis4), float(isviçrefrangıalis4),
                float(sterlinalis4), float(kuveytdinarialis4)]

y = np.arange(len(parabirimleri))
x1 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizalıştcmb1, height=bar_width, color='orange', align='center', label='Döviz Alış TCMB')
plt.barh(y, dövizalışib1, height=bar_width, color='blue', align='center', label='Döviz Alış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x1)

plt.title('12 Mart Bankalar Arası Döviz Kuru Alış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizalıştcmb1[i], y[i] - bar_width, str(dövizalıştcmb1[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizalışib1[i], y[i], str(dövizalışib1[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

parabirimleri2 = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]
dövizsatıştcmb1 = [round(float(japonyenisatis3),4), round(float(rusrublesisatis3),4), float(norveçkronusatis3), float(isveckronusatis3), ## japon yeni ve rus rublesi yuvarlandı
                  float(yuansatis3), float(danimarkakronusatis3), float(suudiriyalisatis3), float(avustralyadolarsatis3),
                  float(kanadadolarisatis3), float(dolarsatis3), float(eurosatis3), float(isvicrefrangisatis3),
                  float(sterlinsatis3), float(kuveytdinarisatis3)]
dövizsatışib1 = [round(float(japonyenisatis4),4), round(float(rusrublesisatis4),4), float(norveçkronusatis4), float(isveçkronusatis4), ## japon yeni ve rus rublesi yuvarlandı
                float(yuansatis4), float(danimarkakronusatis4), float(suudiriyalisatis4), float(avustralyadolarisatis4),
                float(kanadadolarisatis4), float(abddolarisatis4), float(eurosatis4), float(isviçrefrangısatis4),
                float(sterlinsatis4), float(kuveytdinarisatis4)]

y2 = np.arange(len(parabirimleri2))
x2 = np.arange(0,121,24)
bar_width2 = 0.25

plt.barh(y2 - bar_width2, dövizsatıştcmb1, height=bar_width2, color='orange', align='center', label='Döviz Satış TCMB')
plt.barh(y2, dövizsatışib1, height=bar_width2, color='blue', align='center', label='Döviz Satış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')
plt.title('12 Mart Bankalar Arası Döviz Satış Analiz')

plt.yticks(y, parabirimleri2)
plt.xticks(x2)

plt.legend(loc="lower right")

for i in range(len(parabirimleri2)):
    plt.text(dövizsatıştcmb1[i], y2[i] - bar_width2, str(dövizsatıştcmb1[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizsatışib1[i], y2[i], str(dövizsatışib1[i]), ha='left', va='center', fontsize=6)


plt.tight_layout()
plt.show()


###### VERİ GÖRSELLEŞTİRME KISMI 13 MART #############

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizalıştcmb2 = [round(float(japonyenialis2),4), round(float(rusrublesialis2),4), float(norveçkronualis2), float(isveckronualis2), ## japon yeni ve rus rublesi yuvarlandı.
                  float(yuanalis2), float(danimarkakronualis2), float(suudiriyalialis2), float(avustralyadolaralis2),
                  float(kanadadolarialis2), float(dolaralis2), float(euroalis2), float(isvicrefrangialis2),
                  float(sterlinalis2), float(kuveytdinarialis2)]
dövizalışib2 = [round(float(japonyenialis),4), round(float(rusrublesialis),4), float(norveçkronualis), float(isveckronualis), ## japon yeni ve rus rublesi yuvarlandı.
                float(yuanalis), float(danimarkakronualis), float(suudiriyalialis), float(avustralyadolarialis),
                float(kanadadolarıalis), float(abddolarialis), float(euroalis), float(isviçrefrangıalis),
                float(sterlinalis), float(kuveytdinarialis)]


y = np.arange(len(parabirimleri))
x3 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizalıştcmb2, height=bar_width, color='#ff7f0e', align='center', label='Döviz Alış TCMB')
plt.barh(y, dövizalışib2, height=bar_width, color='#9467bd', align='center', label='Döviz Alış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x3)

plt.title('13 Mart Bankalar Arası Döviz Kuru Alış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizalıştcmb2[i], y[i] - bar_width, str(dövizalıştcmb2[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizalışib2[i], y[i], str(dövizalışib2[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizsatıştcmb2 = [round(float(japonyenisatis2),4), round(float(rusrublesisatis2),4), float(norveçkronusatis2), float(isveckronusatis2), ## japon yeni ve rus rublesi yuvarlanıyor
                  float(yuansatis2), float(danimarkakronusatis2), float(suudiriyalisatis2), float(avustralyadolarsatis2),
                  float(kanadadolarisatis2), float(dolarsatis2), float(eurosatis2), float(isvicrefrangisatis2),
                  float(sterlinsatis2), float(kuveytdinarisatis2)]
dövizsatışib2 = [round(float(japonyenisatis),4), round(float(rusrublesisatis),4), float(norveçkronusatis), float(isveçkronusatis), ## japon yeni ve rus rublesi yuvarlanıyor
                float(yuansatis), float(danimarkakronusatis), float(suudiriyalisatis), float(avustralyadolarisatis),
                float(kanadadolarisatis), float(abddolarisatis), float(eurosatis), float(isviçrefrangısatis),
                float(sterlinsatis), float(kuveytdinarisatis)]


y = np.arange(len(parabirimleri))
x4 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizsatıştcmb2, height=bar_width, color='#ff7f0e', align='center', label='Döviz Satış TCMB')
plt.barh(y, dövizsatışib2, height=bar_width, color='#9467bd', align='center', label='Döviz Satış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x4)

plt.title('13 Mart Bankalar Arası Döviz Kuru Satış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizsatıştcmb2[i], y[i] - bar_width, str(dövizsatıştcmb2[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizsatışib2[i], y[i], str(dövizsatışib2[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

###### VERİ GÖRSELLEŞTİRME KISMI 14 MART #############

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizalıştcmb3 = [round(float(japonyenialis5),4), round(float(rusrublesialis5),4), float(norveçkronualis5), float(isveckronualis5), ## japon yeni ve rus rublesi virgülden sonraki kısım çok uzun
                  float(yuanalis5), float(danimarkakronualis5), float(suudiriyalialis5), float(avustralyadolaralis5),
                  float(kanadadolarialis5), float(dolaralis5), float(euroalis5), float(isvicrefrangialis5),
                  float(sterlinalis5), float(kuveytdinarialis5)]
dövizalışib3 = [round(float(japonyenialis6),4), round(float(rusrublesialis6),4), float(norveçkronualis6), float(isveckronualis6), ## japon yeni ve rus rublesi virgülden sonraki kısım çok uzun
                float(yuanalis6), float(danimarkakronualis6), float(suudiriyalialis6), float(avustralyadolarialis6),
                float(kanadadolarıalis6), float(abddolarialis6), float(euroalis6), float(isviçrefrangıalis6),
                float(sterlinalis6), float(kuveytdinarialis6)]


y = np.arange(len(parabirimleri))
x5 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizalıştcmb3, height=bar_width, color='red', align='center', label='Döviz Alış TCMB')
plt.barh(y, dövizalışib3, height=bar_width, color='black', align='center', label='Döviz Alış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x5)

plt.title('14 Mart Bankalar Arası Döviz Kuru Alış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizalıştcmb3[i], y[i] - bar_width, str(dövizalıştcmb3[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizalışib3[i], y[i], str(dövizalışib3[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizsatıştcmb3 = [round(float(japonyenisatis5),4), round(float(rusrublesisatis5),4), float(norveçkronusatis5), float(isveckronusatis5), ## japon yeni ve rus rubleleri virgül kısmı yuvarlandı
                  float(yuansatis5), float(danimarkakronusatis5), float(suudiriyalisatis5), float(avustralyadolarsatis5),
                  float(kanadadolarisatis5), float(dolarsatis5), float(eurosatis5), float(isvicrefrangisatis5),
                  float(sterlinsatis5), float(kuveytdinarisatis5)]
dövizsatışib3 = [round(float(japonyenisatis6),4), round(float(rusrublesisatis6),4), float(norveçkronusatis6), float(isveçkronusatis6), ## japon yeni ve rus rubleleri virgül kısmı yuvarlandı
                float(yuansatis6), float(danimarkakronusatis6), float(suudiriyalisatis6), float(avustralyadolarisatis6),
                float(kanadadolarisatis6), float(abddolarisatis6), float(eurosatis6), float(isviçrefrangısatis6),
                float(sterlinsatis6), float(kuveytdinarisatis6)]


y = np.arange(len(parabirimleri))
x6 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizsatıştcmb3, height=bar_width, color='red', align='center', label='Döviz Satış TCMB')
plt.barh(y, dövizsatışib3, height=bar_width, color='black', align='center', label='Döviz Satış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x6)

plt.title('14 Mart Bankalar Arası Döviz Kuru Satış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizsatıştcmb3[i], y[i] - bar_width, str(dövizsatıştcmb3[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizsatışib3[i], y[i], str(dövizsatışib3[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

###### VERİ GÖRSELLEŞTİRME KISMI 15 MART #############

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizalıştcmb4 = [round(float(japonyenialis7),4), round(float(rusrublesialis7),4), float(norveçkronualis7), float(isveckronualis7), ## japon ve rus rubleleri tekrardan yuvarlandı
                  float(yuanalis7), float(danimarkakronualis7), float(suudiriyalialis7), float(avustralyadolaralis7),
                  float(kanadadolarialis7), float(dolaralis7), float(euroalis7), float(isvicrefrangialis7),
                  float(sterlinalis7), float(kuveytdinarialis7)]
dövizalışib4 = [round(float(japonyenialis8),4), round(float(rusrublesialis8),4), float(norveçkronualis8), float(isveckronualis8), ## japon ve rus rubleleri tekrardan yuvarlandı
                float(yuanalis8), float(danimarkakronualis8), float(suudiriyalialis8), float(avustralyadolarialis8),
                float(kanadadolarıalis8), float(abddolarialis8), float(euroalis8), float(isviçrefrangıalis8),
                float(sterlinalis8), float(kuveytdinarialis8)]


y = np.arange(len(parabirimleri))
x7 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizalıştcmb4, height=bar_width, color='#e67e22', align='center', label='Döviz Alış TCMB')
plt.barh(y, dövizalışib4, height=bar_width, color='#2ecc71', align='center', label='Döviz Alış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x7)

plt.title('15 Mart Bankalar Arası Döviz Kuru Alış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizalıştcmb4[i], y[i] - bar_width, str(dövizalıştcmb4[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizalışib4[i], y[i], str(dövizalışib4[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizsatıştcmb4 = [round(float(japonyenisatis7),4), round(float(rusrublesisatis7),4), float(norveçkronusatis7), float(isveckronusatis7), ## japon yeni ve rus rublesi yuvarlanıyor
                  float(yuansatis7), float(danimarkakronusatis7), float(suudiriyalisatis7), float(avustralyadolarsatis7),
                  float(kanadadolarisatis7), float(dolarsatis7), float(eurosatis7), float(isvicrefrangisatis7),
                  float(sterlinsatis7), float(kuveytdinarisatis7)]
dövizsatışib4 = [round(float(japonyenisatis8),4), round(float(rusrublesisatis8),4), float(norveçkronusatis8), float(isveçkronusatis8), ## japon yeni ve rus rublesi yuvarlanıyor
                float(yuansatis8), float(danimarkakronusatis8), float(suudiriyalisatis8), float(avustralyadolarisatis8),
                float(kanadadolarisatis8), float(abddolarisatis8), float(eurosatis8), float(isviçrefrangısatis8),
                float(sterlinsatis8), float(kuveytdinarisatis8)]


y = np.arange(len(parabirimleri))
x8 = np.arange(0,121,24)
bar_width = 0.25

plt.barh(y - bar_width, dövizsatıştcmb4, height=bar_width, color= "#e67e22", align='center', label='Döviz Satış TCMB')
plt.barh(y, dövizsatışib4, height=bar_width, color='#2ecc71', align='center', label='Döviz Satış İB')

plt.xlabel('Fiyat')
plt.ylabel('Para Birimleri')

plt.yticks(y, parabirimleri)
plt.xticks(x8)

plt.title('15 Mart Bankalar Arası Döviz Kuru Satış Analiz')

plt.legend(loc="lower right")

for i in range(len(parabirimleri)):
    plt.text(dövizsatıştcmb4[i], y[i] - bar_width, str(dövizsatıştcmb4[i]), ha='left', va='center', fontsize=6)
    plt.text(dövizsatışib4[i], y[i], str(dövizsatışib4[i]), ha='left', va='center', fontsize=6)

plt.tight_layout()
plt.show()

############ İŞ BANKASI ORTALAMA DÖVİZ ALIŞ-SATIŞ ###########

ibusdmean = (float(abddolarialis) + float(abddolarialis4) + float(abddolarialis6) + float(abddolarialis8)) / 4
ibeurmean = (float(euroalis) + float(euroalis4) + float(euroalis6) + float(euroalis8)) / 4
ibgbpmean = (float(sterlinalis) + float(sterlinsatis4) + float(sterlinalis6) + float(sterlinalis8)) / 4
ibaudmean = (float(avustralyadolarialis) + float(avustralyadolarialis4) + float(avustralyadolarialis6) + float(avustralyadolarialis8)) / 4
ibcnymean = (float(yuanalis) + float(yuanalis4) + float(yuanalis6) + float(yuanalis8)) / 4
ibdkkmean = (float(danimarkakronualis) + float(danimarkakronualis4) + float(danimarkakronualis6) + float(danimarkakronualis8)) / 4
ibsekmean = (float(isveckronualis) + float(isveckronualis4) + float(isveckronualis6) + float(isveckronualis8)) / 4
ibchfmean = (float(isviçrefrangıalis) + float(isviçrefrangıalis4) + float(isviçrefrangıalis6) + float(isviçrefrangıalis8)) / 4
ibjpymean = (float(japonyenialis) + float(japonyenialis4) + float(japonyenialis6) + float(japonyenialis8)) / 4
ibcadmean = (float(kanadadolarıalis) + float(kanadadolarıalis4) + float(kanadadolarıalis6) + float(kanadadolarıalis8)) / 4
ibkwdmean = (float(kuveytdinarialis) + float(kuveytdinarialis4) + float(kuveytdinarialis6) + float(kuveytdinarialis8)) / 4
ibnokmean = (float(norveçkronualis) + float(norveçkronualis4) + float(norveçkronualis6) + float(norveçkronualis8)) / 4
ibrubmean = (float(rusrublesialis) + float(rusrublesialis4) + float(rusrublesialis6) + float(rusrublesialis8)) / 4
ibsarmean = (float(suudiriyalialis) + float(suudiriyalialis4) + float(suudiriyalialis6) + float(suudiriyalialis8)) / 4

ibusdmean2 = (float(abddolarisatis) + float(abddolarisatis4) + float(abddolarisatis6) + float(abddolarisatis8)) / 4
ibeurmean2 = (float(eurosatis) + float(eurosatis4) + float(eurosatis6) + float(eurosatis8)) / 4
ibgbpmean2 = (float(sterlinsatis) + float(sterlinsatis4) + float(sterlinsatis6) + float(sterlinsatis8)) / 4
ibaudmean2 = (float(avustralyadolarisatis) + float(avustralyadolarisatis4) + float(avustralyadolarisatis6) + float(avustralyadolarisatis8)) / 4
ibcnymean2 = (float(yuansatis) + float(yuansatis4) + float(yuansatis6) + float(yuansatis8)) / 4
ibdkkmean2 = (float(danimarkakronusatis) + float(danimarkakronusatis4) + float(danimarkakronusatis6) + float(danimarkakronusatis8)) / 4
ibsekmean2 = (float(isveçkronusatis) + float(isveçkronusatis4) + float(isveçkronusatis6) + float(isveçkronusatis8)) / 4
ibchfmean2 = (float(isviçrefrangısatis) + float(isviçrefrangısatis4) + float(isviçrefrangısatis6) + float(isviçrefrangısatis8)) / 4
ibjpymean2 = (float(japonyenisatis) + float(japonyenisatis4) + float(japonyenisatis6) + float(japonyenisatis8)) / 4
ibcadmean2 = (float(kanadadolarisatis) + float(kanadadolarisatis4) + float(kanadadolarisatis6) + float(kanadadolarisatis8)) / 4
ibkwdmean2 = (float(kuveytdinarisatis) + float(kuveytdinarisatis4) + float(kuveytdinarisatis6) + float(kuveytdinarisatis8)) / 4
ibnokmean2 = (float(norveçkronusatis) + float(norveçkronusatis4) + float(norveçkronusatis6) + float(norveçkronusatis8)) / 4
ibrubmean2 = (float(rusrublesisatis) + float(rusrublesisatis4) + float(rusrublesisatis6) + float(rusrublesisatis8)) / 4
ibsarmean2 = (float(suudiriyalisatis) + float(suudiriyalisatis4) + float(suudiriyalisatis6) + float(suudiriyalisatis8)) / 4

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizalışmeanib = [round(float(ibjpymean),4), round(float(ibrubmean),4), round(float(ibnokmean),4), round(float(ibsekmean),4),
                  round(float(ibcnymean),4), round(float(ibdkkmean),4), round(float(ibsarmean),4), round(float(ibaudmean),4),
                  round(float(ibcadmean),4), round(float(ibusdmean),4), round(float(ibeurmean),4), round(float(ibchfmean),4),
                  round(float(ibgbpmean),4), round(float(ibkwdmean),4)]
dövizsatışmeanib = [round(float(ibjpymean2),4), round(float(ibrubmean2),4),round(float(ibnokmean2),4), round(float(ibsekmean2),4),
                round(float(ibcnymean2),4), round(float(ibdkkmean2),4), round(float(ibsarmean2),4), round(float(ibaudmean2),4),
                round(float(ibcadmean2),4), round(float(ibusdmean2),4), round(float(ibeurmean2),4), round(float(ibchfmean2),4),
                round(float(ibgbpmean2),4), round(float(ibkwdmean2),4)]


x = np.arange(len(parabirimleri))
bar_width = 0.25

text_fontsize = 6

plt.bar(x, dövizalışmeanib, width=bar_width, color='orange', align='center', label='Döviz Alış Ortalama İB')
plt.bar(x + 0.4, dövizsatışmeanib, width=bar_width, color='blue', align='center', label='Döviz Satış Ortalama İB')


plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x, parabirimleri)

plt.title('İş Bankası Ortalama Döviz Alış-Satış')

plt.legend(loc="upper left")

for i in range(len(parabirimleri)):
    plt.text(x[i], dövizalışmeanib[i], str(dövizalışmeanib[i]), ha='center', va='bottom', fontsize=6)
    plt.text(x[i] + 0.4, dövizsatışmeanib[i] + 0.5, str(dövizsatışmeanib[i]), ha='center', va='bottom', fontsize=6)

plt.tight_layout()
plt.show()

### TCMB ORTALAMA DÖVİZ ALIŞ-SATIŞ ###

tcmbusdmean = (float(dolaralis2) + float(dolaralis3) + float(dolaralis5) + float(dolaralis7)) / 4
tcmbeurmean = (float(euroalis2) + float(euroalis3) + float(euroalis5) + float(euroalis7)) / 4
tcmbgbpmean = (float(sterlinalis2) + float(sterlinsatis3) + float(sterlinalis5) + float(sterlinalis7)) / 4
tcmbaudmean = (float(avustralyadolaralis2) + float(avustralyadolaralis3) + float(avustralyadolaralis5) + float(avustralyadolaralis7)) / 4
tcmbcnymean = (float(yuanalis2) + float(yuanalis3) + float(yuanalis5) + float(yuanalis7)) / 4
tcmbdkkmean = (float(danimarkakronualis2) + float(danimarkakronualis3) + float(danimarkakronualis5) + float(danimarkakronualis7)) / 4
tcmbsekmean = (float(isveckronualis2) + float(isveckronualis3) + float(isveckronualis5) + float(isveckronualis7)) / 4
tcmbchfmean = (float(isvicrefrangialis2) + float(isvicrefrangialis3) + float(isvicrefrangialis5) + float(isvicrefrangialis7)) / 4
tcmbjpymean = (float(japonyenialis2) + float(japonyenialis3) + float(japonyenialis5) + float(japonyenialis7)) / 4
tcmbcadmean = (float(kanadadolarialis2) + float(kanadadolarialis3) + float(kanadadolarialis5) + float(kanadadolarialis7)) / 4
tcmbkwdmean = (float(kuveytdinarialis2) + float(kuveytdinarialis3) + float(kuveytdinarialis5) + float(kuveytdinarialis7)) / 4
tcmbnokmean = (float(norveçkronualis2) + float(norveçkronualis3) + float(norveçkronualis5) + float(norveçkronualis7)) / 4
tcmbrubmean = (float(rusrublesialis2) + float(rusrublesialis3) + float(rusrublesialis5) + float(rusrublesialis7)) / 4
tcmbsarmean = (float(suudiriyalialis2) + float(suudiriyalialis3) + float(suudiriyalialis5) + float(suudiriyalialis7)) / 4

tcmbusdmean2 = (float(dolarsatis2) + float(dolarsatis3) + float(dolarsatis5) + float(dolarsatis7)) / 4
tcmbeurmean2 = (float(eurosatis2) + float(eurosatis3) + float(eurosatis5) + float(eurosatis7)) / 4
tcmbgbpmean2 = (float(sterlinsatis2) + float(sterlinsatis3) + float(sterlinsatis5) + float(sterlinsatis7)) / 4
tcmbaudmean2 = (float(avustralyadolarsatis2) + float(avustralyadolarsatis3) + float(avustralyadolarsatis5) + float(avustralyadolarsatis7)) / 4
tcmbcnymean2 = (float(yuansatis2) + float(yuansatis3) + float(yuansatis5) + float(yuansatis7)) / 4
tcmbdkkmean2 = (float(danimarkakronusatis2) + float(danimarkakronusatis3) + float(danimarkakronusatis5) + float(danimarkakronusatis7)) / 4
tcmbsekmean2 = (float(isveckronusatis2) + float(isveckronusatis3) + float(isveckronusatis5) + float(isveckronusatis7)) / 4
tcmbchfmean2 = (float(isvicrefrangisatis2) + float(isvicrefrangisatis3) + float(isvicrefrangisatis5) + float(isvicrefrangisatis7)) / 4
tcmbjpymean2 = (float(japonyenisatis2) + float(japonyenisatis3) + float(japonyenisatis5) + float(japonyenisatis7)) / 4
tcmbcadmean2 = (float(kanadadolarisatis2) + float(kanadadolarisatis3) + float(kanadadolarisatis5) + float(kanadadolarisatis7)) / 4
tcmbkwdmean2 = (float(kuveytdinarisatis2) + float(kuveytdinarisatis3) + float(kuveytdinarisatis5) + float(kuveytdinarisatis7)) / 4
tcmbnokmean2 = (float(norveçkronusatis2) + float(norveçkronusatis3) + float(norveçkronusatis5) + float(norveçkronusatis7)) / 4
tcmbrubmean2 = (float(rusrublesisatis2) + float(rusrublesisatis3) + float(rusrublesisatis5) + float(rusrublesisatis7)) / 4
tcmbsarmean2 = (float(suudiriyalisatis2) + float(suudiriyalisatis3) + float(suudiriyalisatis5) + float(suudiriyalisatis7)) / 4

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

dövizalışmeantcmb = [round(float(ibjpymean),4), round(float(ibrubmean),4), round(float(ibnokmean),4), round(float(ibsekmean),4),
                  round(float(ibcnymean),4), round(float(ibdkkmean),4), round(float(ibsarmean),4), round(float(ibaudmean),4),
                  round(float(ibcadmean),4), round(float(ibusdmean),4), round(float(ibeurmean),4), round(float(ibchfmean),4),
                  round(float(ibgbpmean),4), round(float(ibkwdmean),4)]
dövizsatışmeantcmb = [round(float(ibjpymean2),4), round(float(ibrubmean2),4),round(float(ibnokmean2),4), round(float(ibsekmean2),4),
                round(float(ibcnymean2),4), round(float(ibdkkmean2),4), round(float(ibsarmean2),4), round(float(ibaudmean2),4),
                round(float(ibcadmean2),4), round(float(ibusdmean2),4), round(float(ibeurmean2),4), round(float(ibchfmean2),4),
                round(float(ibgbpmean2),4), round(float(ibkwdmean2),4)]


x = np.arange(len(parabirimleri))
bar_width = 0.25

plt.bar(x, dövizalışmeantcmb, width=bar_width, color='red', align='center', label='Döviz Alış Ortalama TCMB')
plt.bar(x + 0.4, dövizsatışmeantcmb, width=bar_width, color='black', align='center', label='Döviz Satış Ortalama TCMB')


plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x, parabirimleri)

plt.title('Merkez Bankası Ortalama Döviz Alış-Satış')

plt.legend(loc="upper left")

for i in range(len(parabirimleri)):
    plt.text(x[i], dövizalışmeantcmb[i], str(dövizalışmeantcmb[i]), ha='center', va='bottom', fontsize=6)
    plt.text(x[i] + 0.4, dövizsatışmeantcmb[i] + 0.5, str(dövizsatışmeantcmb[i]), ha='center', va='bottom', fontsize=6)


plt.tight_layout()
plt.show()


################## İŞ BANKASI GÜNLER İÇİN DÖVİZ KURU ALIŞ ARTIŞ İNCELEME ################

parabirimleri5 = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

onikimartibalış = [round(float(japonyenialis4),4), round(float(rusrublesialis4),4), round(float(norveçkronualis4),4), round(float(isveckronualis4),4),
                  round(float(yuanalis4),4), round(float(danimarkakronualis4),4), round(float(suudiriyalialis4),4), round(float(avustralyadolarialis4),4),
                  round(float(kanadadolarıalis4),4), round(float(abddolarialis4),4), round(float(euroalis4),4), round(float(isviçrefrangıalis4),4),
                  round(float(sterlinalis4),4), round(float(kuveytdinarialis4),4)]
onüçmartibalış = [round(float(japonyenialis),4), round(float(rusrublesialis),4),round(float(norveçkronualis),4), round(float(isveckronualis),4),
                round(float(yuanalis),4), round(float(danimarkakronualis),4), round(float(suudiriyalialis),4), round(float(avustralyadolarialis),4),
                round(float(kanadadolarıalis),4), round(float(abddolarialis),4), round(float(euroalis),4), round(float(isviçrefrangıalis),4),
                round(float(sterlinalis),4), round(float(kuveytdinarialis),4)]
ondörtmartibalış = [round(float(japonyenialis6),4), round(float(rusrublesialis6),4),round(float(norveçkronualis6),4), round(float(isveckronualis6),4),
                round(float(yuanalis6),4), round(float(danimarkakronualis6),4), round(float(suudiriyalialis6),4), round(float(avustralyadolarialis6),4),
                round(float(kanadadolarıalis6),4), round(float(abddolarialis6),4), round(float(euroalis6),4), round(float(isviçrefrangıalis6),4),
                round(float(sterlinalis6),4), round(float(kuveytdinarialis6),4)]
onbeşmartibalış = [round(float(japonyenialis8),4), round(float(rusrublesialis8),4),round(float(norveçkronualis8),4), round(float(isveckronualis8),4),
                round(float(yuanalis8),4), round(float(danimarkakronualis8),4), round(float(suudiriyalialis8),4), round(float(avustralyadolarialis8),4),
                round(float(kanadadolarıalis8),4), round(float(abddolarialis8),4), round(float(euroalis8),4), round(float(isviçrefrangıalis8),4),
                round(float(sterlinalis8),4), round(float(kuveytdinarialis8),4)]

x4 = np.arange(len(parabirimleri5)) * 4
y5 = np.arange(0, 151, 30)

bar_width4 = 0.7


plt.bar(x4 - 2, onikimartibalış, width=bar_width4, color='#1f77b4', align='center', label='Döviz Alış İB-12Mart')
plt.bar(x4 - 1, onüçmartibalış, width=bar_width4, color='#2ca02c', align='center', label='Döviz Alış İB-13Mart')
plt.bar(x4 , ondörtmartibalış, width=bar_width4, color='#ff7f0e', align='center', label='Döviz Alış İB-14Mart')
plt.bar(x4 + 1, onbeşmartibalış, width=bar_width4, color='#9467bd', align='center', label='Döviz Alış İB-15Mart')

plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x4, parabirimleri5)

plt.title('İş Bankası Döviz Alış Kur Analiz')

plt.legend(loc="upper right",fontsize = "small")

for i in range(len(x4) - 1):
    plt.axvline(x=x4[i] + 1.5, color='gray', linestyle='-', linewidth=0.5)

for i in range(len(parabirimleri5)):
    plt.text(x4[i] - 2,onikimartibalış[i] + 0.5, str(onikimartibalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x4[i] - 1,onüçmartibalış[i] + 0.5, str(onüçmartibalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x4[i],ondörtmartibalış[i] + 0.5, str(ondörtmartibalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x4[i] + 1,onbeşmartibalış[i] + 0.5, str(onbeşmartibalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")

plt.yticks(y5)
plt.tight_layout()
plt.show()

################## MERKEZ BANKASI GÜNLER İÇİN DÖVİZ KURU ALIŞ ARTIŞ İNCELEME ################

parabirimleri6 = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

onikimarttcmbalış = [round(float(japonyenialis3),4), round(float(rusrublesialis3),4), round(float(norveçkronualis3),4), round(float(isveckronualis3),4),
                  round(float(yuanalis3),4), round(float(danimarkakronualis3),4), round(float(suudiriyalialis3),4), round(float(avustralyadolaralis3),4),
                  round(float(kanadadolarialis3),4), round(float(dolaralis3),4), round(float(euroalis3),4), round(float(isvicrefrangialis3),4),
                  round(float(sterlinalis3),4), round(float(kuveytdinarialis3),4)]
onüçmarttcmbalış = [round(float(japonyenialis2),4), round(float(rusrublesialis2),4),round(float(norveçkronualis2),4), round(float(isveckronualis2),4),
                round(float(yuanalis2),4), round(float(danimarkakronualis2),4), round(float(suudiriyalialis2),4), round(float(avustralyadolaralis2),4),
                round(float(kanadadolarialis2),4), round(float(dolaralis2),4), round(float(euroalis2),4), round(float(isvicrefrangialis2),4),
                round(float(sterlinalis2),4), round(float(kuveytdinarialis2),4)]
ondörtmarttcmbalış = [round(float(japonyenialis5),4), round(float(rusrublesialis5),4),round(float(norveçkronualis5),4), round(float(isveckronualis5),4),
                round(float(yuanalis5),4), round(float(danimarkakronualis5),4), round(float(suudiriyalialis5),4), round(float(avustralyadolaralis5),4),
                round(float(kanadadolarialis5),4), round(float(dolaralis5),4), round(float(euroalis5),4), round(float(isvicrefrangialis5),4),
                round(float(sterlinalis5),4), round(float(kuveytdinarialis5),4)]
onbeşmarttcmbalış = [round(float(japonyenialis7),4), round(float(rusrublesialis7),4),round(float(norveçkronualis7),4), round(float(isveckronualis7),4),
                round(float(yuanalis7),4), round(float(danimarkakronualis7),4), round(float(suudiriyalialis7),4), round(float(avustralyadolaralis7),4),
                round(float(kanadadolarialis7),4), round(float(dolaralis7),4), round(float(euroalis7),4), round(float(isvicrefrangialis7),4),
                round(float(sterlinalis7),4), round(float(kuveytdinarialis7),4)]

x5 = np.arange(len(parabirimleri6)) * 4
y6 = np.arange(0, 151, 30)

bar_width4 = 0.7


plt.bar(x5 - 2, onikimarttcmbalış, width=bar_width4, color='#1f77b4', align='center', label='Döviz Alış TCMB-12Mart')
plt.bar(x5 - 1, onüçmarttcmbalış, width=bar_width4, color='#2ca02c', align='center', label='Döviz Alış TCMB-13Mart')
plt.bar(x5 , ondörtmarttcmbalış, width=bar_width4, color='#ff7f0e', align='center', label='Döviz Alış TCMB-14Mart')
plt.bar(x5 + 1, onbeşmarttcmbalış, width=bar_width4, color='#9467bd', align='center', label='Döviz Alış TCMB-15Mart')

plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x5, parabirimleri6)

plt.title('Merkez Bankası Döviz Alış Kur Analiz')

plt.legend(loc="upper right",fontsize = "small")

for i in range(len(x5) - 1):
    plt.axvline(x=x5[i] + 1.5, color='gray', linestyle='-', linewidth=0.5)

for i in range(len(parabirimleri5)):
    plt.text(x5[i] - 2,onikimarttcmbalış[i] + 0.5, str(onikimarttcmbalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i] - 1,onüçmarttcmbalış[i] + 0.5, str(onüçmarttcmbalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i],ondörtmarttcmbalış[i] + 0.5, str(ondörtmarttcmbalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i] + 1,onbeşmarttcmbalış[i] + 0.5, str(onbeşmarttcmbalış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")

plt.yticks(y5)
plt.tight_layout()
plt.show()

################## İŞ BANKASI GÜNLER İÇİN DÖVİZ KURU SATIŞ ARTIŞ İNCELEME ################

parabirimleri = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

onikimartibsatış = [round(float(japonyenisatis4),4), round(float(rusrublesisatis4),4), round(float(norveçkronusatis4),4), round(float(isveçkronusatis4),4),
                  round(float(yuansatis4),4), round(float(danimarkakronusatis4),4), round(float(suudiriyalisatis4),4), round(float(avustralyadolarisatis4),4),
                  round(float(kanadadolarisatis4),4), round(float(abddolarisatis4),4), round(float(eurosatis4),4), round(float(isviçrefrangısatis4),4),
                  round(float(sterlinsatis4),4), round(float(kuveytdinarisatis4),4)]
onüçmartibsatış = [round(float(japonyenisatis),4), round(float(rusrublesisatis),4),round(float(norveçkronusatis),4), round(float(isveçkronusatis),4),
                round(float(yuansatis),4), round(float(danimarkakronusatis),4), round(float(suudiriyalisatis),4), round(float(avustralyadolarisatis),4),
                round(float(kanadadolarisatis),4), round(float(abddolarisatis),4), round(float(eurosatis),4), round(float(isviçrefrangısatis),4),
                round(float(sterlinsatis),4), round(float(kuveytdinarisatis),4)]
ondörtmartibsatış = [round(float(japonyenisatis6),4), round(float(rusrublesisatis6),4),round(float(norveçkronusatis6),4), round(float(isveçkronusatis6),4),
                round(float(yuansatis6),4), round(float(danimarkakronusatis6),4), round(float(suudiriyalisatis6),4), round(float(avustralyadolarisatis6),4),
                round(float(kanadadolarisatis6),4), round(float(abddolarisatis6),4), round(float(eurosatis6),4), round(float(isviçrefrangısatis6),4),
                round(float(sterlinsatis6),4), round(float(kuveytdinarisatis6),4)]
onbeşmartibsatış = [round(float(japonyenisatis8),4), round(float(rusrublesisatis8),4),round(float(norveçkronusatis8),4), round(float(isveçkronusatis8),4),
                round(float(yuansatis8),4), round(float(danimarkakronusatis8),4), round(float(suudiriyalisatis8),4), round(float(avustralyadolarisatis8),4),
                round(float(kanadadolarisatis8),4), round(float(abddolarisatis8),4), round(float(eurosatis8),4), round(float(isviçrefrangısatis8),4),
                round(float(sterlinsatis8),4), round(float(kuveytdinarisatis8),4)]

x = np.arange(len(parabirimleri)) * 4
y = np.arange(0, 151, 30)

bar_width4 = 0.7


plt.bar(x - 2, onikimartibsatış, width=bar_width4, color='#1abc9c', align='center', label='Döviz Satış İB-12Mart')
plt.bar(x - 1, onüçmartibsatış, width=bar_width4, color='#9b59b6', align='center', label='Döviz Satış İB-13Mart')
plt.bar(x , ondörtmartibsatış, width=bar_width4, color='#e67e22', align='center', label='Döviz Satış İB-14Mart')
plt.bar(x + 1, onbeşmartibsatış, width=bar_width4, color='#2ecc71', align='center', label='Döviz Satış İB-15Mart')

plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x, parabirimleri)

plt.title('İş Bankası Döviz Satış Kur Analiz')

plt.legend(loc="upper right",fontsize = "small")

for i in range(len(x) - 1):
    plt.axvline(x=x[i] + 1.5, color='gray', linestyle='-', linewidth=0.5)

for i in range(len(parabirimleri)):
    plt.text(x[i] - 2,onikimartibsatış[i] + 0.5, str(onikimartibsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x[i] - 1,onüçmartibsatış[i] + 0.5, str(onüçmartibsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x[i],ondörtmartibsatış[i] + 0.5, str(ondörtmartibsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x[i] + 1,onbeşmartibsatış[i] + 0.5, str(onbeşmartibsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")

plt.yticks(y)
plt.tight_layout()
plt.show()

################## MERKEZ BANKASI GÜNLER İÇİN DÖVİZ KURU SATIŞ ARTIŞ İNCELEME ################

parabirimleri7 = ["JPY", "RUB", "NOK", "SEK", "CNY", "DKK", "SAR", "AUD", "CAD", "USD", "EUR", "CHF", "GBP", "KWD"]

onikimarttcmbsatış = [round(float(japonyenisatis3),4), round(float(rusrublesisatis3),4), round(float(norveçkronusatis3),4), round(float(isveckronusatis3),4),
                  round(float(yuansatis3),4), round(float(danimarkakronusatis3),4), round(float(suudiriyalisatis3),4), round(float(avustralyadolarsatis3),4),
                  round(float(kanadadolarisatis3),4), round(float(dolarsatis3),4), round(float(eurosatis3),4), round(float(isvicrefrangisatis3),4),
                  round(float(sterlinsatis3),4), round(float(kuveytdinarisatis3),4)]
onüçmarttcmbsatış = [round(float(japonyenisatis2),4), round(float(rusrublesisatis2),4),round(float(norveçkronusatis2),4), round(float(isveckronusatis2),4),
                round(float(yuansatis2),4), round(float(danimarkakronusatis2),4), round(float(suudiriyalisatis2),4), round(float(avustralyadolarsatis2),4),
                round(float(kanadadolarisatis2),4), round(float(dolarsatis2),4), round(float(eurosatis2),4), round(float(isvicrefrangisatis2),4),
                round(float(sterlinsatis2),4), round(float(kuveytdinarisatis2),4)]
ondörtmarttcmbsatış = [round(float(japonyenisatis5),4), round(float(rusrublesisatis5),4),round(float(norveçkronusatis5),4), round(float(isveckronusatis5),4),
                round(float(yuansatis5),4), round(float(danimarkakronusatis5),4), round(float(suudiriyalisatis5),4), round(float(avustralyadolarsatis5),4),
                round(float(kanadadolarisatis5),4), round(float(dolarsatis5),4), round(float(eurosatis5),4), round(float(isvicrefrangisatis5),4),
                round(float(sterlinsatis5),4), round(float(kuveytdinarisatis5),4)]
onbeşmarttcmbsatış = [round(float(japonyenisatis7),4), round(float(rusrublesisatis7),4),round(float(norveçkronusatis7),4), round(float(isveckronusatis7),4),
                round(float(yuansatis7),4), round(float(danimarkakronusatis7),4), round(float(suudiriyalisatis7),4), round(float(avustralyadolarsatis7),4),
                round(float(kanadadolarisatis7),4), round(float(dolarsatis7),4), round(float(eurosatis7),4), round(float(isvicrefrangisatis7),4),
                round(float(sterlinsatis7),4), round(float(kuveytdinarisatis7),4)]

x5 = np.arange(len(parabirimleri7)) * 4
y6 = np.arange(0, 151, 30)

bar_width4 = 0.7


plt.bar(x5 - 2, onikimarttcmbsatış, width=bar_width4, color='#1abc9c', align='center', label='Döviz Satış TCMB-12Mart')
plt.bar(x5 - 1, onüçmarttcmbsatış, width=bar_width4, color='#9b59b6', align='center', label='Döviz Satış TCMB-13Mart')
plt.bar(x5 , ondörtmarttcmbsatış, width=bar_width4, color='#e67e22', align='center', label='Döviz Satış TCMB-14Mart')
plt.bar(x5 + 1, onbeşmarttcmbsatış, width=bar_width4, color='#2ecc71', align='center', label='Döviz Satış TCMB-15Mart')

plt.xlabel('Para Birimleri')
plt.ylabel('Fiyat')

plt.xticks(x5, parabirimleri7)

plt.title('Merkez Bankası Döviz Satış Kur Analiz')

plt.legend(loc="upper right",fontsize = "small")

for i in range(len(x5) - 1):
    plt.axvline(x=x5[i] + 1.5, color='gray', linestyle='-', linewidth=0.5)

for i in range(len(parabirimleri5)):
    plt.text(x5[i] - 2,onikimarttcmbsatış[i] + 0.5, str(onikimarttcmbsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i] - 1,onüçmarttcmbsatış[i] + 0.5, str(onüçmarttcmbsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i],ondörtmarttcmbsatış[i] + 0.5, str(ondörtmarttcmbsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")
    plt.text(x5[i] + 1,onbeşmarttcmbsatış[i] + 0.5, str(onbeşmarttcmbsatış[i]), ha='center', va='bottom', fontsize=8,rotation = 90,fontweight = "bold")

plt.yticks(y5)
plt.tight_layout()
plt.show()

























































