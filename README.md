# scrapy
all about scrapy

## install python3 in raspberry pi
```bash
sudo apt install python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

### install scrapy
```bash
sudo pip3 install scrapy
```

### During scrapy installation, some dependencies version errors may aoccurr...
```bash
sudo pip3 install  zope.interface==4.4.2
```

### check version of scrapy
```bash
scrapy version
```

### small example
```bash
wget https://peppe8o.com/download/python/myspider.py
scrapy runspider myspider.py -o peppe8o.json
```


### If you just want a list of urls 1..50, try this
```
urls = ['http://www.example.com/page/' + str(i) for i in range(1, 51)]
```
### change USER-AGENT in settings.py
```
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.>
```
