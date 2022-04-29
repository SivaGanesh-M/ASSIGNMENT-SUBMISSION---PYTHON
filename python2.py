file=open('sample2.txt','r')
res=file.readlines()
n=int(input())
c=0
for i in res:
    if(c==n):
        break
    print(i.strip())
    c+=1
    

