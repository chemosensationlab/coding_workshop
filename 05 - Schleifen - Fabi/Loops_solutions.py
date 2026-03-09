# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:49:10 2026

@author: quicken
"""

"""

# # # # # # # # # # # # # # # 
# # # Solutions loops # # # 
# # # # # # # # # # # # # # # 

"""

"""
General remarks:
In python, there are often multiple solutions. So if your code looks different, 
it might still be working as intendet! 
"""

"""
Exercise 1.1: Battery Display.
You have to code a display, that informs the user about the current battery state.
Create a variable battery_level that starts at 100. While the battery level is
above 0: Reduce it by a fixed amount and print information about the current
battery level. When the battery reaches 0, print “System shutting down.”

Bonus: Add a low battery warning, that appears at a battery_level <= 20.
 
Learning Goals:
- Using while keyword
- Conditional statement logic repetition
- "Counter" logic in while loops
"""

battery_level = 100

while battery_level > 0:
    battery_level -= 3
    
    if 0 < battery_level <= 20:
        print("Warning: Battery low.")
    
    # kleiner Check, damit battery_level nicht negativ wird
    if battery_level < 0:
        battery_level = 0
        print(f"Battery level: {battery_level}%. System shutting down.")
        
    else:   
        print(f"Battery level: {battery_level}%")
    
    


"""
Exercise 1.2: Counting Sheep.
You lie in your bed and think about your experiments. But at 7 a.m. you have to
get up to enjoy the breakfast with your dear colleagues. So, you start to count
sheep until you fall asleep. Convert this into python logic: Create a variable
“sheep_count” and a while loop, that runs under a “is_awake” condition. Each
run of the loop increases the sheep_count by one and prints the current count,
until a specific number is reached, which sets the “is_awake” condition to False.
Be careful not to build an endless loop, or you will never fall asleep!

Bonus: When falling asleep, print this information.

Learning Goals:
- Using while keyword repetition
- flag logic in while loops
"""

sheep_count = 0
# this variable is called a "flag", since we use it to control our while loop
is_awake = True

while is_awake:
    sheep_count += 1
    
    if sheep_count <= 42:
        print(f"{sheep_count} sheep...")
    else:
        # if a specific condition is met, the flag is set to False to exit the loop
        is_awake = False
        # bonus: we give the feedback of exiting the loop at the time we set the flag to False
        print("zzzZZZZzzzz")
    
    
    
    
"""
Exercise 1.3: Guess the number.
Start your code with

import random
random_number = random.randint(1,10)

to generate a random integer between 1 & 10. 
Using a while loop, ask the user for input to guess the correct number.
Give a hint whether the guess is too high or too low and end the loop with a
printed “Correct!”, when the number is guessed.

Learning Goals:
- Using extern functions
- repetition of if and else
- more complex while loops
"""

import random
random_number = random.randint(1,10)

# int() to typecast the string input into an integer
# otherwise you will run into an endless loop!
user_input = int(input("Guess a number between 1-10: "))
while user_input != random_number:
    
    # Giving a hint and asking for new input, as long the number is not guessed correctly
    if user_input > random_number:
        user_input = int(input("Too high. Guess again: "))
    else:
        user_input = int(input("Too low. Guess again: "))

# when exiting the while loop, giving feedback on guessing the number correctly
print("Correct! U so smart!")




"""
Exercise 2.1: Shopping
.
1.	Create a list, that you fill with items you want to buy in the grocery store.
Now create an empty “grocery_cart” list. Use a for loop, to move all items to
the grocery_cart, one after another. 
2.	 Test what happens, when you use the .remove() function to remove each
product when it is put into the grocery_cart.
3.	Use the range function, to run the for loop a set amount. Find a solution,
to append each item to the grocery_cart while also emptying the shopping_list.
(Hint: You might want to use the .pop() function).

