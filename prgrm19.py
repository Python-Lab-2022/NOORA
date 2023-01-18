list=[10,15,85,88,37]
print("original list:",list)
for i in list:
    if(i%2==0):
       list.remove(i)
print("after removing even numbers:",list)
