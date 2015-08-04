### print to csv function ### 

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
'painter', 
'nationality', 
'title', 
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
'nationality'
]

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
            q.painter, 
            q.nationality, 
            q.title, 
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
            q.nationality,
            ])
            i += 1
        except ObjectDoesNotExist:
            i += 1

    
    return response