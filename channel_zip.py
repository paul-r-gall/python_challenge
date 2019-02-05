import zipfile

with zipfile.ZipFile('channel.zip', 'r') as f:
    print(f.comment)
    files = f.infolist()
    for z in files:
        print(z.comment)