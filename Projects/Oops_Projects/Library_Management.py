with open('concepts/file_handling/library.txt','+r') as fp:
    # for i in fp.readlines():
    #     print(i)
    print(fp.seek(0))
    line=fp.read()
    print(line)
    print(fp.tell())