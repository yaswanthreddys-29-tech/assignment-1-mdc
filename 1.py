# Q1. Write a program which will find all such numbers 
# which are divisible by 7 but are not a multiple of 3, 
# between 2000 and 3200. Printed the output as a comma-separated sequence.

numbers = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 3 != 0]
print(",".join(numbers))