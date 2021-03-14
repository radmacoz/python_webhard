sentence = '''한 일
1.

배운 것
1.

elapsed time:  hour'''

for i in range(14, 32):
    f = open("./update_log/2103"+str(i)+"_commit", 'w', encoding='utf-8')
    f.write(sentence)
    f.close()