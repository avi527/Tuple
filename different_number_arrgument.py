#write a program that accepts different number of argument and return sum
#of only the positive values passed to it.

def sum(*arg):
    tot=0
    for i in arg:
        if i>0:
            tot +=i
    return tot
print(sum(1,2,3,-4,-5,9))
