# Program to find HCF/GCD of two numbers

# Enter 2 numbers
numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))

# Using Euclidean Algorithms
while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)