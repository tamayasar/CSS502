from bs4 import BeautifulSoup
import requests

headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding" : "gzip, deflate, zstd",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,tr;q=0.7",
        "Cache-Control" : "max-age=0",
        #"Cookie" : "st=a88e5c381e244461a9dff8d8e81fe4e7eca70dd798c3b2bd4d9ab550824548335c0689ae38c29e6e59c0dc2669b69f745332513c4c5afb41c; vid=539; cdid=T4nEE8UG5tuSm689675ef4a8; csls=sWWN3Rr1M7axQDLJw5X9DTxJvxAFcVLyT0t2YYVcXiviZtJ44j6bdHuHRWOqoUMlsOtTWzJ9_6r1Aqdj1_knhg; MS1=https://www.google.com/; nwsh=std; showPremiumBanner=false; OptanonAlertBoxClosed=2024-12-15T15:24:46.801Z; csss=2woJNSJFO06WPJPrPY5O8MZGlCCK8OfV0n8FSYfKA0VOCKrWkGal1RcKzFXAXdRGbeQHkXRTMSb0O5YQfAA3WQ; __cf_bm=pyUxYhatVqJ_BbM2I7ruZfiKdnM5ueyRPEHwsFwJUUc-1734283040-1.0.1.1-CFp01J2PbPbp.bIT4ZB.TDhuywUU51lwGC7i99J4q9skVBNJTcQ5nZqjbyqOFVwCIN9XYEm.PfVmkTDyvAfSqQ; __cflb=0H28vudCb12J6LVB9qNjWurRvgFyPgDAYwh3S6iJT4o; dp=1920*1080-landscape; geoipCity=istanbul; geoipIsp=turksat; searchType=CATEGORY/TREE/CLASSIC; pfuid=7444ecfb32d34d91aab9289299e15279; csid=7Q7eQXosmi3c5CO6qtHIegEJ9FcZ4d8FfGDfuje_vJPX_UThSaL15GR2fEqLa8mftdhRjdVfd-liPebnJOoMuqrCO_RzzppwTgzhZ8GrmdrJ7Rm2DfCLF3yX5KOk1KMYAnWM5LVKa4iG6tUujxde_esH1Y5g1y_WUYRCI7BX7S8tZkj_jUgRkTrfnq-gpSXLaLrlH2KvtAI-t7eo6BnXHjJ7s2-8ZPp7ynFWeeTgCS0ewc8VJx-seGS3O-gMxRm8nkIU6DvlSGJMvKPNcucT9LUpDAa5KxkLqVWLSk6hkiRiQ-gsGTOsu7pmlvA5slPQIbocUV6VDQt59e920YV5ZJE5yJH4cWVtmXa71S8lDC4wr8Zxf1VDTIG5bGS6FYDW; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Dec+15+2024+20%3A30%3A40+GMT%2B0300+(GMT%2B03%3A00)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&consentId=20fee2c4-42cf-42a3-b7b6-480384c8b718&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0004%3A0%2CC0001%3A1%2CC0003%3A0%2CC0002%3A0&hosts=H183%3A0%2CH106%3A0%2CH8%3A0%2CH67%3A0%2CH14%3A0%2CH114%3A0%2CH184%3A0%2CH87%3A1%2CH4%3A0%2CH5%3A0%2CH185%3A0%2CH17%3A0%2CH64%3A1&genVendors=&AwaitingReconsent=false&intType=2&geolocation=TR%3B34; cf_clearance=ayZJJwPqKh7.mgmWYyQdsZ0A6GvgI8Fg0RFThwhD9PM-1734283841-1.2.1.1-DBDFwU4Sw.30HmldOcI.nA0qyq7UEIqgSSMF11svxv7vodohyS.8dQIZWgfntNizbifflsZh6Cse_TvoHUajiLO0AvPu8NUR58VvhYw08Nbejzqpf0O2q477K1aXP9nrbHuYqJksr6gCW8SG.C1GOBeZEwlilzRsNufNnLHaV03ctWuC0v2Nk.GeEOhTUr4uUw9RLNLss_sKEu6je9cFO7La8GTY3GyYAWGPiSzeZFkBXwzczvmFt7NzdxdP6xi8SLwTCpeS9sTWC2tC7BbfxYRV202q5TrWp6n_Ieb1yEb2mbAbQ7zwh2NbeqJttUgbPIULLyUz4wdu.J7B7pvahZnpoivLUAuflKHQGZpWn4GJJv7ABtnR_xpYvGsAa4iW",
        "Priority" : "u=0, i",
        'Referer': 'http://www.google.com',
        }

# This is to iterate through pages.
offset = 50

# sahibinden.com shows up to 20 pages.
for i in range(20):
    r = requests.get("https://www.sahibinden.com/kiralik-daire/istanbul-uskudar?pagingOffset={}&pagingSize=50&address_region=2".format(i*offset),
                     headers = headers)

    soup = BeautifulSoup(r.text, 'lxml')

    #titles = soup.select("tr.searchResultsItem>td.searchResultsTitleValue.leafContent>a.classifiedTitle")
    prices = soup.select("tr.searchResultsItem>td.searchResultsPriceValue>div.classified-price-container>span")

    #for i in zip(titles, prices):
    #    print(i[0].get_text().strip(), i[1].get_text().strip())
    for i in prices:
        print(i.get_text().strip())
