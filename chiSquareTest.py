print("Enter the two words")
s1=input()
s2=input()
print("Enter matrix values in row major order")
freq=[]
for i in range(4):
    freq.append(int(input()))
total=sum(freq)
expFreq=[0,0,0,0]
expFreq[0]=((freq[0]+freq[1])/total)*(freq[0]+freq[2])
expFreq[1]=((freq[1]+freq[0])/total)*(freq[1]+freq[3])
expFreq[2]=((freq[2]+freq[3])/total)*(freq[0]+freq[2])
expFreq[3]=((freq[3]+freq[2])/total)*(freq[3]+freq[1])
print(expFreq)
chiSquare=0
l=[]
for i in range(4):
    l.append((freq[i]-expFreq[i])**2/expFreq[i])
chiSquare=sum(l)
print("Chi Square : "+str(chiSquare))
if chiSquare>2.576:
    print(s1+" "+s2+" forms a collocation")
else:
    print(s1+" "+s2+" does not form a collocation")
