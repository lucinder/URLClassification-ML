import csv, random, sys
random.seed()
src = sys.argv[1]
dst = sys.argv[2]
b0, m0 = [], []
benign, malicious = [], []
bCount, mCount = 0, 0
isMal = {"benign":False,"phishing":True,"defacement":True,"malware":True}
with open(src+".csv", encoding='utf-8') as csvfile:
    print("Reading source data.")
    reader = csv.reader(csvfile, delimiter=",",quotechar="\"")
    next(reader)
    for row in reader: # construct our initial lists
        mal = isMal[row[1]]
        if(mal):
            m0.append([row[0],mal])
        else:
            b0.append([row[0],mal])
while(bCount <= 60000): # randomly select 60000 benign items
    toAdd = b0.pop(random.randint(0,len(b0)-1))
    print(str(bCount) + " - Adding " + str(toAdd) + " to benign.")
    benign.append(toAdd)
    bCount += 1
while(mCount <= 40000): # randomly select 40000 malicious items
    toAdd = m0.pop(random.randint(0,len(m0)-1))
    print(str(mCount) + " - Adding " + str(toAdd) + " to malicious.")
    malicious.append(toAdd)
    mCount += 1
# build our final list
combined = benign + malicious
final = []
while(len(combined) > 0):
    final.append(combined.pop(random.randint(0,len(combined)-1))) # pop randomly from our combined lists
# write to destination csv
with open(dst+".csv",'w',newline='',encoding='utf-8') as dstfile:
    print("Writing to destination file.")
    writer = csv.writer(dstfile, delimiter=",",quotechar="\"")
    for i in final:
        writer.writerow(i)