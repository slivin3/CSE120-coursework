##Created by SAL on 11/18/2024

#Instructions: Write a program that accepts a dollar amount 0.00 and 0.99 as an input and display exact changes for this amount using the minimum number of coins.
#For example, $0.97 shows 3 quarters, 2 dimes, and 2 pennies.
##Note to self:**Use multiple loops of Modulus "%" in Python to find out how many of each denomination coin will be used.

#
Change_needed = float(input("How much change do you have? Enter in 0.xx format for under $1"))

#This line below will alter the 'Change_needed variable so it is not less than 0 for ease of math.  Also change the value from a float to integer.
Change_needed = int(Change_needed * 100)


Quarters = int(Change_needed / 25)
Change_needed = Change_needed % 25
print(Quarters, Change_needed,"Cents leftover")

Dimes = int(Change_needed / 10)
Change_needed = int(Change_needed) % 10
print(Dimes, Change_needed,"Cents leftover")

Nickels = int(Change_needed / 5)
Change_needed = int(Change_needed) % 5
print(Nickels, Change_needed,"Cents leftover")

Pennies = int(Change_needed / 1)
Change_needed = int(Change_needed) % 1
print(Pennies, Change_needed,"Cents leftover")
