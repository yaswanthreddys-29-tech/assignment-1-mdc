# Q3. With a given integral number n, write a program to generate 
# a dictionary that contains (i, i*i).
# Example: input 5 → output {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter a number: "))
squares = {i: i*i for i in range(1, n+1)}
print(squares)