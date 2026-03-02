# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:14:04 2026

@author: quicken
"""

# # # # # # # # # # # # # # # 
# # # Solutions if else # # # 
# # # # # # # # # # # # # # # 

"""
General remarks:
In python, there are often multiple solutions. So if your code looks different, 
it might still be working as intendet! 
"""

"""
Exercise 1: Plant Waterer.
You build a little sensor, that measures the soil moisture level, which is
stored in the variable “moisture” as an integer. If the moisture level is lower
than 30%, it should send a message telling the user to water the plant. If the
level is above the minimum, it should inform the user about the current level.
 
Learning Goals:
- Using if and else keywords
- Conditional statement logic
- f-string logic
"""

moisture = 40

if moisture < 30:
    print("Moisture low, please water me!")
else:
    print(f"Current moisture: {moisture}")
    
"""
Exercise 2: Teacher
You are a teacher and you have to grade the exams of 200 students.
Since it’s very annoying to grade every single exam, you want to write python
code to automatize this. 
Create a small script that starts with a variable “point_score” and set it to
an integer between 0 and 100. Depending on the point_score and the following
table, a print message should appear that shows the respective grade.
Scored Points	>89 >79	>69	>59	<60
Grade (Letter)	 A	 B	 C	 D	 F

Learning Goals:
- including elif in if...else statements.
- prioritization of conditions
"""

# the random module contains the randint function, to generate a random integer
# in a given range. Feel free to set point_score to an int manually aswell
# it is generally helpful for using random inputs to test your code!
import random
point_score = random.randint(0, 100)

if point_score > 89:
    print("Grade A")
elif point_score > 79:
    print("Grade B")
elif point_score > 69:
    print("Grade C")
elif point_score > 59:
    print("Grade D")
else:
    print("Grade F")
    
"""
Exercise 3: Coffee?
You want your coffee machine to write a little message on its screen, once a
lab member presses the button for a specific coffee recipe. Utilizing the
input() function, you can ask for user input in the console. 

choice = input(“What coffee do you desire, master? I serve americano, cappuccino, expresso”)

Depending on the user input, the coffee machine should print a little creative 
message to the customer.

Learning Goals:
- Repeating if/elif/else
- Using the console to input variables
"""

# Tip: .lower() saves you for different capitalizations during input, since everything will be lower case
choice = input("What coffee do you desire, master? I serve americano, cappuccino, espresso").lower()

if choice == "americano":
    print("Enjoy your diluted espresso, you weirdo.")
elif choice == "cappuccino":
    print("Great choice. Enjoy your cappuccino!")
# else would also work, but since we want the input to be exactly "espresso", we should check for that with elif
elif choice == "espresso":
    print("Fast and effective: Espresso in progress.")
# optional:
else:
    print("No valid input.")

"""
Exercise 4: Login System:
Use the input function to ask the user for a username and a password. Then check
if the username AND password are the correct login (user: chemosensorik, password:
cake) and print either “Login successful.” Or “Wrong username or password.” 
Bonus 1: If either password or username is wrong, print this information, so
the user knows where a possible typo occurred. 
Bonus 2: If the password is wrong, print a small message, that helps
the user to remember the password.

Learning Goals:
- 'and' keyword in conditional statements
- ''
"""    
password_input = input("Password:")
username_input = input("Username:")

password = "cake"
username = "chemosensorik"

# both have to be correct
if password_input == password and username_input == username:
    print("Login successful.")
# if password is wrong, give a hint
elif password_input != password:
    print("Wrong password. Hint: What do you have to bring on your birthday?")
# finally give info, wether username is wrong
else:
    print("Wrong username.")

"""
Exercise 5: Lab Access
All keys and locks are broken, so RWTH decided to use keycards to enter the
building and labs. Since this requires a lot of programming, each group has
to program rules for entering their facility themselves. Keycards are given
to student’s, phd’s, postdoc’s and PI’s. The card readers also read out the
current time (0-23) and whether the entering person has a safety training from
Marcus. 

Rules:
-	During an emergency, doors can always be unlocked with every keycard.
    Output: “Emergency access granted.”
-	People can only enter, when they have their safety training.
    If not, the system will inform: “Access denied: Safety training missing.”
-	Students may enter between 8 and 18 o’clock “Hello there, young padawan”,
    but not else: “Access denied: Outside student hours.”
-	PhD students and Postdocs may enter at any time. “Welcome working slave.”
-	The PI is always allowed to enter and doesn’t need a safety training. “All hail the king.”

Write a Python script, that prints exactly one message depending on the situation.
Try to use “and”, “or” and “not”. Nesting your if statements dependent on priority
might be helpful here!

Learning Goals:
- Nesting if statements
- Importance of prioritization
- more complicated logics
"""

# these options are possible and need to be accounted for:
career_state = ["student", "phd", "postdoc", "PI"]
time = random.randint(0, 23) # feel free to set a manual time here
has_training = [True, False]

# this data structure is really suitable for a dictionary
# we create a possible card user here
simons_card = {
    # here, the random module can be helpful again - can you guess, what random.choice() does?
    "career state": random.choice(career_state),
    "time": time,
    "has training": random.choice(has_training)
    }

# current emergency status
emergency = False

# Optional readout for testing:
print(simons_card)

# rules in decending priority
if emergency:
    print("Emergency access granted.")
elif simons_card["career state"] == "PI":
    print("All hail the king.")
else:
    if not simons_card["has training"]:
        print("Access denied: Safety training missing.")
    elif simons_card["career state"] == "postdoc" or simons_card["career state"] == "phd":
        print("Welcome working slave.")
    elif simons_card["career state"] == "student" and 18 >= simons_card["time"] >= 8:
        print("Hello there, young padawan.")
    else:
        print("Access denied: Outside student hours.")
        


