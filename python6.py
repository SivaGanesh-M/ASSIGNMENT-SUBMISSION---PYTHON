file=open('sample.txt','r')
st=file.readlines()
dict={}
for line in st:
    lis=line.split()
    for word in lis:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for key,val in dict.items():
    print(key+": ",val)
