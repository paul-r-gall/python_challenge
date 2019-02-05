from PIL import Image
import numpy as np

image=None
try:
    image = Image.open('oxygen.png')
except IOError:
    pass
pix_arr = np.asarray(image)
print(len(pix_arr[0]))
mid = len(pix_arr)//2
print(mid)
print(pix_arr[mid])
s=''
for i in range(629//7):
    s+=chr(list(pix_arr[mid][7*i])[0])
print(s)

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
l1=[chr(x) for x in l]
print(l1)