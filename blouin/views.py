#!/usr/bin/env python
# Este archivo usa el encoding: utf-8
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from blouin.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from .models import *
from .forms import PaintingForm
#from django.utils import timezone
#from .forms import PostForm
import csv, StringIO
import json
import re
import sys
import requests
from bs4 import BeautifulSoup
import re
from scrapely import Scraper
import mechanize
import random
import socks
import socket
from random import randint
from time import sleep
import codecs
from PIL import Image as PImage
from artproject.settings import MEDIA_ROOT
from quantil import quantil_placer
from r_estimation import *


def quality(request):
    q = Painting.objects.all()
    ### markings cleanup ###
    for i in q:
        s = i.painter
        print s
        p = i.new_price
        print p
        ids = i.id
        quality = quantil_placer(s,p)
        Painting.objects.filter(id =ids).update(quality = quality)
    return HttpResponse(s)


### second clean data, for materials ###

clean = {}
painting_list = [
'wood',
'canvas', 
'acrylic',
'acrylic ',
'linen',
'alluminum',
'aluminum',
'plexiglass',
'panel',
'masonite',
'plate',
'board',
'burlap',
'canvas',
'canvasboard',
'plastic',
'jute',
'marais',
'metal',
'mylar',
'gunny',
'cloth',
'plaster',
'plywood',
'Plexiglas',
'saunders',
'Stonehenge',
'three-ply',
'frame',
'oil',
'oil ',
'oil on tin',
'oil and sand',
'oil and charcoal',
'oil and gold leaf',
'tempera',
]

paper_list = [
'paper', 
'cardboard',
'oilstick',
'arches',
'China paper',
'Chinese paper',
'paper',
'etching',
'newsprint',
'acetate',
'sketchbook',
'sketch',
'wove',
'vellum',
]

lithograph_list = [
'lithograph',
'serigraph',
'mixografia',

]

def clean_data2(request):
    q = Painting.objects.all()
    ### markings cleanup ###
    for i in q:
        s = i.materials_dummy
        ss = s.strip()
        ids = i.id
        if any(word in ss.lower() for word in painting_list):
            clean['materials_dummy2'] = 'painting'
        else:
            if any(word in ss.lower() for word in paper_list):
                clean['materials_dummy2'] = 'paper'
            else:
                clean['materials_dummy2'] = 'other'

        print "is %s" % clean['materials_dummy2']
        Painting.objects.filter(id =ids).update(materials_dummy2 = clean['materials_dummy2'])
    return HttpResponse(s)


### clean data function ###

