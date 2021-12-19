# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

"""
So, filter() takes in a function that returns a boolean, and a list. filter() iterates through the list
and applies the function to each item. Items that return true are retained. The filter function returns
a filter object, which must be converted to a list() if you wanna see the list itself.

The map() function has the same idea except the function doesn't have to be boolean. It retains item order. 

But yes, the point of lambdas is that they're anonymous, and can be compactly inserted as arguments to functions
that require other functions for their arguments (like map & filter). 
"""

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: (x%2==0) , my_list))
math_list = list(map(lambda x: (x*2) , my_list))

print(new_list)
print(math_list)
