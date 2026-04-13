########################################################################################################################
# Created on Tue 26_01_13   #   Created by Melissa Franke   #   fair use in Chemosensation Coding Workshop
# Last edit: 26_04_07       #   Edited by Melissa Franke
########################################################################################################################

# function definition
def binary_converter(bin_number: str) -> int:
    error= False                        # this can help you in the exercise
    bin_number=bin_number[::-1]         # reverse binary number
    dec_number=0                        # declare dec_number
    for i in range(0,len(bin_number)):  # iterate through all letters of input
        if bin_number[i]=='1':          # if the letter is 1
            dec_number=dec_number+2**i  # perform the calculation to get the correct decimal number according to position of 1
    return dec_number, error                   # return decimal number

# user input:
binary_number='00101010'
# funciton call
decimal_number, error= binary_converter(binary_number)
# output:
print(decimal_number)