def clean_data(request):
    q = Painting.objects.all()
    
    ### markings cleanup ###
    for i in q:
        s = i.markings
        ids = i.id
        m = re.findall("signed", s, re.IGNORECASE)
        try:
            t = m[0]
            t = 1
        except IndexError:
            t = 0
            clean['markings_dummy'] = 0
        w = re.findall("\w+", s)
        l = len(w)
        if l == 1 and t == 1:
            clean['markings_dummy'] = 1
        if l > 1 and t ==1:
            clean['markings_dummy'] = 2
        
        print s
        print clean['markings_dummy']
        Painting.objects.filter(id =ids).update(markings_dummy = clean['markings_dummy'])


    #### provenance clean up ###

        pro = i.provenance
        pro_c = re.findall(";", pro)
        pro_l = len(pro_c)
        clean['provenance_dummy'] = pro_l
        Painting.objects.filter(id =ids).update(provenance_dummy = clean['provenance_dummy'])

    ### lot clean up ###
    ### auction house clean up ###
        lot = i.lot
        ch = re.findall("Christie's", lot, re.IGNORECASE)
        so = re.findall("Sotheby's", lot, re.IGNORECASE)
        mo = re.findall("Morton's", lot, re.IGNORECASE)
        alls = re.findall("Morton's", lot, re.IGNORECASE)
        
        clean['auction_house'] = "other"
        try:
            ch_c = ch[0]
            clean['auction_house'] = "Christie's"
        except IndexError:
            "not christie's"
        try:
            so_c = so[0]
            clean['auction_house'] = "Sotheby's"
        except IndexError:
            "not sotheby's"
        try:
            mo_c = mo[0]
            clean['auction_house'] = "Morton's"
        except IndexError:
            "not morton's"

        Painting.objects.filter(id =ids).update(auction_house = clean['auction_house'])

    ### city clean up ###
        city = i.lot
        city_c = re.findall(r"\, (.*) \(", lot) 
        print city_c
        city_cc = city_c[0]
        clean['city'] = city_cc

        Painting.objects.filter(id =ids).update(city_sale = clean['city'])

    ### description clean up ###
        desc = i.description
        desc_c = re.findall(r"certificate", desc)
        try:
            desc_cc = desc_c[0]
            clean['certificate_dummy'] = 1
        except IndexError:
            clean['certificate_dummy'] = 0

        Painting.objects.filter(id =ids).update(certificate_dummy = clean['certificate_dummy'])

        ### sale date year clean up ###
        saley = i.sale_date
        saley_c = re.findall('\d+',saley)
        saley_cc = saley_c[1]
        clean['sale_year'] = saley_cc

        Painting.objects.filter(id =ids).update(sale_year = clean['sale_year'])

        ### materials clean up ###

        matd = i.materials
        try:
            matd_c = matd.split("on",1)[1].strip()
            clean['materials_dummy'] = matd_c
        except IndexError:
            clean['materials_dummy'] = "other"

        print clean['materials_dummy']

        Painting.objects.filter(id =ids).update(materials_dummy = clean['materials_dummy'])

        ### if dead soon clean up ###

        dead = i.nationality
        years = re.findall("\d+", dead)
        dead_c = re.findall("-",dead)

        try:
            dead_cc = dead_c[0]
            clean['dead_soon'] = 0
        except IndexError:
            years = re.findall("\d+", dead)
            print years
            year_born = int(years[0])
            print year_born
            age = 2015 - year_born
            print age
            if age > 80:
                clean['dead_soon'] = 1


        print clean['dead_soon']

        i.dead_soon = clean['dead_soon']

        Painting.objects.filter(id =ids).update(dead_soon = clean['dead_soon'])
    
    ### new price clean up ###
        if i.premium_hammer=="Hammer":

        #### Sotheby's ####
            if i.auction_house=="Sotheby's":
                if i.city_sale=="New York":
                    if i.price_dollars <= 200000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.price_dollars<=3000000 and i.price_dollars>200000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price'] = i.price_dollars*1.12
                elif i.city_sale=="London":
                    if i.currency=="GBP" and i.price_original_currency<=100000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="GBP" and i.price_original_currency<=1800000 and i.price_original_currency>100000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Hong Kong":
                    if i.currency=="HKD" and i.price_original_currency<=1600000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="HKD" and i.price_original_currency<=22500000 and i.price_original_currency>1600000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Paris":
                    if i.currency=="EUR" and i.price_original_currency<=60000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="EUR" and i.price_original_currency<=1800000 and i.price_original_currency>60000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Milan":
                    if i.currency=="EUR" and i.price_original_currency<=60000:
                        clean['new_price']=i.price_dollars*1.305
                    elif i.currency=="EUR" and i.price_original_currency<=1800000 and i.price_original_currency>60000:
                        clean['new_price']=i.price_dollars*1.244
                    else:
                        clean['new_price']=i.price_dollars*1.1464
                elif i.city_sale=="Beijing":
                        clean['new_price']=i.price_dollars*1.18
                else:
                    if i.currency=="CHF" and i.price_original_currency<=200000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="CHF" and i.price_original_currency<=3000000 and i.price_original_currency>200000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12

        ###  Christie's ###
            elif i.auction_house=="Christie's":
                if i.city_sale=="    new York":
                    if i.price_dollars <= 100000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.price_dollars<=2000000 and i.price_dollars>100000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="London":
                    if i.currency=="GBP" and i.price_original_currency<=50000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="GBP" and i.price_original_currency<=1000000 and i.price_original_currency>50000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Paris":
                    if i.currency=="EUR" and i.price_original_currency<=30000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="EUR" and i.price_original_currency<=1200000 and i.price_original_currency>30000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Amsterdam":
                    if i.currency=="EUR" and i.price_original_currency<=30000:
                        clean['new_price']=i.price_dollars*1.3025
                    elif i.currency=="EUR" and i.price_original_currency<=1200000 and i.price_original_currency>30000:
                        clean['new_price']=i.price_dollars*1.242
                    else:
                        clean['new_price']=i.price_dollars*1.1452
                elif i.city_sale=="Milan":
                    if i.currency=="EUR" and i.price_original_currency<=30000:
                        clean['new_price']=i.price_dollars*1.30
                    elif i.currency=="EUR" and i.price_original_currency<=1200000 and i.price_original_currency>30000:
                        clean['new_price']=i.price_dollars*1.26
                    else:
                        clean['new_price']=i.price_dollars*1.185
                elif i.city_sale=="Geneva":
                    if i.currency=="CHF" and i.price_original_currency<=100000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="CHF" and i.price_original_currency<=2000000 and i.price_original_currency>100000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Zurich":
                        clean['new_price']=i.price_dollars*1.20
                elif i.city_sale=="Hong Kong":
                    if i.currency=="HKD" and i.price_original_currency<=800000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="HKD" and i.price_original_currency<=15000000 and i.price_original_currency>800000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Dubai":
                    if i.price_dollars<=100000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.price_dollars<=2000000 and i.price_dollars>100000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                elif i.city_sale=="Mumbai":
                    if i.currency=="INR" and i.price_original_currency<=4500000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="INR" and i.price_original_currency<=90000000 and i.price_original_currency>4500000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12
                else: 
                    if i.currency=="RMB" and i.price_original_currency<=600000:
                        clean['new_price']=i.price_dollars*1.25
                    elif i.currency=="RMB" and i.price_original_currency<=12000000 and i.price_original_currency>600000:
                        clean['new_price']=i.price_dollars*1.20
                    else:
                        clean['new_price']=i.price_dollars*1.12

        ###  Morton y todo lo demás ###

            else: 
                clean['new_price']=i.price_dollars*1.20

        else:
            clean['new_price']=i.price_dollars

        Painting.objects.filter(id =ids).update(new_price = clean['new_price'])



    return HttpResponse(s)

