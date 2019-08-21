#program :- write a program that has a nested list to store toppers details
#edit the details and reprint the details

Toppers=(("arav","bsc",92.0),("Chaitanya","BCA",99.0),
         ("Dhruvika","Btech",97))
for i in Toppers:
    print(i)
choice=input("do you want to edit the details")
if choice == 'y':
    name=input("Enter the name of the student whose details are to be edited")
    new_name=input("enter the correct name")
    new_course=input("enter the correct course")
    new_aggr=input("enter the correct aggregate")
    i=0
    new_Toppers=()
    while i<len(Toppers):
        if Toppers[i][0] == name:
            new_Toppers += (new_name,new_course,new_aggr)
        else:
            new_Toppers += Toppers[i]
        i+1
for i in new_Toppers:
    print(i,end=' ')
