import linecache

try:
    file1 = open('text1.txt', 'r', encoding='utf-8')
    file2 = open('text2.txt', 'r', encoding='utf-8')
    with open('merge_text.txt', 'w',) as file3:
        for i,(file1,file2) in enumerate(zip(file1,file2)):
            file3.writelines(linecache.getline('text1.txt',i))
            file3.writelines(linecache.getline('text2.txt',i))
            print(linecache.getline('text1.txt',i))
            print(linecache.getline('text2.txt',i))
except:
    print('Pliki nie istnieją')