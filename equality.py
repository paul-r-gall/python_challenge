file=open('equality.txt')
s=''.join(file.read().split())

def check(pos, s):
    try:
        return s[pos].islower() and s[pos-3:pos].isupper() and s[pos-4].islower() and s[pos+1:pos+4].isupper() and s[pos+4].islower()
    except IndexError:
        return False
        
for i in range(len(s)):
    if check(i,s):
        print(s[i])



