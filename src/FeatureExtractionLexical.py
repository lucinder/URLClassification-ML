import csv, re, sys, statistics
src = sys.argv[1]
print(src)
dst = sys.argv[2]
converted = []
shorteners = [""]
DEBUG = sys.argv[3] if (len(sys.argv) > 3) else 0
CUTOFF_DEBUG = 200
with open(src+".csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",",quotechar="\"")
    next(reader)
    i = 1
    for row in reader:
        url = row[0]
        print("Reading line " + str(i)+" - " + url)
        cur = {"url":url,"malicious":row[1]} # get url and type base features
        # print("Malicious? " + row[1])

        # lexical feature extraction
        # untokenized url length
        url_length = len(url)
        cur["length"] = url_length

        # tokenize url
        tokenized = re.split(r'(https|http|://|www|\.|\/|[\(A-Za-z0-9%\'\~\)]+|\/[^\/]*)|\\|\+|\-|\=|\&|\;|\?|_',url)
        tokenized = [tk for tk in tokenized if tk] # remove whitespace
        # print(tokenized)

        # split domain and path
        protocol = "N/A"
        domain = []
        path = []
        if "/" in tokenized:
            domain = tokenized[0:tokenized.index('/')]
            path = tokenized[tokenized.index('/')+1:]
        else:
            domain = tokenized
        if(tokenized[1] == "://"): # handle protocols
            protocol = tokenized[0:tokenized.index("://")][0]
            if "/" in tokenized:
                domain = tokenized[tokenized.index("://")+1:tokenized.index('/')]
            else:
                domain = tokenized[tokenized.index("://")+1:]
        if("www" in domain and domain[domain.index("www") + 1] == "."): # handle subdomain
            # print("Clearing a subdomain!")
            domain = domain[domain.index(".")+1:]

        # check file extension flag
        hasExtension = (len(path) > 1 and path[len(path)-2] == '.')
        cur["extension"] = hasExtension
        # print("Has file extension? " + str(hasExtension))

        # remove special tokens
        domain = [tk for tk in domain if tk != '.']
        path = [tk for tk in path if tk != '.']
        domain = [tk for tk in domain if tk != '/']
        path = [tk for tk in path if tk != '/']
        domain = [tk for tk in domain if tk != '\'']
        path = [tk for tk in path if tk != '\'']
        # print("Protocol: " +protocol+"; Domain: " + str(domain) + "; Path: " + str(path))

        # get TLD and hostname
        hostname = domain[0]
        TLD = domain[len(domain) - 1]
        cur["hostname"] = hostname
        cur["tld"] = TLD
        # print("Hostname: " + hostname + "; TLD: " + TLD)

        # check for common url shortners
        shorteners = [["bit","ly"],["ow","ly"],["t","co"],["tinyurl","com"],["tiny","cc"],["bit","do"],["cutt","ly"]]
        shortened = False
        for s in shorteners:
            if (domain == s):
                shortened = True
        cur["isShortened"] = shortened
        # print("Is shortened? " + str(shortened))
        
        # get token counts
        domainTokenCount = len(domain)
        pathTokenCount = len(path)
        # print("Domain Token Count: " + str(domainTokenCount)+ "; Path Token Count: " + str(pathTokenCount))

        # get token length means, stddevs, maxes
        dLens = [len(tk) for tk in domain]
        pLens = [len(tk) for tk in path]
        dLenAvg = statistics.fmean(dLens) if len(dLens) > 0 else 0
        pLenAvg = statistics.fmean(pLens) if len(pLens) > 0 else 0
        # print("Domain Avg Token Length: " + str(dLenAvg)+ "; Path Avg Token Length: " + str(pLenAvg))
        dLenStdev = statistics.stdev(dLens) if len(dLens) > 1 else 0
        pLenStdev = statistics.stdev(pLens) if len(pLens) > 1 else 0
        # print("Domain Token Length Stdev: " + str(dLenStdev)+ "; Path Token Length Stdev: " + str(pLenStdev))
        dLenLongest = max(dLens) if len(dLens) > 0 else 0
        pLenLongest = max(pLens) if len(pLens) > 0 else 0
        # print("Longest domain token length: " + str(dLenLongest) +"; Longest path token length: " + str(pLenLongest))

        # assign fields
        cur["domainTokenCount"] = domainTokenCount
        cur["domainTokenLengthAvg"] = dLenAvg
        cur["domainTokenLengthStdev"] = dLenStdev
        cur["domainTokenLengthMax"] = dLenLongest
        cur["pathTokenCount"] = pathTokenCount
        cur["pathTokenLengthAvg"] = pLenAvg
        cur["pathTokenLengthStdev"] = pLenStdev
        cur["pathTokenLengthMax"] = pLenLongest

        # add to our new list
        # print(cur + "\n")
        converted.append(cur)
        i += 1
        if(DEBUG == 1 and i == CUTOFF_DEBUG):
            break
metrics = ['url','malicious','length','extension','hostname','tld','isShortened','domainTokenCount','domainTokenLengthAvg','domainTokenLengthStdev','domainTokenLengthMax','pathTokenCount','pathTokenLengthAvg','pathTokenLengthStdev','pathTokenLengthMax']
with open(dst+".csv",'w',newline='',encoding='utf-8') as dstfile:
    print("Writing to file!")
    writer = csv.DictWriter(dstfile, fieldnames=metrics)
    writer.writeheader()
    writer.writerows(converted)