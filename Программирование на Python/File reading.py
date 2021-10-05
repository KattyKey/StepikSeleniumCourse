
# Task 1

#out = open(r'C:\Users\k.novosol\Downloads\dataset_3363_2.txt')
#s = out.read().strip()
#substr=''
#key=""
#res = ''
#for i in range(len(s)):
#    if s[i].isdigit():
#        substr+=s[i]
#        if i == len(s)-1:
#            res+=key*int(substr)
#    else:
#        if key != "":
#            res+=key*int(substr)
#        key = s[i]
#        substr=""
#into = open(r'C:\Users\k.novosol\Downloads\file2.txt', 'w')
#into.write(res)


# Task 2
'''
out = open('C:\\Users\\k.novosol\\Downloads\\dataset_3363_3.txt')
s = out.read().strip().split(' ')
d = {}
for i in range(len(s)):
    key = s[i].upper()
    if key in d:
        value = d.get(key)
        d[key] = value+1
    else:
        d[key] = int(1)
reskey =''
resval =0
for key,value in d.items():
    if int(value) == resval:
        if key<reskey:
            reskey=key
    elif int(value) > resval:
        reskey=key
        resval=value

res = reskey+' '+str(resval)
into = open(r'C:\\Users\\k.novosol\\Downloads\\file2.txt', 'w')
into.write(res)
'''


# Task 3
out = open('C:\\Users\\k.novosol\\Downloads\\dataset_3363_4.txt')
text = out.read().strip().replace('\n',';')
s =text.split(';')
counter = 0
math = 0
phis = 0
lit = 0
into = open(r'C:\\Users\\k.novosol\\Downloads\\file2.txt', 'a')
for i in range(len(s)):
    if s[i].isalpha():
        counter+=1
        math+=int(s[i+1])
        phis+=int(s[i+2])
        lit+=int(s[i+3])
        res = str((int(s[i+1])+int(s[i+2])+int(s[i+3]))/3)+'\n'
        into.write(res)

into.write(str(math/counter)+" "+str(phis/counter)+" " + str(lit/counter))