#programm to manipulate efficiently each value that is passed to the tuple
#using variable length argument

def display(*args):
    print(args)
Tup=(1,2,3,4,5,6)
Tup1=(7,8,9,10,11,12)
display(Tup,Tup1)

#agr krke aap kitna bhi variablepass kr skte hai

#NOTE :- if youhave a function that displays all the parameters passed to it,
#then even the function does not know how many value it will be passed.in such cases
#we use a variable-length argument that begains with a'*' symbolis know as gather
#and specifies a variable length argument.
