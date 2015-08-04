#!/usr/bin/env python
# Este archivo usa el encoding: utf-8
import re

clean = {}

seller = "Christie's"
price_dollars = 150000
price_original_currency = 200000
currency = "GBP"
city = "London"
premium_hammer = "Hammer"


if premium_hammer=="Hammer":

#### Sotheby's ####
    if seller=="Sotheby's":
        if city=="New York":
            if price_dollars <= 200000:
                new_price=price_dollars*1.25
            elif price_dollars<=3000000 and price_dollars>200000:
                new_price=price_dollars*1.20
            else:
                new_price = price_dollars*1.12
        elif city=="London":
            if currency=="GBP" and price_original_currency<=100000:
                new_price=price_dollars*1.25
            elif currency=="GBP" and price_original_currency<=1800000 and price_original_currency>100000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Hong Kong":
            if currency=="HKD" and price_original_currency<=1600000:
                new_price=price_dollars*1.25
            elif currency=="HKD" and price_original_currency<=22500000 and price_original_currency>1600000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Paris":
            if currency=="EUR" and price_original_currency<=60000:
                new_price=price_dollars*1.25
            elif currency=="EUR" and price_original_currency<=1800000 and price_original_currency>60000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Milan":
            if currency=="EUR" and price_original_currency<=60000:
                new_price=price_dollars*1.305
            elif currency=="EUR" and price_original_currency<=1800000 and price_original_currency>60000:
                new_price=price_dollars*1.244
            else:
                new_price=price_dollars*1.1464
        elif city=="Beijing":
                new_price=price_dollars*1.18
        else:
            if currency=="CHF" and price_original_currency<=200000:
                new_price=price_dollars*1.25
            elif currency=="CHF" and price_original_currency<=3000000 and price_original_currency>200000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12

###  Christie's ###
    elif seller=="Christie's":
        if city=="    new York":
            if price_dollars <= 100000:
                new_price=price_dollars*1.25
            elif price_dollars<=2000000 and price_dollars>100000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="London":
            if currency=="GBP" and price_original_currency<=50000:
                new_price=price_dollars*1.25
            elif currency=="GBP" and price_original_currency<=1000000 and price_original_currency>50000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Paris":
            if currency=="EUR" and price_original_currency<=30000:
                new_price=price_dollars*1.25
            elif currency=="EUR" and price_original_currency<=1200000 and price_original_currency>30000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Amsterdam":
            if currency=="EUR" and price_original_currency<=30000:
                new_price=price_dollars*1.3025
            elif currency=="EUR" and price_original_currency<=1200000 and price_original_currency>30000:
                new_price=price_dollars*1.242
            else:
                new_price=price_dollars*1.1452
        elif city=="Milan":
            if currency=="EUR" and price_original_currency<=30000:
                new_price=price_dollars*1.30
            elif currency=="EUR" and price_original_currency<=1200000 and price_original_currency>30000:
                new_price=price_dollars*1.26
            else:
                new_price=price_dollars*1.185
        elif city=="Geneva":
            if currency=="CHF" and price_original_currency<=100000:
                new_price=price_dollars*1.25
            elif currency=="CHF" and price_original_currency<=2000000 and price_original_currency>100000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Zurich":
                new_price=price_dollars*1.20
        elif city=="Hong Kong":
            if currency=="HKD" and price_original_currency<=800000:
                new_price=price_dollars*1.25
            elif currency=="HKD" and price_original_currency<=15000000 and price_original_currency>800000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Dubai":
            if price_dollars<=100000:
                new_price=price_dollars*1.25
            elif price_dollars<=2000000 and price_dollars>100000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        elif city=="Mumbai":
            if currency=="INR" and price_original_currency<=4500000:
                new_price=price_dollars*1.25
            elif currency=="INR" and price_original_currency<=90000000 and price_original_currency>4500000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12
        else: 
            if currency=="RMB" and price_original_currency<=600000:
                new_price=price_dollars*1.25
            elif currency=="RMB" and price_original_currency<=12000000 and price_original_currency>600000:
                new_price=price_dollars*1.20
            else:
                new_price=price_dollars*1.12

###  Morton y todo lo demás ###

    else: 
        new_price=price_dollars*1.20

else:
    new_price=price_dollars

print new_price
