#Question1,B
Primal_numbers_list= [x for x in range (1,1000)if all(x%i!=0 for i in range(2,x))]
print(Primal_numbers_list)
#first : we created an empty list 
#we used list comprehension to go all over the numbers between 1 and 1000 
#for each number we check if it's primry by using all() function and checking that x is not divisble on any number
#from 1 to 1000
#finally we print the list