#Code that I either gave up on or think is trash and should not be read by another human beeing
#but still won't delete for some god damn reason...


n=1.25792
p=3
print(n)
m=n*(10**p)
print(m)

m=str(m)

temp = m[p]
if int(temp) > 5:
    temp=m[p-1]
    #why can I not do int(temp)+=1 :?
    temp2=int(temp)
    temp2+=1
    temp=str(temp2)
    
    m[p-1]=temp

print(m)