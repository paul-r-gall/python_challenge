import pickle

banner = pickle.load(open('banner_unix.p','rb'))
for l in banner: 
    print(''.join(tup[0]*tup[1] for tup in l))