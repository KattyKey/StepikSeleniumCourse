# put your python code here
n=int(input())
counter = n
back = 0
numb =1
a = [[0 for j in range(n)] for i in range(n)]
i = 0
j = 0
while numb <=n**2:
    while j < counter:
       a[i][j]=numb
       numb+=1
       j+=1
    counter -=1
    j-=1
    i=n-counter
    # Спуск по и вниз
    while i <=counter:
        a[i][j]=numb
        numb+=1
        i+=1
    #counter -=1
    i-=1
    j=counter-1
    # Обратная джей
    while j >=back:
        a[i][j]=numb
        numb+=1
        j-=1

    j+=1
    i=counter-1
    back+=1
    while i >=back:
        a[i][j]=numb
        numb+=1
        i-=1
    #counter -=1
    i+=1
    j=back

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

