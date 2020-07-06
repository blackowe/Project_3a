# Author: Erik Blackowicz
# Date: 7/6/20
# Description: Code asks user for a # of integers(postive # only), then loops thru values to return the min & max values of that dataset.

user_limit = int(input("How many integers would you like to enter?\n")) # Number should be >=1
print("Please enter", user_limit, "integers.")
min_var = int(input())  # initalize min to equal first input value
max_var = min_var       # initalize max = min to start, will change if # integers entered >1

for i in range(1,user_limit):
    user_num = int(input())  # will hold the value temporarily for each pass thru the loop
    if user_num > max_var:
        max_var = user_num
    if user_num < min_var:
        min_var = user_num

print("min:", min_var)
print("max:", max_var)