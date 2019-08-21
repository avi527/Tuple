#we have already studied list comprehension  to create a new list in the
#earlier sections of this chapter.you can use the same concept to manipulate the
#values in one tuple to create a new tuple.

#question :- consider the program given below passes a tuple as an argument
# to a function
#double().the function scales each value in the tuple by a factor of two and places the scaled valuesin another tuples

def double(T):
    return ([i*2 for i in T])
tup=1,2,3,4,5
print("original tuple :",tup)
print("double values:",double(tup))
