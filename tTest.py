import math
d={}
n = int(input("Enter no of words"))
for i in range(n):
    s= input("Enter name of the string")
    c= int(input("Enter frequency"))
    d[s]=c
total = int(input("Enter total no of words"))
s = input("Enter the word you want to search collocation for ")
x=d[s]/total
l= s.split(" ")
s1=l[0]
s2=l[1]
mew = (d[s1]/total)*(d[s2]/total)
t=(x-mew)/math.sqrt(x/total)
print(" t = "+str(t))
if t>2.576:
    print(s+" forms a collocation")
else:
    print(s+" does not form a collocation")
