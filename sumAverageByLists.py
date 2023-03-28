numlist=list()
k=0
print("Enter Number")
while True:
    x=input("Enter Number")
    if x=='done' : break
    value=float(x)
    numlist.append(value)
k=sum(numlist)/len(numlist)
print('AVG= ', k)
  