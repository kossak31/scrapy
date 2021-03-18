## start project
```
scrapy startproject scrapy_spider
```

## generate a file example.py with genspider
```
scrapy genspider example example_domain.com
```


```
├── scrapy.cfg                # deploy configuration file
└── scrapy_spider             # project's Python module, you'll import your code from here
    ├── __init__.py
    ├── items.py              # project items definition file
    ├── middlewares.py        # project middlewares file
    ├── pipelines.py          # project pipeline file
    ├── settings.py           # project settings file
    └── spiders               # a directory where spiders are located
        ├── __init__.py
        └── example.py        # spider we just created
```


## real example
```
scrapy genspider quotes_spider quotes.toscrape.com
```


### start crawl quotes_spider
```
scrapy crawl quotes_spider
```