Learning Goals:
- For ... in keyword
- changing iterables while looping over them is dangerous!
- understanding the range() function
"""

grocery_list = ["apple", "bread", "banana", "chocolate"]
shopping_cart = []

# this adds every item to the shopping_cart list, without changing the grocery_list
for item in grocery_list:
    shopping_cart.append(item)
print(shopping_cart)

# lets do this again but remove all the items from the grocery_list
grocery_list = ["apple", "bread", "banana", "chocolate"]
shopping_cart = []
for item in grocery_list:
    shopping_cart.append(item)
    grocery_list.remove(item)
print(shopping_cart)
# you will see, that as the list gets shorter, the for loop will "skip" items
# this is because once removing "apple" at index [0], each item in the list moves
# forward, so "bread" would be at grocery_list[0]. Since the for loop already
# worked on the item at position [0], it moves on to the item at position [1], 
# which is now "banana", not "bread".

# how to solve this?
# if we iterate backwards, the indices of items in front won't change!
grocery_list = ["apple", "bread", "banana", "chocolate"]
shopping_cart = []
# we can set the start of the range at the last index with len(list)-1
# since the "stop" is exclusive, we set it to -1 to stop at 0
# we have to set the stepsize to -1, since we are stepping backwards!
for i in range(len(grocery_list)-1, -1, -1):
    shopping_cart.append(grocery_list[i])
    # with -pop(), we remove items in a list based on the index
    # so we always remove the last item
    grocery_list.pop(-1)

print(shopping_cart)
print(grocery_list)

# to do this a bit less complicated, you could use the reverse() function as well.
grocery_list = ["apple", "bread", "banana", "chocolate"]
shopping_cart = []
for item in reversed(grocery_list):
    shopping_cart.append(item)
    grocery_list.pop(-1)

print(shopping_cart)
print(grocery_list)




"""
Exercise 2.2: Leaderboard
1.	Create a list of integers with values between 1-99. Use the sorted()
function of python to sort the values in descending order (sorted(list, reverse=True)).
Use the range() function to build a for loop.
2.	Now use the enumerate() function to build the for loop and compare –
which version is easier to read? Or less error prone?

Learning Goals:
- enumerate function
- readibility in python
"""

x = [4, 88, 6, 12, 18, 15, 14, 9, 22, 54]

# alternative list of random ints:
x = []
for i in range(10):
    x.append(random.randint(1, 99))

x = sorted(x, reverse=True)

for i in range(len(x)):
    print(f"Place {i+1}: {x[i]} points")
    
for i, score in enumerate(x):
    print(f"Place {i+1}: {score} points.")
    
    
    
    
"""
Exercise 2.3: Rating students
1.	You corrected some student protocols in the animal physiology course and noted,
how many mistakes they had in the following dictionary (names are fictious):
corrected = {
    "Hannah": 3,
    "Fabi": 0,
    "Johanna": 4,
    "Yuliia": 2,
    "Moritz": 3,
    "Ilian": 6,
    "Christopher": 10,
    "Christoph": 1,
    "Lena": 2
}
You don’t care how many mistakes a student has, just if they passed or not.
Therefore, you want to set each number >= 3 to False (for has not passed) and
everyone else to True.

2.	You also have a list with all students, that need to be corrected:
submitted = [
    "Hannah", # handed in first
    "Fabi",
    "Kevin",
    "Johanna",
    "Yuliia",
    "David",
    "Moritz",
    "Ilian",
    "Leonie",
    "Christopher",
    "Christoph",
    "Simon",
    "Lena" # handed in last
] 
The list also shows the order, in which people handed in their submission. In
your moodle, each submission has its own page, related to the time of submission
in relation to the other students. Test, whether the submitted student was already
corrected by you and only apply the pass/not passed logic to those students.
Find all students and the respective pages in your moodle that you still have to
correct. You should start correcting people, that handed in earlier, since you are
running close to their correction deadline. 
(Hint: Use the keyword “in” to write a conditional statement, testing if a
 submitted student is already corrected.)


Learning Goals:
- combining for loops and if ... else
"""

# first part
corrected = {
    "Hannah": 3,
    "Fabi": 0,
    "Johanna": 4,
    "Yuliia": 2,
    "Moritz": 3,
    "Ilian": 6,
    "Christopher": 10,
    "Christoph": 1,
    "Lena": 2
}

for student in corrected:
        if corrected[student] >= 3:
            corrected[student] = False
        else:
            corrected[student] = True
   
# second part
corrected = {
    "Hannah": 3,
    "Fabi": 0,
    "Johanna": 4,
    "Yuliia": 2,
    "Moritz": 3,
    "Ilian": 6,
    "Christopher": 10,
    "Christoph": 1,
    "Lena": 2
}

submitted = [
    "Hannah", # handed in first
    "Fabi",
    "Kevin",
    "Johanna",
    "Yuliia",
    "David",
    "Moritz",
    "Ilian",
    "Leonie",
    "Christopher",
    "Christoph",
    "Simon",
    "Lena" # handed in last
] 

for i, student in enumerate(submitted):
    # apply pass / no pass logic to corrected students
    if student in corrected:
        if corrected[student] >= 3:
            corrected[student] = False
        else:
           corrected[student] = True
           
    else:
        # if not corrected, print the info on where to correct the student
        print(f"Correct the student {student} on moodle page {i+1}")
        

    

