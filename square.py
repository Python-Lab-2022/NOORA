list=[1,2,3,4,5,6]
for i in list:
    print(i)

squared = [ ]

for i in list:
    sqr = i * i
    squared.append(sqr)
    print("The square of {} is {}".format(i, sqr))
