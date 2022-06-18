#write a python function that takes one argument as a list a=[2,4,6,8] and remove the second last item from that
#list and returns the whole list without the removed item

def numbers(a):
    a=[2,4,6,8]
    a.pop(2)
    return a
numbers([2,4,6,8])   

#write a python program that has a list days=['monday','tuesday','friday','monday']and counts the number occurence of monday
days=['monday','tuesday','friday','monday'] 
c=days.count('monday')
print(c)

#Write a python function named smallest that accepts a lst of unsorted integers and returns the smallest
#number in the list.Example a. smallest([3,6,8,2,4,1,5,7])return 1

def smallest(a):
    a.sort()
    print(a[0])
    return smallest
smallest([3,6,8,2,4,1,5,7])    

#write a function named divisible_by+seven that; using the range function an a for loop returns a list containg all the numbers between 100 and 200 that
#are divisible by 7
def divisible_by_seven():
    a= range(100,200)
    for i in a:
        if i%7==0:
            print(i) 
divisible_by_seven 

#Write a python program that take two inputs(as integers )from a user and adds the 2 numbers, checks if the
#the sum is greater than 10,less than 10 or equal 10 and prints a statement after each check

a=int(input("Enter number:"))
b=int(input("Enter number2:"))
c=a+b
if c<10:
    print("the number is less than 10")
if c>10:
    print("the number is greater than 10")
if c==10:
    print("the number is equals to 10")  
    
#Write a function that takes one argument which is a list, a=[1,2,3,4,5]
#and returns True if 4 is present in the list and False is 4 is not in the list

def check(a):
    if 4 in a:
     print( True)
    else:
     print (False)
check([1,2,3,4,5])     

#Write a function that takes one argument whih is a list Fruits=["grapes","apples","pineapple"] and 
# removes the last fruit from the list then returns the list without removed fruit   
def fruit(Fruits):
    Fruits=["grapes","apples","pineapple"] 
    Fruits.pop() 
    return Fruits  
fruit(["grapes","apples","pineapple"] )    

#write a python program thattakes in a list of cars, cars=["Ford","BMW","Volvo"] and returns a sorted list

def car():
    Cars=["Ford","BMW","Volvo"] 
    Cars.sort()
    return Cars
car()        