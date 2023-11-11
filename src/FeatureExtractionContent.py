import requests, sys, re, csv, urllib3
from datetime import datetime,timedelta
from bs4 import BeautifulSoup as BS

src = sys.argv[1]
print(src)
dst = sys.argv[2]
DEBUG = sys.argv[3] if (len(sys.argv) > 3) else 0
CUTOFF_DEBUG = 200
converted = []
t0 = datetime.now()
with open(src+".csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",",quotechar="\"")
    next(reader)
    i = 1
    for row in reader:
        tn = (datetime.now()-t0)
        tn = tn-timedelta(microseconds=tn.microseconds)
        url = row[0]
        print("("+str(tn)+") >> Reading line " + str(i)+" - " + url)
        cur = {"url":url,"lineCount":-1,"iframeCount":-1,"hyperlinkCount":-1}
        try:
            r = requests.get(url)
        except (requests.exceptions.MissingSchema,requests.exceptions.InvalidSchema,requests.exceptions.SSLError,urllib3.exceptions.MaxRetryError):
            url = "https://"+url
            r = requests.get(url)
        except requests.ConnectionError:
            converted.append(cur)
            print("Line read failed with Connection Error.")
            i += 1
            continue
        if r.status_code != 200:
            print("Line read failed with status code " + str(r.status_code))
            i += 1
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
        i += 1
failed = [x["url"] for x in converted if x["lineCount"] == -1]
if(len(failed) > 0):
    print("Number of failed requests: " + len(failed))
    print("Failed Requests:" + (("\n"+x) for x in failed))
else:
    print("All requests succeded!")