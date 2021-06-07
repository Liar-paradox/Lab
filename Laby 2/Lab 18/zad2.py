import linecache

inw = open('pantadeusz.txt','r',encoding='utf-8')

for i,inw in enumerate(inw):
    if i == 7:
        print(linecache.getline('pantadeusz.txt',8))
    elif i == 11:
        print(linecache.getline('pantadeusz.txt', 12))
    elif i == 59:
        print(linecache.getline('pantadeusz.txt', 60))
    elif i == 93:
        print(linecache.getline('pantadeusz.txt', 98))
    elif i == 103:
        print(linecache.getline('pantadeusz.txt', 104))