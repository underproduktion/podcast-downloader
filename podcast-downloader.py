import feedparser
import requests
import time
PodFeed = feedparser.parse("INSERT FEED HERE")

for post in PodFeed.entries:
    print("Downloading "+post.title)
    datum = time.strftime("%y%m%d", post.published_parsed)
    abvtitle = post.title
    abvtitle = abvtitle.replace(" ", "_")
    abvtitle = abvtitle.replace("/", "_")
    abvtitle = abvtitle.replace(",", "_")
    abvtitle = abvtitle.replace(".", "_")
    abvtitle = abvtitle.replace("#", "")
    abvtitle = abvtitle.replace(":", "")
    abvtitle = abvtitle.replace("!", "")
    abvtitle = abvtitle.replace("å", "a")
    abvtitle = abvtitle.replace("ä", "a")
    abvtitle = abvtitle.replace("ö", "o")
    abvtitle = abvtitle.replace("Å", "A")
    abvtitle = abvtitle.replace("Ä", "A")
    abvtitle = abvtitle.replace("Ö", "O")
    abvtitle = abvtitle.replace("–", "")
    abvtitle = abvtitle.replace("-", "")
    abvtitle = abvtitle.replace('"', '')
    filnamn = datum+"_"+abvtitle+".mp3"
    print("Filename: "+filnamn+"\n")
    url = post.enclosures[0].href
    r = requests.get(url, allow_redirects=True)
    open(filnamn, 'wb').write(r.content)
