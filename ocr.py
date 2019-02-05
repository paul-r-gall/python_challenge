file=open('ocr.txt')
s=''.join(file.read().split())
cDict = {}
for c in s: 
    try:
        cDict[c]+=1
    except KeyError:
        cDict[c]=1
print(cDict)