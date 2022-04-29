file=open('sample.txt','r')
st=file.readlines()
mx=0
wrd=""
for line in st:
    lis=line.split()
    for word in lis:
        if(len(word)>mx):
            mx=len(word)
            wrd=word
            
print(wrd)
