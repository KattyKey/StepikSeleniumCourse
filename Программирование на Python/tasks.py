# Task 1

'''n = int(input())
s = []
for i in range(n):
    s.append( input().split(';'))
d,i={},0
for i in range(len(s)):
    resA, resB, valueA, valueB = int(s[i][1]), int(s[i][3]), [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    if s[i][0] in d:
        valueA =d[s[i][0]]
    if s[i][2] in d:
        valueB =d[s[i][2]]

    if resA ==resB:
        valueA[0]+=1
        valueA[2] += 1
        valueA[4] += 1
        valueB[0] += 1
        valueB[2] += 1
        valueB[4] += 1
    if resA >resB:
        valueA[0]+=1
        valueA[1] += 1
        valueA[4] += 3
        valueB[0] += 1
        valueB[3] += 1

    if resA <resB:
        valueA[0]+=1
        valueA[3] += 1
        valueB[0] += 1
        valueB[1] += 1
        valueB[4] += 3

    d[s[i][0]]=valueA
    d[s[i][2]] = valueB
for q, w in d.items():
    print((q+':'), *w, end='\n')'''
# Task 2
'''def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

tex = list(input())
tra = list(input())
d = {}
for i in range(len(tex)):
    d[tex[i]]=tra[i]
word = list(input())
tran = list(input())
res1, res2 = '',''
for i in range(len(word)):
    res1+=d[word[i]]
print(res1)
for i in range(len(tran)):
    res2+=get_key(d,tran[i])
print(res2)'''
# Task 3
'''seqD =[]
for i in range(int(input())):
    seqD.append(input().strip().lower())

seqR=[]
for i in range(int(input())):
    seqR+=(input().lower().strip().split(" "))
res = []
for i in seqR:
    if i not in seqD:
        if i not in res:
            res.append(i)
for i in res:
    print (i)'''

'''
2
word 
POC
7
word word word word word word word word word word word word word word word word word word word word word 
wold word word
word word wold
word wold word
wold wold wold
poc Poc pOc poC POc pOC PoC POC
POS rOC p0c 
'''

# Task 4
'''d ={}
for i in range(int(input())):
    s = input().split(" ")
    if d.get(s[0])==None:
        d[s[0]] = s[1]
    else:
        value = d.get(s[0])
        d[s[0]] = int(value) + int(s[1])

x,y=0,0
for key,value in d.items():
    if key=="север":
        y+= int(value)
    elif key =="юг":
        y-=int(value)
    elif key =="восток":
        x+=int(value)
    elif key =="запад":
        x-=int(value)
print(str(x)+ " "+str(y))'''
# Task 5
out = open('C:\\Users\\k.novosol\\Downloads\\dataset_3380_5.txt')
s = out.read().strip().split('\n')

d = {}
for i in s:
    t = i.split('\t')
    if d.get(t[0]) == None:
        d[t[0]] = [t[2],1]
    else:
        value = d.get(t[0])
        d[t[0]] = [float(value[0]) + float(t[2]), int(value[1])+1]
for i in range(1,12):
    if d.get(str(i)) == None:
        print(str(i)+ " -")
    else:
        value = d.get(str(i))
        print(str(i) + " "+ str(value[0]/value[1]))
