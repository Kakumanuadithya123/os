n=int(input("enter the process"))
at=[]
bt=[]
for i in range(n):
    a=int(input("arrival time"))
    b=int(input("burst time"))
    at.append(a)
    bt.append(b)
print("at",at)
print("bt",bt)
ct=[]
k=at[0]+bt[0]
x=0
for i in range(n):
    if i==1:
        x=k+bt[i]
    else:
        x=x+bt[i]
    ct.append(x)
print("ct",ct)
tat=[]
for i in range(n):
    tat.append(ct[i]-at[i])
print("tat",tat)
wt=[]
for i in range(n):
    wt.append(tat[i]-bt[i])
print("wt",wt)
s=0
for i in range(n):
    s=s+tat[i]
    atat=s/n
print("atat",atat)
s1=0
for i in range(n):
    s1=s1+wt[i]
    awt=s1/n
print("awt",awt)
