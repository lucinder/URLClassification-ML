import requests, sys, re, csv
from bs4 import BeautifulSoup as BS

src = sys.argv[1]
print(src)
dst = sys.argv[2]
DEBUG = sys.argv[3] if (len(sys.argv) > 3) else 0
CUTOFF_DEBUG = 200
converted = []

with open(src+".csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",",quotechar="\"")
    next(reader)
    i = 1
    for row in reader:
        url = row[0]
        print("Reading line " + str(i)+" - " + url)
        cur = {"url":+url,"lineCount":-1,"iframeCount":-1,"hyperlinkCount":-1}
        r = requests.get(url)
        if r.status_code != 200:
            converted.append(cur)
            continue
        soup = BS(r.content,'html.parser')
        lc = len(re.findall("\n",soup.prettify()))
        cur["lineCount"] = lc
        hrefs = soup.find_all('a')
        hrefs = [link for link in hrefs if link != ""]
        cur["hyperlinkCount"] = len(hrefs)
        iframes = soup.find_all('iframe')
        cur["iframeCount"] = len(iframes)
        converted.append(cur)
failed = [x["url"] for x in converted if x["lineCount"] == -1]
if(len(failed) > 0):
    print("Number of failed requests: " + len(failed))
    print("Failed Requests:" + (("\n"+x) for x in failed))
else:
    print("All requests succeded!")