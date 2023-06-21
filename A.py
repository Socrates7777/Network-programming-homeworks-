#Homework 1
#Question 1 - A
L1=['HTTP','HTTPS','FTP','DNS'] #creating first list
L2=[80,443,20,53]#creating second list
d={}#creating an empty dict
for k in L1:#loop for putting L1 as keys and L2 as values
    for v in L2:
        d[k]=v
        L2.remove(v)
        break
print(d)#final result