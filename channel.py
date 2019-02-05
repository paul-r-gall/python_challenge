import zipfile


base = 'channel/'
default = 'Next nothing is '
zf = zipfile.ZipFile('channel.zip','r')
name = '90052.txt'
filename = base+name

def stripS(s):
    if len(s)==4:
        return s[2]
    if len(s)==5:
        return '\n'
final = ""
while True:
    f = open(filename,'r')
    s = f.read()
    if s[:len(default)]==default:
        newNum = s[len(default):]
        #print(newNum)
        filename = base + newNum + '.txt'
        name = newNum+'.txt'
        final+=stripS(str(zf.getinfo(name).comment))
        #print(str(zf.getinfo(name).comment))
        
    else:
        print(s)
        break
print(final)
