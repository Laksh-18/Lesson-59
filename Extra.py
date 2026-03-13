# Get the number of chocolates and candies from the user
chocolates = int(input("Enter the number of chocolates: "))
candies = int(input("Enter the number of candies: "))

a = chocolates
b = candies

while b:
    temp = b
    b = a % b
    a = temp

print ("Maximum gift boxes:", a)