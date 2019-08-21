#zip() is a built-in function that takes two or more sequence and "zips"
#them into alist of tuple thus,formed has one elements from each sequence
#the code given below illustrates this concept

#question:- program to show the use of zip() function

Tup=(1,2,3,4,5,6)
List1=['ad','bfh','cgdd','dfgf','efgr','gfgf']
print(list((zip(Tup,List1))))