### second attempt at forms, works!! working form ###
def search_form(request):
    form = PaintingForm(request.GET)
    return render(request, 'blouin/search_form.html', {'form': form})


## dictionary to keep saved results
search_query = {}
### returns search results from search_form ###
def search(request):
    # request_params = request.GET.copy()
    if 'painter' in request.GET and request.GET['painter']:
        q = request.GET['painter']
        #t = request.GET['title'] if she wants it
        s = request.GET['year']
        w = request.GET['width']#*100 # get rido of decimals
        h = request.GET['height']#*100 # get rid of decimals
        m = request.GET['materials']       
        qual = request.GET['quality']
        
        if qual == "":
            qual = 0
        else:
            qual = request.GET['quality']

        

        ### condition so it does not break when it does not find input ###
        
        pp = {'painter__icontains': q}
        
        if s != "":
        ### year ranges ###
            y_h = int(s) + 2
            y_l = int(s) - 2
            aa = {'year__range': (y_l, y_h)}
        else:
            aa = {'year__icontains': s}
            s = 0

        ### height and width ranges ###
        if w != "": 
            a = float(w)
            w_h = int(w)*1.25
            w_l = int(w)*.75
            bb = {'width__range': (w_l, w_h)}
        else:
            bb = {'width__icontains': w}
            w = 0

        ### height and width ranges ###
        if h != "":
            b = float(h)
            h_h = int(h)*1.25
            h_l = int(h)*.75
            cc = {'height__range': (h_l, h_h)}
        else:
            cc = {'height__icontains': h}
            h = 0

        mm = {'materials_dummy2__icontains': m}

        ### funtion to append dictionaries ###
        z1 = pp.copy()
        z1.update(aa)
        z2 = z1.copy()
        z2.update(bb)
        z3 = z2.copy()
        z3.update(cc)
        z4 = z3.copy()
        z4.update(mm)
        global search_query
        search_query = z4
        print search_query
        no_image = Painting.objects.get(id = 6934).image1 ### no image file
        paintings = Painting.objects.filter(**z4) ## using function keys

        estimation_results_raw = price_estimation(q, float(s), float(h), float(w), m, int(qual))
        #estimation_results_raw = price_estimation(q, float(s), float(h), float(w), m, int(qual)    
        print estimation_results_raw
        estimation_results_h = '${:,.2f}'.format(estimation_results_raw*.825)
        estimation_results_l = '${:,.2f}'.format(estimation_results_raw*1.175) 
        estimation_results = estimation_results_h + " - " + estimation_results_l 

        # year = Painting.objects.filter(year__icontains = )
        return render(request, 'blouin/search_results.html',
            {'paintings': paintings, 'no_image': no_image, 'estimation_results': estimation_results})
    else:
        return render(request, 'blouin/search_form.html', {'error': True})

