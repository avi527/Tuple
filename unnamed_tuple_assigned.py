#an unnamed tuple of values assigned to vaalues of another unnamed tuple
(val1,val2,val3)=(1,2,3)
print(val1,val2,val3)

tup1=(100,200,300)
(val1,val2,val3)=tup1
print(tup1)
print(val1,val2,val3)

#program to return the highest as well as the lowest value in the list

def max_min(vals):
    x=max(vals)
    y=min(vals)
    return (x,y)
vals=(99,98,90,97,89,86,93,82)
(max_marks,min_marks)=max_min(vals)
print("Height Marks =",max_marks)
print("Lowest Marks = ",min_marks)

#2nd minimum maximum example
def minimum_maximum(value):
    a=min(value)
    b=max(value)
    return a,b
value=(20,30,40,60,70,90,500,600,300,900,1002)
(minnimu_marks,maximum_mark)=minimum_maximum(value)
print(f"minimum number {minnimu_marks}")
print(f"maximum number {maximum_mark}")

#note :- you can't delete elements from a tuple.Method like remove()
#or pop() do not work with a tuple

#unlike lists,tuples do not support remove(),pop(),append(),sort(),reverse()
# and insert() methods.
