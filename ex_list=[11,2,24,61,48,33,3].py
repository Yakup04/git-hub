ex_list=[11,2,24,61,48,33,3]
evens=[]
odds=[]
count=0
oddsi=0
evensi=0
for i in ex_list:
    if count< len(ex_list):
        if i%2==0 :
            evens.append(i)
            count+=1
            evensi+=1
        else:
            odds.append(i) 
            count+=1
            oddsi+=1
print(evens,evensi)
print(odds,oddsi)               