### captures adjusted estimation from search results ###
def estimation(request):
    no_image = Painting.objects.get(id = 6934).image1 ### no image file
    if 'list' in request.GET:
        estimation_results = 10
        print search_query

        paintings = Painting.objects.filter(**search_query) ## using function keys
        return render(request, 'blouin/search_results.html',
            {'paintings': paintings, 'no_image': no_image, 'estimation_results': estimation_results})
        # return HttpResponseRedirect(reverse('search'))
    else:
        "nothin"


    ### pretty html template ###

def blog_single(request):
        return render(request, 'blouin/blog-single.htm')



### print to httml all entries with attached pictures ###

def post_list(request):
    recent_posts = Painting.objects.all()
    template = loader.get_template('blouin/post_list.html')
    context = Context({'painting_list': recent_posts})
    return HttpResponse(template.render(context))
    #return render(request, 'blouin/post_list.html')

### first attempt at forms ###

    
### helper code to print to csv ###

class DictUnicodeWriter(object):

    def __init__(self, f, fieldnames, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, D):
        self.writer.writerow({k:v.encode("utf-8") for k,v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for D in rows:
            self.writerow(D)

    def writeheader(self):
        self.writer.writeheader()

class UnicodeWriter(object):
  
    def __init__(self, f, dialect=csv.excel_tab, encoding="utf-16", **kwds):
        # Redirect output to a queue
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoding = encoding
    
    def writerow(self, row):
        # Modified from original: now using unicode(s) to deal with e.g. ints
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = data.encode(self.encoding)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

fieldnames = [
'title', 
'price',
'new_price',
'painter', 
'nationality',  
'markings', 
'original_currency',    
'price_original_currency', 
'price_dollars', 
'currency', 
'exhibited',
'edition', 
'condition', 
'year', 
'estimate', 
'low_estimate', 
'high_estimate', 
'measurements',
'url',
'sizenotes', 
'provenance',
'auction_data',    
'lot',    
'description',     
'literature',
'materials',    
'sale_date',
'premium_hammer',
'width',
'height',
'depth', 
'markings_dummy',
'provenance_dummy',
'auction_house',
'city_sale',
'certificate_dummy',
'sale_year',
'materials_dummy',
'dead_soon',
'materials_dummy2',
]

### prints to csv all the database code ###

def test1(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    
    writer = UnicodeWriter(response)
    writer.writerow(fieldnames)
    i = 1
    while i<6933:
        try:
            q = Painting.objects.get(id = i)
            writer.writerow([
            q.title, 
            q.price,
            q.new_price,
            q.painter, 
            q.nationality, 
            q.markings, 
            q.original_currency,    
            q.price_original_currency, 
            q.price_dollars, 
            q.currency, 
            q.exhibited,
            q.edition, 
            q.condition, 
            q.year, 
            q.estimate, 
            q.low_estimate, 
            q.high_estimate, 
            q.measurements,
            q.url,
            q.sizenotes, 
            q.provenance,
            q.auction_data,    
            q.lot,    
            q.description,     
            q.literature,
            q.materials,    
            q.sale_date,
            q.premium_hammer,
            q.width,
            q.height,
            q.depth, 
            q.markings_dummy,
            q.provenance_dummy,
            q.auction_house,
            q.city_sale,
            q.certificate_dummy,
            q.sale_year,
            q.materials_dummy,
            q.dead_soon,
            q.materials_dummy2,
            ])
            i += 1
        except ObjectDoesNotExist: #DoesNotExist:
            i += 1

    
    return response



#### Get python to ignore robot handler, caution breaks web page rules! #####

br = mechanize.Browser()
br.set_handle_robots(False)

### procedure to mask user agent #####


#afile = open('fakeuser.txt', 'r') # file with fake user 

### random line grab from file ###

# def random_line(afile): 
#     line = next(afile)
#     for num, aline in enumerate(afile):
#       if random.randrange(num + 2): continue
#       line = aline
#     return line

### variable with fake user grabbed randomly   #####
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' #random_line(afile)



### use tor proxy server to hide ip address ###
#for some reason it doesn work on reforma.com!

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket


### sample ###

### carlos cruz diez no funciona, fix iiittt ###

sample = {
'Leonora_Carrington':'http://artsalesindex.artinfo.com/asi/search/Leonora_Carrington/artistAuctions.ai?artistID=29224',
'Cruz_Diez':'http://artsalesindex.artinfo.com/asi/search/Carlos_Cruz-Diez/artistAuctions.ai?artistID=39409',
'Cruz_Diez':'http://artsalesindex.artinfo.com/asi/results.action?page=3&sort=3&uom=in&dir=desc&currency=USD',
'Wilfredo_Lam':'http://artsalesindex.artinfo.com/asi/search/Wifredo_Lam/artistAuctions.ai?artistID=97681',
'Rufino_Tamayo':'http://artsalesindex.artinfo.com/asi/search/Rufino_Tamayo/artistAuctions.ai?artistID=173265',
'Pedro_Coronel':'http://artsalesindex.artinfo.com/asi/search/Pedro_Coronel/artistAuctions.ai?artistID=37207'
}

### extra artists ###

extra = {
'Cundo_Bermudez':'http://artsalesindex.artinfo.com/asi/search/Cundo_Bermudez/artistAuctions.ai?artistID=14042',
'Jose_Clemente_Orozco': 'http://artsalesindex.artinfo.com/asi/search/Jose%20Clemente_Orozco/artistAuctions.ai?artistID=131583',
'David_Alfaro_Siqueiros': 'http://artsalesindex.artinfo.com/asi/search/David%20Alfaro_Siqueiros/artistAuctions.ai?artistID=164630',
'Diego_Rivera': 'http://artsalesindex.artinfo.com/asi/search/Diego_Rivera/artistAuctions.ai?artistID=149187',
'Jean_Michel_Basquiat': 'http://artsalesindex.artinfo.com/asi/search/Jean-Michel_Basquiat/artistAuctions.ai?artistID=10108',
'Frida_Kahlo': 'http://artsalesindex.artinfo.com/asi/search/Frida_Kahlo/artistAuctions.ai?artistID=89440'
}

total = {}
total.update(sample)
total.update(extra)

currencies = "ARS|AUD|CAD|CHF|CLP|CNY|COP|EUR|GBP|HKD|ILS|INR|JEP|JPY|KRW|KWD|KYD|MXN|RUB|SAR|SEK|SGD|TOP|TRY|TWD|USD|UYU|VEF|ZAR|"

keys2 = [
'Markings:', 
'Literature:', 
'high_estimate', 
'height',
'currency',
'year',
'title',
'price_original_currency',
'depth',
'width',
'low_estimate',
'lot',
'auction_date',
'Description:',
'auction_data',
'premium',
'original_currency',
'price',
'Exhibited:',
'Edition:',
'Condition:',
'nationality',
'estimate',
'painter',
'Measurements:',
'url',
'Size Notes:',
'Provenance:',
'Materials:',
'price_dollars',]

#print total 
home_url = "http://artsalesindex.artinfo.com/" 

full_list = []

### fills the database with requests to blouin, must update list of artists in the total dict ###

### gets info from website using beautiful soup (might have to change everything to usable string code) ####
def index(request):
    full_list = []
    for key in total:
        artist_url = total[key]
        print artist_url
        page = 1
        while page <= 100:
            headers = {'User-Agent': user_agent}
            url = artist_url + "&page=%s" % page
            
            ### alternate url, cruz diez ###
            #url = 'http://artsalesindex.artinfo.com/asi/results.action?page=%s&sort=3&uom=in&dir=desc&currency=USD' % page
            source_code = requests.get(url, headers=headers)    
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            print url
            for link in soup.findAll("div", {"class": "results-title"}):
                #print link
                links = link.findAll("a")
                #print links
                for linkspaintings in links:
                    aa = linkspaintings.get("href")
                    links = home_url + aa
                    print links
                    link_scrape(links)
                    #data = link_scrape(links)
                    #sleep(randint(2,8))
            page = page +1
            #print page
    return HttpResponse() 

# variable containers ####

keys0 = ['original_currency','estimate'] # dict keys used when find all iterates over items

characs = {}
charac_list = []

### scrapes the links from the websites ###

def link_scrape(url):
    headers = {'User-Agent': user_agent}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html5lib') # create soup class readable object
    characs['url'] = url
    data = soup.findAll("div", {"id": "artworkIndex_0"})
    data_container = data[0]
    #print data_container
    for i in data_container.findAll("div", {"class":"artist"}): # find and clean painter name
        painter_name_raw = i.find("a")
        painter_name_text = painter_name_raw.text.strip()
        #print painter_name_text
        b = painter_name_text.splitlines()
        painter_name = b[0].strip() +" " + b[1].strip()
        characs['painter'] = painter_name
        #print characs['painter']
    for nationality_raw in data_container.findAll("p", {"class":"artist-nationality"}): # find and clean nationality
        characs['nationality'] = nationality_raw.text.strip()
        #print characs['nationality']
    for title_raw in data_container.findAll("h4", {"class":"title"}):
        characs['title'] = title_raw.text.strip()
        #print characs['title']
    for lot_raw in data_container.findAll("h2", {"class":"lotnumber"}): # find and clean lot number
        characs['lot'] = lot_raw.text.strip()
        #print characs['lot']
    for year_raw in data_container.findAll("p", {"style":"font-family:'Arial'; font-size: 12.5px; font-weight:600; color:#000000; margin:0; padding:0; line-height:16px;"}): # year 
        a = year_raw.text.strip()
        y = a.strip()
        
        if "-" and "Circa" in y:
            b = y.split()
            year = b[1].strip()
            characs['year'] = int(year)
            print characs['year']
        elif "Circa" in y:
            #print "found"
            b = y.splitlines()
            year = b[1].strip()
            characs['year'] = int(year)
            #print characs['year']
        elif "-" in y:
            #print "found"
            b = y.splitlines()
            year = b[0].strip()
            characs['year'] = int(year)
            #print characs['year']
        elif "Before" in y:
            c = re.findall('\d+',y)
            characs['year'] = int(c[0])
        else:
            characs['year'] = y
    
    


        #print characs['year']
    
    
            #print characs['year']
    for auction_data_raw in data_container.findAll("p", {"class":"auctiondata"}): # find and clean auction info
        characs['auction_data'] = auction_data_raw.text.strip()
        #print characs['auction_data']
    for x in data_container.findAll("div", {"class":"price"}): # find and clean price
        characs['price'] = x.text.strip()
        #print characs['price']
    y = 0
    for x in data_container.find_all("div", {"class":"lot-details1"}, recursive = False): # estimate and original currency
        info = x.text
        characs[keys0[y]] = info
        #print characs[keys0[y]]
        y += 1
    for x in data_container.find_all("p", {"class": "artworkdetails"}): # find and clean all other characteristics
        #print x
        for keys in x.find("b"):
            #print keys
            content = x.br.next_sibling
        #print content
            characs[keys] = content
    
    #print characs
    
### cleaning data ###
    # currency list #
    
    try:
        price_raw = re.findall("\d+", characs['original_currency'])
        characs['price_original_currency'] = ''.join(price_raw)
    except IndexError:
        characs['price_original_currency'] = 0
    print characs['price_original_currency']

    if characs['price_original_currency'] == '':
        characs['price_original_currency'] = 0

    currency_raw = re.findall(currencies, characs['original_currency'])
    characs['currency'] = ''.join(currency_raw)
    print characs['currency']

    premium = re.findall('Premium|Hammer',characs['original_currency'])    
    try:
        characs['premium'] = premium[0]
    except IndexError:
        characs['premium'] = "bought in"

    price_dollars_raw = re.findall(".+?(?=USD)", characs['price'])
    try:
        price_dollars = re.findall("\d+", price_dollars_raw[0])
        characs['price_dollars'] = "".join(price_dollars)
    except IndexError:
        characs['price_dollars'] = 0

    premium1 = re.findall(".+?(?=-)", characs['estimate'])
    try:
        low_estimate_raw = re.findall("\d+", premium1[0])
    except IndexError:
        characs['low_estimate'] = 0
    else:
        characs['low_estimate'] = int("".join(low_estimate_raw))
        print characs['low_estimate']

    premium2 = re.findall("-(.*)", characs['estimate'])
    try:
        high_estimate_raw = re.findall("\d+", premium2[0])
    except IndexError:
        characs['high_estimate'] = 0
    else:
        characs['high_estimate'] = int("".join(high_estimate_raw))
        print characs['high_estimate']

    premium = re.findall("\d+.\d+", characs['Measurements:'])
    try:
        characs['height'] = float(premium[1])
    except IndexError:
        characs['height'] = 0.0
    except ValueError: ## captures exceptions where painting is bigger than 1,000 cm
        a = re.findall(r'\d+\.?', premium[1])
        characs['height'] = float("".join(a))

    print characs['height']

    try:
        characs['width'] = float(premium[3])
    except IndexError:
        characs['width'] = 0.0
        print characs['width']
    except ValueError: ## captures exceptions where painting is bigger than 1,000 cm
        a = re.findall(r'\d+\.?', premium[3])
        characs['width'] = float("".join(a))

    try:
        characs['depth'] = float(premium[5])
    except IndexError:
        characs['depth'] = 0.0
    print characs['depth']

    premium = re.findall("\(([^^]+)\)", characs['lot'])
    try:
        characs['auction_date'] = premium[0]
    except IndexError:
        characs['auction_date'] = 'no date'

    if characs['year'] == '':
        characs['year'] = 0
    
    if characs['price_dollars'] == '':
        characs['price_dollars'] = 0

    if characs['price_original_currency'] == '':
        characs['price_original_currency'] = 0

    if characs['low_estimate'] == '':
        characs['low_estimate'] = 0
    
    if characs['high_estimate'] == '':
        characs['high_estimate'] = 0


    for key in keys2:
        if key in characs:
            characs[key] = characs[key]
        else:
            characs[key] = ""
        #print key 
        #print "wtf man"
        #print characs[key]

    ### replace / with - so it doesn t confuse the saving file location
    characs['title'] = characs['title'].replace("/", "-");
    
    ### retrieving image ans saving it to local file ###

    image_href = soup.find("div", {"class":"artwork-image"})
    try:
        for image in image_href.findAll("img"):
            painting_image = image.get("src")
        #print characs
        painting_name = characs['title'] + "_" + str(characs['year']) + "_" + characs['painter'] + "_" + str(characs['width']*characs['height']) + ".jpg"
        print painting_name
        r = requests.get(painting_image, headers=headers)
        f = open('blouin/media/paintings/%s' % painting_name, 'w')
        f.write(r.content)
        f.close()
        image_found = 'true'
    except AttributeError:
        #print "no painting image"
        image_found = 'false'


    #print characs


### saving to db database in django ###
    
### if Painter is a differen model class use this snippet ###

    # try:
    #     t = Painter.objects.get(name__iexact=characs['painter'])
    # except ObjectDoesNotExist:
    #     t = Painter(name=characs['painter'])
    #     t.save()
    
    #### para no guardar la misma pintura crear un "RFC" por pintura tipo H*W*P*estimates+painter+title
    
    RFC = str(characs['height']) +"-"+ str(characs['width']) + "-" + str(characs['low_estimate']) + str(characs['high_estimate'])+"-"+ characs['auction_date']+"-"+ characs['title'] +"-"+ characs['painter'] +'-' + characs['lot']
    #print RFC 
    rs = ""
    try:
        rs = Painting.objects.get(RFC__iexact = RFC)
    except ObjectDoesNotExist:
        rs = Painting(
        painter = characs['painter'],
        nationality = characs['nationality'],
        price = characs['price'],
        title = characs['title'],
        markings = characs['Markings:'],
        original_currency = characs['original_currency'],
        price_original_currency = characs['price_original_currency'],
        price_dollars = characs['price_dollars'],
        currency = characs['currency'],
        exhibited = characs['Exhibited:'],
        edition = characs['Edition:'],
        condition = characs['Condition:'],
        year = characs['year'],
        estimate = characs['estimate'],
        low_estimate = characs['low_estimate'],
        high_estimate = characs['high_estimate'],
        measurements = characs['Measurements:'],
        url = characs['url'],   
        sizenotes = characs['Size Notes:'],
        provenance = characs['Provenance:'],
        auction_data = characs['auction_data'],
        lot = characs['lot'],
        description = characs['Description:'],      
        literature  = characs['Literature:'],
        materials = characs['Materials:'],
        sale_date = characs['auction_date'],
        premium_hammer = characs['premium'],
        width = characs['width'],
        height = characs['height'],
        depth  = characs['depth'],
        RFC = RFC
        )
        rs.save()
        ### add picture images, only if image was found ###
        if image_found == 'true':
            q = rs.id
            reopen = open('blouin/media/paintings/%s' % painting_name, 'rb')
            django_file = File(reopen)
            image_save = Painting.objects.get(id = q)
            image_save.image1.save(painting_name, django_file, save=True)

    except MultipleObjectsReturned:
        print "already registered"

    


    # You want to set this field to point to an existing image (in a script, or a view, etc.).
    # image_root = '/media/paintings/%s' % painting_name
    # print image_root
    
    # painting_object = Painting_Image(name = painting_name, image1 = image_root)
    # painting_object.save()
    # print painting_object

    # You must use a path relative to the settings.MEDIA_ROOT.
 
    # painting_object.image1 = image_root
    # painting_object.save()
    
    #charac_list.append(characs.copy())
    
    #print ' -------- ***** --------'
    #print charac_list
    return rs


# ### function call ups ###


