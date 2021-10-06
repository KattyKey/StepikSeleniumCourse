import requests
'''
out = open('C:\\Users\\k.novosol\\Downloads\\dataset_3378_2.txt')
t = out.read().strip()
r = requests.get(t)

s = r.text.splitlines()
print(len(s))
'''
r = requests.get(open('C:\\Users\\k.novosol\\Downloads\\dataset_3378_3.txt').read().strip())
i=''
while not i.startswith('We'):
    i= r.text
    r=requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+i)

print (i)