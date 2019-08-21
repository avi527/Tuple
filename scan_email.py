addr='avinash@gmial.com'
user_name,domain_name=(addr.split('@'))
print("user name =",user_name)
print("domain name =",domain_name)

#write a program that has a list of number (both positive as well as negative)
#make a new tuple that has only positive values from this list

Tup=(-10,1,2,-9,3,4,-8,5,6)
newtup=()
for i in Tup:
    if i>0:
        newtup +=(i,)
print(newtup)
